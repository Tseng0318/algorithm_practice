def binary_search(keys, query):
    # write your code here
    left = 0
    right = len(keys) - 1
    result = -1                  # best (leftmost) match found so far
    
    while left <= right:
        mid = (left + right) // 2
        if keys[mid] == query:
            # found a match — but is there an earlier one?
            result = mid          # record this index as a candidate
            right = mid - 1            # keep searching to the LEFT
        elif keys[mid] < query:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
