'''
You are given two 32-bit numbers, N and M, and two bit positions, i and
j. Write a method to insert M into N such that M starts at bit j and ends at
bit i. You can assume that the bits j through i have enough space to fit all of
M. That is, if M = 10011, you can assume that there are at least 5 bits between
j and i. You would not, for example, have j = 3 and i = 2, because M could not
fully fit between bit 3 and bit 2.
'''


def insertion(M, N, i, j):
    output = N
    m_position = 0
    for n in range(i, j + 1):
        bit = get_bit(M, m_position)  # get the bit from N starting from 0
        output = update_bit(output, n, bit)
        m_position += 1

    return output


def get_bit(x, position):
    mask = 1 << position
    return x & mask != 0


def update_bit(x, position, val):
    mask = val << position
    return x + mask
