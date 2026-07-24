from itertools import combinations


def count_inversions(a):
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    left,  left_inv  = count_inversions(a[:mid])      # LINE A
    right, right_inv = count_inversions(a[mid:])      # LINE B
    merged, split_inv = merge_and_count(left, right)  # LINE C
    return merged, left_inv + right_inv + split_inv

def merge_and_count(left, right):
    merged = []
    i = j = 0
    inversions = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
            inversions += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    _, ans = count_inversions(elements)
    print(ans)
