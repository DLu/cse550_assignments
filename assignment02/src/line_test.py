#!/usr/bin/python

from assignment02.geometry import bresenham

correct = 0
total = 0

def draw(x0,y0,x1,y1,points):
    dx = abs(x0-x1)
    dy = abs(y0-y1)
    mx = min(x0,x1)
    my = max(y0,y1)
    mmy = min(y0,y1)

    P = []
    for y in range(dy+1):
        P.append(['.']*(dx+1))
    for x,y in points:
        P[(my-y)][x-mx] = '*'    
    return P
                

def test(x0, y0, x1, y1, points):
    global correct, total
    test_points = bresenham(x0, y0, x1, y1)
    if test_points == points:
        correct += 1
    else:
        print "Failed Test: (%d, %d) to (%d, %d)"%(x0,y0,x1,y1)
        print "\tExpected:", points
        print "\tReceived:", test_points
        for s1,s2 in zip(draw(x0,y0,x1,y1,points),draw(x0,y0,x1,y1,test_points)):
            print '\t', ''.join(s1), ''.join(s2)
        
    total += 1
    
test(0,0,5,5,[(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5)])
test(0,0,5,0,[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0)])
test(0,0,0,5,[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5)])
test(0,0,10,5,[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (4, 2), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (8, 4), (9, 4), (9, 5), (10, 5)])
test(0,0,-10,5,[(0, 0), (-1, 0), (-1, 1), (-2, 1), (-3, 1), (-3, 2), (-4, 2), (-5, 2), (-5, 3), (-6, 3), (-7, 3), (-7, 4), (-8, 4), (-9, 4), (-9, 5), (-10, 5)])
test(0,0,-10,-5,[(0, 0), (-1, 0), (-1, -1), (-2, -1), (-3, -1), (-3, -2), (-4, -2), (-5, -2), (-5, -3), (-6, -3), (-7, -3), (-7, -4), (-8, -4), (-9, -4), (-9, -5), (-10, -5)])
test(0,0,10,-5, [(0, 0), (1, 0), (1, -1), (2, -1), (3, -1), (3, -2), (4, -2), (5, -2), (5, -3), (6, -3), (7, -3), (7, -4), (8, -4), (9, -4), (9, -5), (10, -5)])
test(-3,-5,5,3,[(-3, -5), (-2, -5), (-2, -4), (-1, -4), (-1, -3), (0, -3), (0, -2), (1, -2), (1, -1), (2, -1), (2, 0), (3, 0), (3, 1), (4, 1), (4, 2), (5, 2), (5, 3)])
test(-3,5,5,-3,[(-3, 5), (-2, 5), (-2, 4), (-1, 4), (-1, 3), (0, 3), (0, 2), (1, 2), (1, 1), (2, 1), (2, 0), (3, 0), (3, -1), (4, -1), (4, -2), (5, -2), (5, -3)])

print "Passed %d/%d"%(correct, total)
