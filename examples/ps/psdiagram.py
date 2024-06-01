#!/bin/python3
import sys
import math

#colors = [ '#000', '#200', '#300', '#400', '#600', '#800', '#A00', '#C00', '#E00', '#F00']
#colors = [ '#00F', '#44F', '#88F', '#CCF', '#FFF', '#FCC', '#F99', '#F66', '#F33', '#F00']
#colors = [ 'hsl(%ddeg,100%%,50%%)' % i for i in range(217, 0, -24)]
colors = [ 'hsl(%ddeg,70%%,45%%)' % i for i in range(0, 360, 60)]

def main(args):
    lines = sys.stdin.read().split('\n')
    # BSD/Mac syntax for input:
    # top -n 10 -l 2 -ncols 1000 -o cpu -stats cpu,command | tac | grep -m1 -B12 "^%" | python psdiagram.py
    parts = [ line.split(' ', 1) for line in lines ]
    pairs = [ (float(p[0]), p[1].strip()) for p in parts if len(p) == 2 ]
    print("diagram top_diagram size auto style clean")
    i = 0
    y = 50
    x = 100
    LC = len(colors)
    pairs.reverse()
    for p in pairs:
        i += 1
        # 'rect r%d "%s" ul %f %f size %f 50 class c%d'
        # TODO: why doesn't 'text-color white' work?
        v = 50*math.sqrt(p[0])
        #color = colors[i%len(colors)]
        color = colors[(i + (2)*(i%2)) % LC]
        print('rect r%d "%s" ul %f %f size %f %f color %s' %
              (i, p[1], x, y, v, v, color))
        y += v

if __name__ == '__main__':
    main(sys.argv[1:])
