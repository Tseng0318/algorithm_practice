from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    # 1. pair up (value/weight ratio, weight, value) for each item
    items = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True)
    # 2. sort by ratio descending
    # 3. walk items: if it fits, take it all; otherwise take the fraction that fits and break
    value = 0.0
    for v, w in items:
        if w <= capacity:
            # whole item fits — take it all # [(100, 20), (120, 50), (60, 30)]
            value += v
            capacity -= w
        else:
            # only a fraction fits — take that fraction, then stop
            value += (v/w) * capacity
            capacity -= capacity
            break
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
