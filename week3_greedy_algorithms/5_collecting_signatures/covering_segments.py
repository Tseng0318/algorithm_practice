from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    
    # 1. sort segments by their END point
    segments = sorted(segments, key=lambda x: x[1])
    
    # track the most recently placed dot; start below any possible coordinate
    last_point = float('-inf')
    
    for s in segments:
        # 2. is this segment NOT yet covered by last_point?
        #    (it's uncovered when the segment starts strictly after the dot)
        if s[0]>last_point:
            # 3. need a new dot — place it at the segment's END for max reach
            points.append(s[1])
            # 4. update last_point to the dot you just placed
            last_point = s[1]
    
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
