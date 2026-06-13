def fibonacci_huge_naive(n, m):
    # Phase 1: find the Pisano period π(m)
    #   - walk F(k) mod m starting from 0, 1
    #   - count steps until the pair (previous, current) returns to (0, 1)
    #   - that count is the period
    previous, current = 0 ,1
    period = 0
    while True:
        previous, current = current, (previous + current)%m
        period += 1
        if previous==0 and current==1:
            break



    # Phase 2: reduce the index and compute
    #   - n = n % period
    #   - run your last-digit-style loop (with % m) that many times
    #   - return the result
    previous, current = 0, 1
    n = n % period
    if n <= 1:
       return n
    
    for _ in range(n-1):
        previous, current = current, (previous + current)%m
    
    return current


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
