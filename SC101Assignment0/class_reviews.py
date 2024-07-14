"""
File: class_reviews.py
Name: HUANGIHC
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = -1  # Sentinel number


def main():
    """
    TODO: class review for SC001 or SC101
    """
    cat_org = str(input('Which class? ')).upper()  # the first category for data
    # print(str(cat_org))  # check cat

    data_org = int(input('Score: '))  # the first data
    n0 = 0
    n1 = 0
    max0 = max1 = -float('inf')  # Initialize with negative infinity
    min0 = min1 = float('inf')  # Initialize with positive infinity
    tot0 = tot1 = 0
    avg0 = avg1 = None
    print(max0)

    if data_org == EXIT:
        print('No class scores were entered')
    if cat_org == 'SC001':  # 判斷第一次的data是哪個分類
        n0 = 1
        data0 = data_org
        min0 = data0
        max0 = data0
        tot0 = data0
    elif cat_org == 'SC101':
        n1 = 1
        data1 = data_org
        min1 = data1
        max1 = data1
        tot1 = data1

    while True:
        cat = str(input('Which class? ')).upper()
        data = int(input('Score: '))

        if data == EXIT:
            break
        elif cat == "SC001":
            n0 += 1

            if data > max0:
                max0 = data
            if data < min0:
                min0 = data
            if data != EXIT:

                tot0 = tot0 + data
                avg0 = tot0 / n0

        elif cat == "SC101":
            n1 += 1

            if data > max1:
                max1 = data
            if data < min1:
                min1 = data
            if data != EXIT:
                tot1 = tot1 + data
                avg1 = tot1 / n1

    print('=============SC001==============')
    if n0 == 0:
        print('No score for SC001')
    else:
        print('Max (001): ' + str(max0))
        print('Min (001): ' + str(min0))
        print('Avg (001): ' + str(avg0))

    print('=============SC101==============')
    if n1 == 0:
        print('No score for SC101')
    else:
        print('Max (101): ' + str(max1))
        print('Min (101): ' + str(min1))
        print('Avg (101): ' + str(avg1))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
