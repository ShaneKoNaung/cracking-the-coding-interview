# function to check if the two string is one or two edit away to be the same
def oneaway(str1, str2):
    if len(str1) == len(str2):
        return oneReplaceAway(str1, str2)
    elif len(str1) + 1 == len(str2):
        return oneEditAway(str1, str2)
    elif len(str2) + 1 == len(str1):
        return oneEditAway(str2, str1)
    return False


# check if the two strings are one replace away to be the same
def oneReplaceAway(str1, str2):
    replacement = 0  # keep track of replacements
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            replacement += 1  # increment the replacement
            if replacement > 1:
                return False
    return True


# check if the two strings are one edit(insert or remove) away to be the same
def oneEditAway(str1, str2):
    for i in range(len(str1)):
        if str1[i] not in str2:
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
