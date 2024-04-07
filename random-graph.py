#!/usr/bin/python3
import math
import random
random.seed(0)

N = 30
C = .2
R = 10*N

def main(args):
    print("color #80C0FF")
    for i in range(N):
        x = (math.cos(i*(2*math.pi)/N) + 1)*R
        y = (math.sin(i*(2*math.pi)/N) + 1)*R
        print("rect ID%d ul %f %f size 30 20" % (i, x, y))
    for i in range(int(N*N*C)):
        print("edge color black width .1 from ID%d to ID%d" % (random.randint(0,N-1), random.randint(0,N-1), ))

if __name__ == '__main__':
    import sys
    main(sys.argv)
