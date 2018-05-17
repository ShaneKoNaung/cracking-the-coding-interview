'''
Write a function to determine the number of bits you would need to flip to
convert integer A to integer B.
'''


def conversion(a, b):
    answer = a ^ b
    numberOfOnes = count_1s(answer)
    return numberOfOnes


def count_1s(num):
    count = 0
    while num > 0:
        num &= num - 1
        count += 1
    return count
