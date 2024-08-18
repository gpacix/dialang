#!/usr/bin/python3
import sys
import math

def open_file(args):
    if args[0] != '-':
        return open(args[0])
    return sys.stdin

def err(*args):
    print(*args, file=sys.stderr)

DEBUG=False
def debug(*args):
    if DEBUG:
        print('DEBUG:', *args, file=sys.stderr)

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

class GridLayout:
    def __init__(self, lines):
        debug('%s' % lines) ##DEBUG
        line = lines[0]
        lines = lines[1:]
        if not line.strip().startswith('layout grid'):
            err('error: unknown layout: %s' % line)
            return None
        self.dimensions = list(map(to_number, line[11:].strip().split()))
        self.width, self.height, self.xspace, self.yspace = self.dimensions
        debug("%s" % self.dimensions) ##DEBUG
        d = {}
        row = 0
        lines = [ line for line in lines if not line or line[0] != '#' ]
        for line in lines:
            col = 0
            for c in line:
                if c != ' ':
                    d[c] = (col, row) # x, y
                col += 1
            row += 1
        self.positions = [d[k] for k in sorted(d.keys())]
        debug(self.positions) ##DEBUG

    def transform(self, line):
        # TODO: error message if no remaining positions
        pos, self.positions = self.positions[0], self.positions[1:]
        # figure out position, size
        ulx = (self.width  + self.xspace) * pos[0] + self.xspace
        uly = (self.height + self.yspace) * pos[1] + self.yspace
        return "%s ul %s %s size %s %s" % to_strings(line, ulx, uly, self.width, self.height)

    def has_more(self):
        return len(self.positions) > 0


def parse_layout(inlines):
    layoutlines = []
    line, inlines = inlines[0], inlines[1:]
    layoutlines.append(line)
    while inlines and inlines[0].strip() != "endlayout":
        line, inlines = inlines[0], inlines[1:]
        layoutlines.append(line)
    return GridLayout(layoutlines), inlines[1:]

def apply_layout(line, layout):
    if not layout or not layout.has_more():
        return line
    ls = line.strip()
    if not ls:
        return line
    if ls.startswith('#') or ls.startswith('edge ') or ls.startswith('color '):
        return line
    if ' size ' in line or ' radius ' in line:
        return line
    return layout.transform(line)

def main(args):
    global DEBUG
    filenameargs = [a for a in args if '=' not in a]
    settings = [a for a in args if '=' in a]
    for s in settings:
        if s.upper() == 'DEBUG=1':
            DEBUG = True

    inlines = open_file(filenameargs + ['-']).readlines()
    inlines = [line.rstrip('\r\n') for line in inlines]
    layout = None
    lines = []
    while inlines:
        line = inlines[0]
        if line.lstrip().startswith('layout grid'):
            layout, inlines = parse_layout(inlines)
        else:
            lines.append(apply_layout(line, layout))
            inlines = inlines[1:]
    for line in lines:
        print(line)

if __name__ == '__main__':
    main(sys.argv[1:])
