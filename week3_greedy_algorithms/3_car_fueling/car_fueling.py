from sys import stdin


def min_refills(distance, tank, stops):
    # treat destination as the final point in the journey
    stops = stops + [distance]
    
    refills = 0
    position = 0     # where you currently are
    i = 0            # index of the next stop to consider
    n = len(stops)
    # Example: distance = 950, tank = 400, stops = [200, 375, 550, 750]
    while position < distance:
        # 1. Remember where i started this iteration (for the "did we advance?" check)
        last_reachable = i
        
        # 2. Advance i forward as long as stops[i] is reachable from position.
        #    "Reachable" means the distance from position to stops[i] is at most `tank`.
        while i<n and stops[i] - position <= tank:
            i += 1
        
        # 3. If i never advanced, you couldn't reach any station from here.
        #    What do you return?
        if i== last_reachable:
            return -1
        
        # 4. Jump to the farthest station you could reach.
        #    Which index is that? (Hint: i is now one past the last reachable.)
        position = stops[i - 1]
        
        # 5. If that "station" was actually the destination, you're done.
        #    Should this count as a refill?
        if position == distance:
            break
        
        # 6. Otherwise this was a real refill.
        refills += 1
    
    return refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
