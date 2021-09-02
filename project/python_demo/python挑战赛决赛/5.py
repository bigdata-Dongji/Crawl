#!/usr/bin/python
#-*- coding:utf-8 -*-



#source code demo
def main():

    N = int(input())
    D = []
    price = 0
    money = 0
    if N <= 1000:
        price = float(input())
        numbers = [num for num in input().split(" ", N - 1)]
        result = ''.join(numbers)
        list1 = []
        for each in result:
            if each not in list1:
                if each == '\n':
                    print('\\n', result.count(each))
                else:
                    D.append(result.count(each))
                list1.append(each)

    for i in range(len(D) + 1):
        if len(D) == 4 and not (0 in D):
            mins = min(D)
            money = mins * price * 0.5 * 4
            D = [i - mins for i in D]
            D = list(filter(lambda number: number > 0, D))
            continue

        if sum(D) % 2 == 0:
            D = list(filter(lambda number: number > 0, D))
            money = sum(D) * price * 0.8+money
            break
        else:
            if len(D) == 3 and not (0 in D):
                mins = min(D)
                money = mins * price * 0.8 * 3 + money
                D = [i - mins for i in D]
                D = list(filter(lambda number: number > 0, D))
                continue

            if len(D) == 2 and not (0 in D):
                mins = min(D)
                money = mins * price * 0.8 * 2 + money
                D = [i - mins for i in D]
                D = list(filter(lambda number: number > 0, D))
                continue

            if len(D) == 1 and not (0 in D):
                mins = min(D)
                money = 1 * price + money
                D = list(filter(lambda number: number > 0, D))
                D = [i - mins for i in D]
                continue

    print(money)
if __name__ == '__main__':
    main()