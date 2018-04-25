'''
Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
'''


def isUnique(str):
    char = {}
    if str == " ":
        return True
    for i in range(len(str)):
        if str[i] in char:
            return False
        else:
            char[str[i]] = 1
    return True


def testFun(s, bool_val):
    if isUnique(s) == bool_val:
        print("Test passed.")
    else:
        print("Test failed.")


testFun("string", True)
testFun("abcdefghijklmnopqrstuvwxyz", True)
testFun(" ", True)
testFun("aabcd", False)
testFun("abcdeff", False)
