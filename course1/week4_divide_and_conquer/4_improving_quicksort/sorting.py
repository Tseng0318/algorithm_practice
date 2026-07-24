from random import randint


def partition3(array, left, right):
    # write your code here
    pivot = array[left]        # pivot was pre-swapped here by the caller
    
    lt = left                  # array[left..lt-1]  <  pivot
    gt = right                 # array[gt+1..right]  >  pivot
    i = left                   # current element under inspection
    
    while i <= gt:
        if array[i] < pivot:
            # element belongs in the LEFT region
            # swap it down to lt, advance both lt and i
            array[i], array[lt] = array[lt], array[i]
            lt += 1
            i += 1
        elif array[i] > pivot:
            # element belongs in the RIGHT region
            # swap it up to gt, advance gt DOWN — but do NOT advance i
            array[i], array[gt] = array[gt], array[i]
            gt -= 1
            # (i stays — the swapped-in element is unexamined)
        else:
            # element EQUALS pivot — it's already in the middle region
            # just move on
            i += 1
    
    return lt, gt

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
