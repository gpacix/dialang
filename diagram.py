#!/usr/bin/python3
import sys
import math

SVG_TEMPLATE='''\
<svg width="%s" height="%s" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<!-- generated by https://github.com/gpacix/dialang; source for this diagram:
%s
-->
%s
%s
</svg>'''

STYLESHEET_TEMPLATE='<link xmlns="http://www.w3.org/1999/xhtml" rel="stylesheet" href="%s" type="text/css" />'

STYLE_TEMPLATE='<style>\n%s</style>\n'

RECT_TEMPLATE='<rect id="%s" class="node %s" x="%s" y="%s" width="%s" height="%s" rx="%s" ry="%s" fill="%s" />'

LINE_TEMPLATE='<line id="%s" class="edge %s" x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" />'

TEXT_TEMPLATE = '<text id="%s" class="text %s" x="%s" y="%s" textLength="%s" fill="%s" font-family="%s" text-anchor="middle" lengthAdjust="spacingAndGlyphs">%s</text>'

CIRCLE_TEMPLATE = '<circle id="%s" class="node %s" cx="%s" cy="%s" r="%s" fill="%s" />'

DIAMOND_TEMPLATE = '<g transform="translate(%s,%s), scale(%s,%s)"><polygon id="%s" class="node %s" fill="%s" points="-0.5 0  0 0.5  0.5 0  0 -0.5" /></g>'

POLYGON_TEMPLATE = '<g transform="translate(%s,%s) rotate(%s)"><polygon id="%s" class="%s" points="%s" fill="%s" /></g>'

DIAMOND_POINTS = [-0.5, 0,  0, 0.5,  0.5, 0,  0, -0.5]

ARROWHEAD_POINTS = [ -1, 0,  -1, -0.5,  0, 0,  -1, 0.5 ]

PARALLELOGRAM_POINTS = [0.5, -0.5,  0.3, 0.5,  -0.5, 0.5,  -0.3, -0.5]

KINDS = [ 'color', 'edge', 'rect', 'rrect', 'oval', 'circle', 'diamond',
          'cloud', 'cylinder', 'para', 'hex', 'diagram' ]

class Shape:
    def __init__(self, size, stroke_width, path):
        self.size = size
        self.stroke_width = stroke_width
        self.path = path

    PATH_TEMPLATE = '''<g transform="translate(%s,%s), scale(%s,%s)"><g transform="translate(%s,%s)">
<path id="%s" class="node %s" fill="%s" stroke="%s" style="stroke-width:%s"
       d="%s" /></g></g>'''

    def emit(self, x, y, width, height, id, additional_class, fill, stroke):
        xscale, yscale = width / self.size[0], height / self.size[1]
        return (self.PATH_TEMPLATE %
                to_strings(x, y, xscale, yscale, -self.size[0]/2, -self.size[1]/2, id,
                           additional_class, fill, stroke, self.stroke_width, self.path))

# This image is 118 x 80
# x y  xscale yscale id class fill stroke
cloud = Shape((118, 80), "5px", '''M72,19c13.117,0,23.809,10.578,23.996,23.648c-0.02,0.266-0.035,0.535-0.035,0.75
       c0,3.809,2.688,7.09,6.422,7.844 C107.957,52.363,112,57.309,112,63c0,6.617-5.383,12-12,12
       H14.508c-0.379-0.125-0.773-0.223-1.176-0.289C5.605,73.406,0,67.801,0,59c0-8.824,7.176-16,16-16
       a 15 15 0 1 1 ,20-23  a 15 15 0 1 1, 36.5 -1''')

# CLOUD_TEMPLATE = '''<g transform="translate(%s,%s), scale(%s,%s)"><g transform="translate(-56,-38)">
# <path id="%s" class="node %s" fill="%s" stroke="%s" style="stroke-width:5px"
#        d="M72,19c13.117,0,23.809,10.578,23.996,23.648c-0.02,0.266-0.035,0.535-0.035,0.75
#        c0,3.809,2.688,7.09,6.422,7.844 C107.957,52.363,112,57.309,112,63c0,6.617-5.383,12-12,12
#        H14.508c-0.379-0.125-0.773-0.223-1.176-0.289C5.605,73.406,0,67.801,0,59c0-8.824,7.176-16,16-16
#        a 15 15 0 1 1 ,20-23  a 15 15 0 1 1, 36.5 -1" /></g></g>'''

# This image is 52 x 68
# x y  xscale yscale id class fill stroke

cylinder = Shape((52, 68), "3px", '''M1,9 v 50 a 25 8  0 0 0 50 0 v -50  a 25 8  0 1 0 -50 0  a 25 8  0 1 0 50 0''')
# CYLINDER_TEMPLATE = '''<g transform="translate(%s,%s), scale(%s,%s)"><g transform="translate(-26,-34)">
# <path id="%s" class="node %s" fill="%s" stroke="%s" style="stroke-width:3px"
#        d="M1,9 v 50 a 25 8  0 0 0 50 0 v -50  a 25 8  0 1 0 -50 0  a 25 8  0 1 0 50 0" /></g></g>'''

parallelogram = Shape((100, 60), "1px", '''M 60,60 h -60 l 30 -60 h 60 l -30 60''') #  H 100 L 100 60

hexagon = Shape((100, 60), "1px", '''M 20,60 l -20 -30 l 20 -30 h 60 l 20 30 l -20 30 h -60''')

context = { 'color': '#C0C0C0', 'text_color': 'black', 'edge_width': 3,
            'diagram_width': 1000, 'diagram_height': 750,
            'font_half_height': 6, 'font_average_width': 10, 'font_family': 'helvetica,arial,sans-serif',
            'css_href': '', 'style': 'default'}
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

def tokenize(line):
    num, s = line
    if '"' not in s and "'" not in s:
        return num, s.split()
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
    return num, [t for t in tokens if t]

def parse(ntokens):
    num, tokens = ntokens
    r = {}
    r['list'] = []

    kind = tokens[0]
    if kind not in KINDS:
            print('Unknown element type "%s" in line %d with tokens %s' % (kind, num, tokens), file=sys.stderr)
            print(lines0[num-1], file=sys.stderr)
            sys.exit(9)
    r['name'] = kind

    if len(tokens) < 2:
        print("Missing ID for %s in line %d with tokens %s" % (tokens[0], num, tokens), file=sys.stderr)
        print(lines0[num-1], file=sys.stderr)
        sys.exit(8)
    r['id'] = tokens[1]
    i = 2
    while i < len(tokens):
        current_token = tokens[i]
        try:
            # special so far: center size ul ll ur lr color from to
            if current_token in ['center', 'size', 'ul', 'll', 'ur', 'lr']:
                r[current_token] = (to_number(tokens[i+1]), to_number(tokens[i+2]))
                i += 3
            elif current_token in ['color', 'text-color', 'from', 'to', 'width', 'height',
                                   'url', 'stylesheet', 'style', 'class', 'text-class', 'arrow']:
                r[current_token] = tokens[i+1]
                i += 2
            elif current_token in ['z', 'radius']:
                r[current_token] = to_number(tokens[i+1])
                i += 2
            else:
                r['list'].append(current_token)
                i += 1
        except IndexError as ie:
            print("Missing value for %s in line %d with tokens %s" % (current_token, num, tokens), file=sys.stderr)
            print(lines0[num-1], file=sys.stderr)
            sys.exit(5)
        except ValueError as ve:
            print("Numeric value required for %s in line %d with tokens %s" % (current_token, num, tokens), file=sys.stderr)
            print(lines0[num-1], file=sys.stderr)
            sys.exit(7)

    if r['name'] not in ['diagram', 'edge']:
        try:
            calculate_dimensions(r)
        except TypeError:
            print("Error with dimensions or size in line %d with tokens %s" % (num, tokens), file=sys.stderr)
            print(lines0[num-1], file=sys.stderr)
            sys.exit(3)
    return num, r

def make_object(nparsed):
    num, parsed = nparsed
    try:
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
        elif kind == 'diamond':
            return make_diamond(parsed)
        elif kind == 'cloud':
            return make_cloud(parsed)
        elif kind == 'cylinder':
            return make_cylinder(parsed)
        elif kind == 'para':
            return make_shape(parsed, parallelogram)
        elif kind == 'hex':
            return make_shape(parsed, hexagon)
        elif kind == 'diagram':
            return make_diagram(parsed)
        else:
            return None
    except KeyError as ke:
        print("Missing property %s in line %d with tokens %s" % (ke, num, parsed), file=sys.stderr)
        print(lines0[num-1], file=sys.stderr)
        sys.exit(4)

def get_id(item):
    # we 100% fully expect to have an ID, but...
    if 'id' in item:
        return item['id']
    return 'unknown' # this will not be unique

def calculate_bounds(x1, x2, xc, dx):
    "Figure out x1 and x2 given any 2 inputs"
    #print("calculate_bounds:", x1, x2, xc, dx)
    if x1 is None:
        if x2 is None:
            x1 = xc - dx/2
        else:
            if dx is None:
                x1 = 2*xc - x2
            else:
                x1 = x2 - dx
    if x2 is None:
        # have x1; which other do we have?
        if dx is None:
            x2 = 2*xc - x1
        else:
            x2 = x1 + dx
    return x1, x2

def calculate_dimensions(r):
    "Make sure r has enough information to determine its bounding box"
    # figure out info we do have: x1, y1, xc, yc, x2, y2
    #print('calculate_dimensions:', r)
    x1, y1, x2, y2 = None, None, None, None
    xc, yc, dx, dy = None, None, None, None
    for k in r:
        if k == 'ul':
            x1, y1 = r[k]
        elif k == 'll':
            x1, y2 = r[k]
        elif k == 'ur':
            x2, y1 = r[k]
        elif k == 'lr':
            x2, y2 = r[k]
        elif k == 'center':
            xc, yc = r[k]
        elif k == 'size':
            dx, dy = r[k]
        elif k == 'radius':
            dx, dy = 2*r[k], 2*r[k]
    #print('calculate_dimensions:', (x1, y1, x2, y2, xc, yc, dx, dy))
    x1, x2 = calculate_bounds(x1, x2, xc, dx)
    y1, y2 = calculate_bounds(y1, y2, yc, dy)
    r['ul'] = (x1, y1)
    r['lr'] = (x2, y2)

def get_ul(r):
    if 'ul' in r:
        return r['ul']
    c = r['center']
    s = r['size']
    return (c[0]-s[0]/2.0, c[1]-s[1]/2.0)

def get_lr(r):
    if 'lr' in r:
        return r['lr']
    c = r['center']
    s = r['size']
    return (c[0]+s[0]/2.0, c[1]+s[1]/2.0)

def get_center(r):
    if 'center' in r:
        return r['center']
    ul = r['ul']
    s = get_size(r)
    return (ul[0]+s[0]/2.0, ul[1]+s[1]/2.0)

def get_size(r):
    if 'size' in r:
        return r['size']
    ul = r['ul']
    lr = r['lr']
    return (lr[0] - ul[0], lr[1] - ul[1])

def get_z(nitem):
    num, item = nitem
    if 'z' in item:
        return item['z']
    elif item['name'] == 'edge':
        return 0
    return 1

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

def get_class_str(item):
    if 'class' in item:
        return ' ' + item['class']
    return ''

def get_text_class_str(item):
    if 'text-class' in item:
        return ' ' + item['text-class']
    elif 'class' in item:
        return ' ' + item['class']
    return ''

def get_text_width(s, maxwidth, hint=.95):
    return min(context['font_average_width'] * len(s), maxwidth*hint)

def scale_points(points, w, h):
    r = points[:]
    for i in range(len(r)):
        r[i] *= w
        w, h = h, w
    return ' '.join([to_string(n) for n in r])

def entity_encode(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def dash_encode(s):
    "Two dashes is illegal inside an XML comment, so escape one"
    return s.replace('--', '&#45;-')

def id_encode(s):
    '''Encode s as an XML ID, meaning it matches: [A-Za-z_][A-Za-z_0-9\\.-]*,
       by replacing illegal characters with _ ; guaranteed to return a string'''
    if not s:
        return ''
    id = ''
    for i in range(len(s)):
        c = s[i]
        if not (c.isalnum() or c in '_-.'):
            c = '_'
        id += c
    if id[0] != '_' and  not id[0].isalpha():
        id[0] = '_'
    else:
        id = '_'
    return id

def make_either_rect(item, rx, ry):
    label = get_label(item)
    x, y = get_ul(item)
    width, height = get_size(item)
    textwidth = get_text_width(label, width)
    textx, texty = get_center(item)
    texty += context['font_half_height']
    css_classes = get_class_str(item)
    text_css_classes = get_text_class_str(item)
    node = (RECT_TEMPLATE % to_strings(get_id(item), css_classes, x, y, width, height, rx, ry, get_color(item))
            + TEXT_TEMPLATE % to_strings(get_id(item)+'-label', text_css_classes, textx, texty, textwidth,
                                         get_text_color(item), get_font_family(item), label))
    url = get_url(item)
    if url:
        node = ('<a xlink:href="%s" xlink:title="click">' % entity_encode(url)) + node + '</a>'
    return node

def make_rect(r):
    return make_either_rect(r, 0, 0)

def make_rounded_rect(r):
    return make_either_rect(r, 10, 10)

def make_oval(r):
    s = get_size(r)
    m = min(s[0], s[1])/2.0
    return make_either_rect(r, m, m)

def make_circle(item):
    label = get_label(item)
    x, y = item['center']
    r = item['radius']
    textwidth = get_text_width(label, 2 * r)
    texty = y + context['font_half_height']
    css_classes = get_class_str(item)
    text_css_classes = get_text_class_str(item)
    node = (CIRCLE_TEMPLATE % to_strings(get_id(item), css_classes, x, y, r, get_color(item))
            + TEXT_TEMPLATE % to_strings(get_id(item)+'-label', text_css_classes, x, texty, textwidth,
                                         get_text_color(item), get_font_family(item), label))
    url = get_url(item)
    if url:
        node = ('<a xlink:href="%s" xlink:title="click">' % url) + node + '</a>'
    return node

def make_diamond(item):
    label = get_label(item)
    x, y = get_center(item)
    width, height = get_size(item)
    textwidth = get_text_width(label, width, .6)
    texty = y + context['font_half_height']
    css_classes = get_class_str(item)
    text_css_classes = get_text_class_str(item)
    # TODO: why do we need to divide by 4.0? What's going on?
    # part was the stroke-width; why are the diamonds all stroke-colored?
    # diamond_points = [-0.5, 0,  0, 0.5,  0.5, 0,  0, -0.5]
    points_string = scale_points(DIAMOND_POINTS, width, height)
    rotation = 0
    node = (POLYGON_TEMPLATE % to_strings(x, y, rotation, get_id(item), 'node ' + css_classes, points_string, get_color(item))
            + TEXT_TEMPLATE % to_strings(get_id(item)+'-label', text_css_classes, x, texty, textwidth,
                                         get_text_color(item), get_font_family(item), label))
    url = get_url(item)
    if url:
        node = ('<a xlink:href="%s" xlink:title="click">' % url) + node + '</a>'
    return node

def make_cloud(item):
    label = get_label(item)
    x, y = get_center(item)
    width, height = get_size(item)
    #xscale, yscale = width / 118, height / 80
    textwidth = get_text_width(label, width, .6)
    texty = y + 2.5*context['font_half_height']
    css_classes = get_class_str(item)
    text_css_classes = get_text_class_str(item)
#    node = (CLOUD_TEMPLATE % to_strings(x, y, xscale, yscale, get_id(item), css_classes, "none", get_color(item))
    node = (cloud.emit(x, y, width, height, get_id(item), css_classes, "none", get_color(item))
            + TEXT_TEMPLATE % to_strings(get_id(item)+'-label', text_css_classes, x, texty, textwidth,
                                         get_text_color(item), get_font_family(item), label))
    url = get_url(item)
    if url:
        node = ('<a xlink:href="%s" xlink:title="click">' % url) + node + '</a>'
    return node

def make_cylinder(item):
    label = get_label(item)
    x, y = get_center(item)
    width, height = get_size(item)
    #xscale, yscale = width / 42, height / 34
    textwidth = get_text_width(label, width, .6)
    texty = y + 1.5*context['font_half_height'] ## TODO: adjust this
    css_classes = get_class_str(item)
    text_css_classes = get_text_class_str(item)
#    node = (CYLINDER_TEMPLATE % to_strings(x, y, xscale, yscale, get_id(item), css_classes, "white", get_color(item))
    node = (cylinder.emit(x, y, width, height, get_id(item), css_classes, "white", get_color(item))
            + TEXT_TEMPLATE % to_strings(get_id(item)+'-label', text_css_classes, x, texty, textwidth,
                                         get_text_color(item), get_font_family(item), label))
    url = get_url(item)
    if url:
        node = ('<a xlink:href="%s" xlink:title="click">' % url) + node + '</a>'
    return node

def make_shape(item, shape):
    label = get_label(item)
    x, y = get_center(item)
    width, height = get_size(item)
    #xscale, yscale = width / 100, height / 60
    textwidth = get_text_width(label, width, .6)
    texty = y + 1*context['font_half_height'] ## TODO: adjust this
    css_classes = get_class_str(item)
    text_css_classes = get_text_class_str(item)
    node = (shape.emit(x, y, width, height, get_id(item), css_classes, "white", get_color(item))
            + TEXT_TEMPLATE % to_strings(get_id(item)+'-label', text_css_classes, x, texty, textwidth,
                                         get_text_color(item), get_font_family(item), label))
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

def get_endpoint(edge, fromto):
    objid, pos = split_at_last(edge[fromto], '.')
    if objid not in objects:
        print("Unknown node with ID %s for edge %s" % (objid, edge), file=sys.stderr)
        #print(lines0[num-1], file=sys.stderr)
        sys.exit(6)
    return objects[objid]

def get_start(edge):
    return get_endpoint(edge, 'from')

def get_end(edge):
    return get_endpoint(edge, 'to')

def get_width(edge):
    if 'width' in edge:
        return edge['width']
    return context['edge_width']

def get_arrow(edge):
    if 'arrow' in edge:
        return edge['arrow']
    return 'none'

def find_nearest_port(dest, source):
    "Return a port (e.g. ul, lc) on dest that faces source"
    dc = get_center(dest)
    sc = get_center(source)
    # we want the angle FROM dest, since it's easier to think about:
    angle = math.atan2(sc[1] - dc[1], sc[0] - dc[0]) * 180 / math.pi
    # 0 is to the right, negative is counter-clockwise, positive is clockwise
    # each port gets 360/8 = 45 degrees, so mr is -22.5 to 22.5
    angle_i = int((-angle + 180 + 22.5) / 45)
    #print(angle, angle_i)
    #sys.exit(0)
    return ['ml', 'll', 'lc', 'lr', 'mr', 'ur', 'uc', 'ul', 'ml'][angle_i]

def get_port_pos(item, port):
    "Specify port as {uml}{lcr}"
    v, h = port[0], port[1]
    if v == 'u':
        y = get_ul(item)[1]
    elif v == 'l':
        y = get_lr(item)[1]
    else: # v == 'm':
        y = get_center(item)[1]
    if h == 'l':
        x = get_ul(item)[0]
    elif h == 'r':
        x = get_lr(item)[0]
    else: # h == 'c'
        x = get_center(item)[0]
    return x, y

def length(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def shrink_to(newlength, x1, y1, x2, y2):
    distance = length(x1, y1, x2, y2)
    factor = 1 - (newlength / distance)
    x3 = x2*(1-factor) + x1*factor
    y3 = y2*(1-factor) + y1*factor
    return x3, y3

def ah_pos_circle(source, dest):
    '''Determine where the point of the arrowhead is when dest is a circle'''
    x1, y1 = get_center(source)
    x2, y2 = get_center(dest)
    r = dest['radius']
    distance = length(x1, y1, x2, y2)
    factor = r / distance
    x = x2*(1-factor) + x1*factor
    y = y2*(1-factor) + y1*factor
    # figure out new end for edge: assume thickness of 5 (eh)
    x3, y3 = shrink_to(distance - (r + 5), x1, y1, x2, y2)
    return x, y, x3, y3

def arrowhead_position(source, dest):
    # also include where the edge's line should terminate
    kind = dest['name']
    if kind == 'circle':
        return ah_pos_circle(source, dest)
    x1, y1 = get_center(source)
    # pick a port: ul, ml, ll, uc, mc, lc, ur, mr, lr
    port = find_nearest_port(dest, source)
    x2, y2 = get_port_pos(dest, port)
    distance = length(x1, y1, x2, y2)
    distance1 = distance - 5
    x3, y3 = shrink_to(distance1, x1, y1, x2, y2)
    return x2, y2, x3, y3


def make_arrowhead(edge, x1, y1, x2, y2, hx, hy, css_classes, end):
    # use the polygon template:
    ah_length, ah_width = 20, 20
    points_string = scale_points(ARROWHEAD_POINTS, ah_length, ah_width)
    rotation = get_angle(x1, y1, x2, y2)  # TODO: fix this so arrowheads are aligned with edge angle
    arrowhead = POLYGON_TEMPLATE % to_strings(hx, hy, rotation, get_id(edge)+end, 'arrowhead ' + css_classes, points_string, get_color(edge))
    return arrowhead

def make_edge(edge):
    color = get_color(edge)
    width = get_width(edge)
    source = get_start(edge)
    dest = get_end(edge)
    arrow = get_arrow(edge)
    x1, y1 = get_center(source)
    x2, y2 = get_center(dest)
    css_classes = get_class_str(edge)
    if arrow in ['head', 'both']:
        hx, hy, xe, ye = arrowhead_position(source, dest)
    else:
        xe, ye = x2, y2
    if arrow in ['tail', 'both']:
        tx, ty, xb, yb = arrowhead_position(dest, source) # note reversal!
    else:
        xb, yb = x1, y1
    line = LINE_TEMPLATE % to_strings(get_id(edge), css_classes, xb, yb, xe, ye, color, width)
    result = line
    if arrow in ['head', 'both']:
        result += '\n' + make_arrowhead(edge, x1, y1, x2, y2, hx, hy, css_classes, '-he')
    if arrow in ['tail', 'both']:
        result += '\n' + make_arrowhead(edge, x2, y2, x1, y1, tx, ty, css_classes, '-ta')
    return result

def make_diagram(diagram):
    context['diagram_width']  = diagram['width']
    context['diagram_height'] = diagram['height']
    if 'stylesheet' in diagram:
        context['css_href'] = diagram['stylesheet']
    if 'style' in diagram:
        context['style'] = diagram['style']

def get_style_fragment():
    if 'css_href' in context and context['css_href']:
        return STYLESHEET_TEMPLATE % entity_encode(context['css_href'])
    style = ''
    try:
        sfile = open('css/' + context['style'] + '.css')
        style = sfile.read()
        close(sfile)
    except:
        pass
    return STYLE_TEMPLATE % style

def get_angle(x1, y1, x2, y2):
    if x1 == x2:
        return math.copysign(90, y2 - y1)
    return math.atan2(y2 - y1, x2 - x1) * 180 / math.pi

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

lines0 = []

def main(args):
    global lines0
    filenameargs = [a for a in args if '=' not in a]
    lines0 = open_file(filenameargs + ['-']).readlines()
    lines0 = [line.rstrip('\r\n') for line in lines0]
    update_context(args)

    # keep the line numbers for error reporting:
    lines = zip(range(1, len(lines0)+1), lines0)
    # remove blank lines and comment lines (first non-whitespace char is #):
    lines = [line for line in lines if line[1].lstrip() and line[1].lstrip()[0] != '#']
    parsed = [parse(tokenize(line)) for line in lines]
    for nobj in parsed:
        obj = nobj[1]
        objects[obj['id']] = obj

    parsed.sort(key=get_z)
    svgobjects = [make_object(thing) for thing in parsed]
    svgobjects = [ob for ob in svgobjects if ob]
    # either it has an external stylesheet, or it specified a style (if both, stylesheet wins):
    print(SVG_TEMPLATE % (context['diagram_width'], context['diagram_height'], dash_encode('\n'.join(lines0)),
                          get_style_fragment(), '\n'.join(svgobjects)))

if __name__ == '__main__':
    main(sys.argv[1:])
