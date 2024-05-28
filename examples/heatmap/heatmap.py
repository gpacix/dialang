#!/bin/python3
import sys

colors = [ '#000', '#200', '#300', '#400', '#600', '#800', '#A00', '#C00', '#E00', '#F00']
colors = [ '#00F', '#44F', '#88F', '#CCF', '#FFF', '#FCC', '#F99', '#F66', '#F33', '#F00']
#colors = [ 'hsl(%ddeg,100%%,50%%)' % i for i in range(217, 0, -24)]

def main(args):
    WIDTH, HEIGHT, X, Y = 40, 40, 150, 180
    lines = sys.stdin.read().split('\n')
    # first lines is names, rest is data:
    names = lines[0].split(',') + ['']
    data = [line.split(',') for line in lines[1:]]
    print("diagram HeatMap width 800 height 600 style clean")
    print("rect title 'Heat Map of Interpersonal Communication' center 400 30 size 800 60 class c3")
    # names:
    for i in range(len(names)):
        if names[i]:
            print('rect rh%d "%s" center 100 %d size 100 %d class c%d'
                  % (i, names[i], Y + (i+1)*HEIGHT, HEIGHT, (i%2)+1))
    for i in range(len(names)):
        if names[i]:
            print('rect rv%d "%s" trotate -90 center %d %d size %d 100 class c%d'
                  % (i, names[i], X + (i+1)*WIDTH, Y - 50, WIDTH, (i%2)+1))

    for i in range(len(colors)):
        c = colors[(len(colors)-1)-i]
        print('rect leg%d "%d+" size %d %d center %d %d color %s' %
              (i, (9-i)*10, WIDTH, HEIGHT, 650, Y + (i+1) * HEIGHT, c))
    row = 0
    for record in data:
        from_name = names[row]
        row += 1
        col = 0
        for field in record:
            to_name = names[col]
            col += 1
            if field:
                val = int(field)
                #style = val % 7
                try:
                    color = colors[(val // 10)%10]
                except IndexError as ie:
                    print(ie)
                    sys.exit(1)
                rollover = ('%s → %s: %d' % (from_name, to_name, val))
                print('rect r%d-%d " " size %d %d center %d %d color %s rollover "%s"' %
                      (row, col, WIDTH, HEIGHT, col*WIDTH+X, row*HEIGHT+Y, color, rollover))

if __name__ == '__main__':
    main(sys.argv[1:])
