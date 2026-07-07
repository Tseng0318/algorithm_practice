def majority_element_naive(elements):
    # Pass 1: find the candidate
    candidate = None
    count = 0
    for e in elements:
        if count == 0:
            candidate = e
        if e == candidate:
            count += 1
        else:
            count -= 1
    
    # Pass 2: verify it's actually a majority
    if elements.count(candidate) > len(elements) / 2:
        return 1
    return 0
# [3, 2, 9, 2, 2]

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
