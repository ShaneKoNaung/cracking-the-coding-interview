'''
Given a real number between O and 1 (e.g., 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately
in binary with at most 32 characters, print "ERROR:'
'''


def binaryToString(num):
    '''
    num is a real number between 0 and 1.
    print the binary representation of num
    if the length of the representation is greater than 32, print "ERROR"
    '''
    # if the number is less than 0 or greater than 1
    if num < 0 or num > 1:
        print("ERROR")
        return 0
    r = num
    str_out = "."
    while num > 0:
        if len(str_out) > 32:
            print("ERROR")
            return 0
        else:
            r = 2 * num
            if r >= 1:
                str_out += '1'
                num = r - 1
            else:
                str_out += '0'
                num = r
    print(str_out)
