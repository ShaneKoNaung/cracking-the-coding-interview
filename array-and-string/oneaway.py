# function to check if the two string is one or two edit away to be the same
def oneaway(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    changes = 0
    if str1 == str2:
        return True
    if abs(len1 - len2) > 1:
        return False
    else:
        if len1 == len2:
            for i in range(len1):
                if str1[i] != str2[i]:
                    changes += 1
            if changes > 1:
                return False
            else:
                return True
        else:
            if len1 < len2:
                for i in range(len1):
                    if str1[i] not in str2:
                        return False
            else:
                for i in range(len2):
                    if str2[i] not in str2:
                        return False
            return True


def testFun(str1, str2, bool_val):
    if oneaway(str1, str2) == bool_val:
        print("Test passed.")
    else:
        print("Test failed.")


testFun("pale", "ple", True)
testFun('pales', 'pale', True)
testFun('pale', 'bale', True)
testFun("pale", "bake", False)
