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

RECT_TEMPLATE='<rect x="%f" y="%f" width="%f" height="%f" rx="%f" ry="%f" fill="%s" />'

context = { 'color': None, 'edge_color': None, 'node_color': None }

def to_number(s):
    if s.isnumeric():
        return int(s)
    return float(s)

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
        return RECT_TEMPLATE % (10, 10, 20, 15, 0, 0, context['color'])
    else:
        return None

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
