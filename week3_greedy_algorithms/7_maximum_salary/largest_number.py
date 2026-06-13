from itertools import permutations
from functools import cmp_to_key

def compare(a, b):
    # you want a first when a+b is the bigger gluing
    if a + b > b + a:
        return -1      # a should come first → which sign?
    elif a + b < b + a:
        return 1     # b should come first → which sign?
    else:
        return 0


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    # after sorting, join them
    result = "".join(numbers)
    # edge case: if the biggest digit is 0, the whole thing is 0
    if result[0] == "0":                       # all-zeros edge case
        return "0"
    return result

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
