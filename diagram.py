#!/usr/bin/python3

INPUT='''
color blue
rect A "Starting_Point" center 100 100 size 100 50
rrect B "Ending_Point" ul 300 300 size 100 150 color green
edge E from A lr to B
'''

SVG_TEMPLATE='''\
<svg width="1000" height="750" xmlns="http://www.w3.org/2000/svg">
%s
</svg>'''

RECT_TEMPLATE='<rect x="%f" y="%f" width="%f" height="%f" rx="%f" ry="%f" fill="%s" />'

context = { 'color': None, 'edge_color': None, 'node_color': None }

def tokenize(s):
    # later, respect quotes
    return s.split()

def make_object(s):
    tokens = tokenize(s)
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
