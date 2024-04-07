#!/usr/bin/python3

INPUT='''
color blue
rect A "Starting_Point" center 100 100 size 100 50
rrect B "Ending_Point" ul 300 300 size 100 150 color green
edge E from A.lr to B
'''

SVG_TEMPLATE='''\
<svg width="1000" height="750" xmlns="http://www.w3.org/2000/svg">
%s
</svg>'''

RECT_TEMPLATE='<rect x="%s" y="%s" width="%s" height="%s" rx="%s" ry="%s" fill="%s" />'

context = { 'color': None, 'edge_color': None, 'node_color': None }

def to_number(s):
    if s.isnumeric():
        return int(s)
    return float(s)

def to_string(n):
    if n == int(n):
        return '%d' % n
    return '%f' % n

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
        elif current_token in ['color', 'from', 'to']:
            r[current_token] = tokens[i+1]
            i += 2
        else:
            r['list'].append(current_token)
            i += 1
    return r

def make_object(s):
    tokens = tokenize(s)
    print('tokens:',tokens)
    parsed = parse(tokens)
    print('parsed:',parsed)
    t0 = tokens[0]
    if t0 == 'color':
        context['color'] = tokens[1]
        return None
    elif t0 == 'rect':
        return make_rect(parsed)
    elif t0 == 'rrect':
        return make_rounded_rect(parsed)
    else:
        return None

def get_ul(r):
    if 'ul' in r:
        return r['ul']
    c = r['center']
    s = r['size']
    return (c[0]-s[0]/2.0, c[1]-s[1]/2.0)

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

def main(args):
    # for now, just ignore the args and use our hard-coded input:
    lines = INPUT.split('\n')
    # remove blank lines and comment lines (first non-whitespace char is #):
    lines = [line for line in lines if line.lstrip() and line.lstrip()[0] != '#']
    objects = [make_object(line) for line in lines]
    objects = [ob for ob in objects if ob]
    #print(objects)
    print(SVG_TEMPLATE % '\n'.join(objects))

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
