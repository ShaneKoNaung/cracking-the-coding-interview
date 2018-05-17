'''
You have an integer and you can flip exactly one bit from a 0 to a 1. Write
code to find the length of the longest sequence of 1s you could create.
'''


def flipBitToWin(num):
    '''
    num is an integer
    return the length of the longest sequence of 1s by fliping one 0 to 1.
    '''
    binary = bin(num)
    count_ones = 0
    max_len = 0
    is_zero = False
    i = 0
    if num == 0:
        return 0
    while i < len(binary) - 2:
        if is_bit_set(num, i):
            count_ones += 1
        else:
            if is_zero is False:
                count_ones += 1
                is_zero = True
                j = i + 1
            elif count_ones >= max_len:
                max_len = count_ones
                count_ones = 0
                is_zero = False
                i = j - 1
        i += 1
    return max(count_ones, max_len)


def is_bit_set(x, position):
    mask = x >> position
    return 1 & mask
