def change(money):
    # write your code here
    coins = 0
    coins += money // 10
    money = money % 10
    coins += money // 5
    money = money % 5
    coins += money
    return coins


if __name__ == '__main__':
    m = int(input())
    print(change(m))
