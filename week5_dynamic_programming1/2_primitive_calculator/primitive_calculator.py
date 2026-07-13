def compute_operations(n):
    min_ops = [0] * (n + 1)
    parent  = [0] * (n + 1)
    min_ops[1] = 0

    for m in range(2, n + 1):
        best = min_ops[m - 1] + 1      # the always-available +1 option
        prev = m - 1

        if m % 2 == 0 and min_ops[m // 2] + 1 < best:
            best = min_ops[m // 2] + 1
            prev = m // 2

        if m % 3 == 0 and min_ops[m // 3] + 1  < best:    # is coming from m//3 better?
            best = min_ops[m // 3] + 1
            prev = m//3

        min_ops[m] = best
        parent[m]  = prev

    sequence = []
    m = n
    while m >= 1:
        sequence.append(m)
        if m == 1:
            break
        m = parent[m]
    sequence.reverse()
    return sequence


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
