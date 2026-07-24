def optimal_summands(n):
    summands = []
    k = 1                    # the next candidate summand
    remaining = n            # how much of n is left to distribute
    
    while remaining > 0:
        # Can I safely take k as a distinct summand AND still have room
        # for a strictly larger one next time?
        # That's true when (remaining - k) > k, i.e. remaining > 2*k.
        if remaining>2*k:
            # safe: take k, reduce remaining, move to next candidate
            summands.append(k)
            remaining -= k
            k += 1
        else:
            # not safe: dump ALL of remaining into one final summand and stop
            summands.append(remaining)
            remaining = 0       # set to 0 to end the loop
    
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
