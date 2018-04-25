def isPalinPermu(string):
    letters = {}
    string = string.replace(" ", "")
    str_len = len(string)
    # checking if the length of the string is even
    # if it is, there must be only pairs of characters
    if str_len % 2 == 0:
        # counting each character
        for i in string:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
        # checking if there is more than odd num char
        for i in letters.values():
            if i % 2 == 1:
                return False
        return True
    else:
        # counting each character
        for i in string:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
        count = 0
        for i in letters.values():
            if i % 2 == 1:
                count += 1
                if count > 1:
                    return False
        return True


def testFun(s, bool_val):
    if isPalinPermu(s) == bool_val:
        print("Test passed.")
    else:
        print("Test failed.")


testFun("catTtcaT", True)
testFun("catT tcaT", True)
testFun("baaba", True)
testFun("bcaaadddcb", False)
