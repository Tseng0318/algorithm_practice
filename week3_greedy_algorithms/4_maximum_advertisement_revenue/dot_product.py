from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    
    # for permutation in permutations(second_sequence):
    #     dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
    #     max_product = max(max_product, dot_product)
    first_sequence.sort()
    second_sequence.sort()
    max_product = sum(x*y for x, y in zip(first_sequence, second_sequence))

    return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
