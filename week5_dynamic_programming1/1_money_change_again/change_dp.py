def change(money):
    coins = [1, 3, 4]
    
    # min_coins[m] = fewest coins needed to make amount m
    min_coins = [0] * (money + 1)      # min_coins[0] = 0 (zero coins make zero)
    
    for m in range(1, money + 1):
        min_coins[m] = float('inf')    # start pessimistic
        for c in coins:
            if m >= c:                 # can we actually use coin c?
                # what's the cost of using c, then optimally making (m - c)?
                candidate = 1+min_coins[m-c]
                # keep the best option seen so far
                if candidate < min_coins[m]:
                    min_coins[m] = candidate
    
    return min_coins[money]

if __name__ == '__main__':
    m = int(input())
    print(change(m))
