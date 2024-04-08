#!/usr/bin/python3
import sys

SVG_TEMPLATE='''\
<svg width="%s" height="%s" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
%s
</svg>'''

RECT_TEMPLATE='<rect x="%s" y="%s" width="%s" height="%s" rx="%s" ry="%s" fill="%s" />'

LINE_TEMPLATE='<line x1="%s" y1="%s" x2="%s" y2="%s" style="stroke:%s;stroke-width:%s" />'

TEXT_TEMPLATE = '<text x="%s" y="%s" textLength="%s" fill="%s" font-family="%s" text-anchor="middle" lengthAdjust="spacingAndGlyphs">%s</text>'

CIRCLE_TEMPLATE = '<circle cx="%s" cy="%s" r="%s" fill="%s" />'

context = { 'color': 'gray', 'text_color': 'black', 'edge_width': 3,
            'diagram_width': 1000, 'diagram_height': 750,
            'font_half_height': 6, 'font_average_width': 10, 'font_family': 'helvetica,arial,sans-serif' }
          #, 'edge_color': None, 'node_color': None

objects = { }

def to_number(s):
    if s.isnumeric():
        return int(s)
    return float(s)

def to_string(n):
    if type(n) == str:
        return n
    if n == int(n):
        return '%d' % n
    if type(n) == float:
        return '%f' % n
    return '%s' % n

def to_strings(*args):
    return tuple(to_string(x) for x in args)

def partition(pred, items):
    truefor, falsefor = [], []
    for it in items:
        if pred(it):
            truefor.append(it)
        else:
            falsefor.append(it)
    return truefor, falsefor

def tokenize(s):
    if '"' not in s and "'" not in s:
        return s.split()
    # need to do it the hard way...
    # go until ", split that, then go until closing " and make single token
    length = len(s)
    tokens = []
    acc = ''
    i = 0
    while i < length:
        c = s[i]
        if c in ['"', "'"]:
            if acc:
                tokens += acc.split(' ')
                acc = ''
            i += 1
            start = i
            while i < length and s[i] != c:
                i += 1
            tokens.append(s[start:i])
        else:
            acc += c
        i += 1
    if acc:
        tokens += acc.split(' ')
    return [t for t in tokens if t]

def parse(tokens):
    r = {}
    r['list'] = []
    r['name'] = tokens[0]
    r['id'] = tokens[1]
    i = 2
    while i < len(tokens):
        current_token = tokens[i]
        # special so far: center size ul ll ur lr color from to
        if current_token in ['center', 'size', 'ul', 'll', 'ur', 'lr']:
            r[current_token] = (to_number(tokens[i+1]), to_number(tokens[i+2]))
            i += 3
        elif current_token in ['color', 'text-color', 'from', 'to', 'width', 'height', 'radius', 'url']:
            r[current_token] = tokens[i+1]
            i += 2
        else:
            r['list'].append(current_token)
            i += 1
    return r

def make_object(parsed):
    kind = parsed['name']
    if kind == 'color':
        context['color'] = parsed['id']
        return None
    elif kind == 'edge':
        return make_edge(parsed)
    elif kind == 'rect':
        return make_rect(parsed)
    elif kind == 'rrect':
        return make_rounded_rect(parsed)
    elif kind == 'oval':
        return make_oval(parsed)
    elif kind == 'circle':
        return make_circle(parsed)
    elif kind == 'diagram':
        return make_diagram(parsed)
    else:
        return None

def get_ul(r):
    if 'ul' in r:
        return r['ul']
    c = r['center']
    s = r['size']
    return (c[0]-s[0]/2.0, c[1]-s[1]/2.0)

def get_center(r):
    if 'center' in r:
        return r['center']
    ul = r['ul']
    s = r['size']
    return (ul[0]+s[0]/2.0, ul[1]+s[1]/2.0)

def get_color_for_type(t):
    if (t + '_color') in context:
        return context[t + '_color']
    return context['color']

def get_color(r):
    if 'color' in r:
        return r['color']
    return get_color_for_type('node')

def get_text_color(r):
    if 'text-color' in r:
        return r['text-color']
    return get_color_for_type('text')

def get_font_family(r):
    if 'font-family' in r:
        return r['font-family']
    return context['font_family']

def get_label(item):
    if 'label' in item:
        return item['label']
    if 'list' in item:
        ls = item['list']
        if ls:
            return ls[0]
    return item['id']

def get_url(item):
    if 'url' in item:
        return item['url']

def get_text_width(s, maxwidth):
    return min(context['font_average_width'] * len(s), maxwidth*.95)

def make_either_rect(item, rx, ry):
    label = get_label(item)
    x, y = get_ul(item)
    width, height = item['size']
    textwidth = get_text_width(label, width)
    textx, texty = get_center(item)
    texty += context['font_half_height']
    node = (RECT_TEMPLATE % to_strings(x, y, width, height, rx, ry, get_color(item))
            + TEXT_TEMPLATE % to_strings(textx, texty, textwidth, get_text_color(item),
                                         get_font_family(item), label))
    url = get_url(item)
    if url:
        node = ('<a xlink:href="%s" xlink:title="click">' % url) + node + '</a>'
    return node

def make_rect(r):
    return make_either_rect(r, 0, 0)

def make_rounded_rect(r):
    return make_either_rect(r, 10, 10)

def make_oval(r):
    s = r['size']
    m = min(s[0], s[1])/2.0
    return make_either_rect(r, m, m)

def make_circle(item):
    label = get_label(item)
    x, y = item['center']
    r = to_number(item['radius'])
    textwidth = get_text_width(label, 2 * r)
    texty = y + context['font_half_height']
    node = (CIRCLE_TEMPLATE % to_strings(x, y, r, get_color(item))
            + TEXT_TEMPLATE % to_strings(x, texty, textwidth, get_text_color(item),
                                         get_font_family(item), label))
    url = get_url(item)
    if url:
        node = ('<a xlink:href="%s" xlink:title="click">' % url) + node + '</a>'
    return node

def split_at_last(s, d):
    if d in s:
        return (s[:s.rfind(d)], s[s.rfind(d)+1:])
    return (s, None)

def is_edge(obj):
    return obj['name'] == 'edge'

def get_start(edge):
    sourceid, pos = split_at_last(edge['from'], '.')
    source = objects[sourceid]
    return get_center(source)

def get_end(edge):
    destid, pos = split_at_last(edge['to'], '.')
    dest = objects[destid]
    return get_center(dest)

def get_width(edge):
    if 'width' in edge:
        return edge['width']
    return context['edge_width']

def make_edge(edge):
    color = get_color(edge)
    width = get_width(edge)
    x1, y1 = get_start(edge)
    x2, y2 = get_end(edge)
    return LINE_TEMPLATE % to_strings(x1, y1, x2, y2, color, width)

def make_diagram(diagram):
    context['diagram_width']  = diagram['width']
    context['diagram_height'] = diagram['height']

def update_context(args):
    errors = []
    for a in args:
        if '=' in a:
            k, v = a.split('=', 1)
            if k in context:
                t = type(context[k])
                context[k] = t(v)
            else:
                errors.append('  unknown default: %s' % k)
    if errors:
        print('error:', file=sys.stderr)
        for err in errors:
            print(err, file=sys.stderr)
        print('valid defaults are:', ' '.join(context.keys()), file=sys.stderr)
        sys.exit(2)

def open_file(args):
    if args[0] != '-':
        return open(args[0])
    return sys.stdin

def main(args):
    filenameargs = [a for a in args if '=' not in a]
    lines = open_file(filenameargs + ['-']).readlines()
    lines = [line.rstrip('\r\n') for line in lines]
    update_context(args)

    # remove blank lines and comment lines (first non-whitespace char is #):
    lines = [line for line in lines if line.lstrip() and line.lstrip()[0] != '#']
    parsed = [parse(tokenize(line)) for line in lines]
    for obj in parsed:
        objects[obj['id']] = obj
    edges, nonedges = partition(is_edge, parsed)

    svgobjects = [make_object(thing) for thing in edges + nonedges]
    svgobjects = [ob for ob in svgobjects if ob]
    print(SVG_TEMPLATE % (context['diagram_width'], context['diagram_height'], '\n'.join(svgobjects)))

if __name__ == '__main__':
    main(sys.argv[1:])
