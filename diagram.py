#!/usr/bin/python3
import sys

SVG_TEMPLATE='''\
<svg width="%s" height="%s" xmlns="http://www.w3.org/2000/svg">
%s
</svg>'''

RECT_TEMPLATE='<rect x="%s" y="%s" width="%s" height="%s" rx="%s" ry="%s" fill="%s" />'

LINE_TEMPLATE='<line x1="%s" y1="%s" x2="%s" y2="%s" style="stroke:%s;stroke-width:%s" />'

TEXT_TEMPLATE = '<text x="%s" y="%s" textLength="%s" fill="%s" text-anchor="middle" lengthAdjust="spacingAndGlyphs">%s</text>'

CIRCLE_TEMPLATE = '<circle cx="%s" cy="%s" r="%s" fill="%s" />'

context = { 'color': 'gray', 'text_color': 'black', 'edge_width': 3,
            'diagram_width': 1000, 'diagram_height': 750, 'font_half_height': 6, }
          #, 'edge_color': None, 'node_color': None

objects = { }

def to_number(s):
    if s.isnumeric():
        return int(s)
    return float(s)

def to_string(n):
    if n == int(n):
        return '%d' % n
    return '%f' % n

def partition(pred, items):
    truefor, falsefor = [], []
    for it in items:
        if pred(it):
            truefor.append(it)
        else:
            falsefor.append(it)
    return truefor, falsefor

def tokenize(s):
    # later, respect quotes
    return s.split()

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
        elif current_token in ['color', 'text-color', 'from', 'to', 'width', 'height', 'radius']:
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

def get_label(item):
    if 'label' in item:
        return item['label']
    if 'list' in item:
        ls = item['list']
        if ls:
            return ls[0]
    return item['id']

def make_either_rect(r, rx, ry):
    label = get_label(r)
    color = get_color(r)
    textcolor = get_text_color(r)
    ul = get_ul(r)
    x = to_string(ul[0])
    y = to_string(ul[1])
    s = r['size']
    width = to_string(s[0])
    height = to_string(s[1])
    textwidth = to_string(s[0]*.95)
    c = get_center(r)
    textx = to_string(c[0])
    texty = to_string(c[1] + context['font_half_height'])
    return (RECT_TEMPLATE % (x, y, width, height, rx, ry, color)
            + TEXT_TEMPLATE % (textx, texty, textwidth, textcolor, label))

def make_rect(r):
    return make_either_rect(r, 0, 0)

def make_rounded_rect(r):
    return make_either_rect(r, 10, 10)

def make_oval(r):
    s = r['size']
    m = min(s[0], s[1])/2.0
    return make_either_rect(r, m, m)

def make_circle(item):
    r = to_number(item['radius'])
    textwidth = to_string(2*r*.95)
    r = to_string(r)
    c = item['center']
    x, y = to_string(c[0]), to_string(c[1])
    label = get_label(item)
    color = get_color(item)
    textcolor = get_text_color(item)
    return (CIRCLE_TEMPLATE % (x, y, r, color)
            + TEXT_TEMPLATE % (x, y, textwidth, textcolor, label))

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
    return LINE_TEMPLATE % (to_string(x1), to_string(y1), to_string(x2), to_string(y2), color, width)

def make_diagram(diagram):
    context['diagram_width']  = diagram['width']
    context['diagram_height'] = diagram['height']

def open_file(args):
    if args[0] != '-':
        return open(args[0])
    return sys.stdin

def main(args):
    lines = open_file(args + ['-']).readlines()

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
