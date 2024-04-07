#!/usr/bin/python3

INPUT='''
color blue
rect A "Starting Point" center 100 100 size 100 50
rrect B "Ending Point" ul 300 300 size 100 150 color green
edge E from A lr to B
'''

color = None
edge_color = None
node_color = None

def main(args):
    # for now, just ignore the args and use our hard-coded input:
    lines = INPUT.split('\n')
    # remove blank lines and comment lines (first non-whitespace char is #):
    lines = [line for line in lines if line.lstrip() and line.lstrip()[0] != '#']
    print(lines)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
