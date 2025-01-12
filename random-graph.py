#!/usr/bin/python3
import math
import random
random.seed(0)

N = 30
C = .2
R = 10*N

def main(args):
    SIZE = R*2.2
    print("diagram random_graph width %d height %d" % (SIZE, SIZE))
    print("color #80C0FF")
    for i in range(N):
        f = (1 + i%2)/2.0 #random.randint(1,2)/2.0
        x = math.cos(i*(2*math.pi)/N)*R*f + R
        y = math.sin(i*(2*math.pi)/N)*R*f + R
        print("rect ID%d ul %f %f size 30 20" % (i, x, y))
    for i in range(int(N*N*C)):
        print("edge E%d color black width 1 from ID%d to ID%d" % (i, random.randint(0,N-1), random.randint(0,N-1), ))

if __name__ == '__main__':
    import sys
    main(sys.argv)
