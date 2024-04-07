#!/usr/bin/python3
import sys

SVG_TEMPLATE='''\
<svg width="1000" height="750" xmlns="http://www.w3.org/2000/svg">
%s
</svg>'''

RECT_TEMPLATE='<rect x="%s" y="%s" width="%s" height="%s" rx="%s" ry="%s" fill="%s" />'

LINE_TEMPLATE='<line x1="%s" y1="%s" x2="%s" y2="%s" style="stroke:%s;stroke-width:%s" />'

context = { 'color': 'gray', 'edge_width': 3 } #, 'edge_color': None, 'node_color': None

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
        elif current_token in ['color', 'from', 'to', 'width']:
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
    elif kind == 'rect':
        return make_rect(parsed)
    elif kind == 'rrect':
        return make_rounded_rect(parsed)
    elif kind == 'edge':
        return make_edge(parsed)
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

def make_rect(r):
    ul = get_ul(r)
    s = r['size']
    color = get_color(r)
    return RECT_TEMPLATE % (to_string(ul[0]), to_string(ul[1]), to_string(s[0]), to_string(s[1]), 0, 0, color)

def make_rounded_rect(r):
    ul = get_ul(r)
    s = r['size']
    color = get_color(r)
    return RECT_TEMPLATE % (to_string(ul[0]), to_string(ul[1]), to_string(s[0]), to_string(s[1]), 10, 10, color)

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
    print(SVG_TEMPLATE % '\n'.join(svgobjects))

if __name__ == '__main__':
    main(sys.argv[1:])
