import math

def gcd(a, b):

    return math.gcd(a, b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
