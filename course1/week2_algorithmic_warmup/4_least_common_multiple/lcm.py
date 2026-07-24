import math
def lcm(a, b):
    return (a*b)// math.gcd(a, b)



if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

