'''
Given a positive integer, print the next smallest and the next largest number
that have the same number of 1 bits in their binary representation.
'''


def nextNumberBrute(num):
    numberOfOnes = get_1s(num)
    print(get_nextSmall(num, numberOfOnes))
    print(get_nextLarge(num, numberOfOnes))


def get_nextLarge(num, numberOfOnes):
    num += 1
    while get_1s(num) != numberOfOnes:
        num += 1
    return num


def get_nextSmall(num, numberOfOnes):
    num -= 1
    while get_1s(num) != numberOfOnes:
        num -= 1
    return num


def get_1s(num):
    count = 0
    while num > 0:
        num &= num - 1
        count += 1
    return count


nextNumberBrute(11)
