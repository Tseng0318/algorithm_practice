def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def maximum_value(dataset):
    digits = [int(dataset[i]) for i in range(0, len(dataset), 2)]
    ops    = [dataset[i] for i in range(1, len(dataset), 2)]
    n = len(digits)

    M = [[0] * n for _ in range(n)]   # max over range i..j
    m = [[0] * n for _ in range(n)]   # min over range i..j

    # base case: a single digit — its min and max are itself
    for i in range(n):
        M[i][i] = digits[i]
        m[i][i] = digits[i]

    # fill by increasing interval length
    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            j = i + length - 1

            best = float('-inf')
            worst = float('inf')

            for k in range(i, j):            # split between k and k+1
                op = ops[k]
                a = evaluate(M[i][k], M[k+1][j], op)
                b = evaluate(M[i][k], m[k+1][j], op)
                c = evaluate(m[i][k], M[k+1][j], op)
                d = evaluate(m[i][k], m[k+1][j], op)

                best  = max(best,  a, b, c, d)
                worst = min(worst, a, b, c, d)

            M[i][j] = best
            m[i][j] = worst

    return M[0][n-1]


if __name__ == "__main__":
    print(maximum_value(input()))
