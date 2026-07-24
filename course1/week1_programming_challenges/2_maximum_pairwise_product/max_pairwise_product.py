def max_pairwise_product(numbers):

    sort = sorted(numbers)
    max_num = sort[-1] * sort[-2]

    min_num = sort[0] * sort[1]

    return max(max_num, min_num)

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
