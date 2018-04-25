'''
Assumeyou have a method isSubstringwhich checks if one word is a substring of
another. Given two strings, sl and s2, write code to check if s2 is a rotation
of sl using only one call to isSubstring
(e.g., "waterbottle" is a rotation of"erbottlewat").
'''


# check if w1 is the substring of w2
def isSubstring(w1, w2):
    if w1 in w2:
        return True
    return False


def isRotation(str1, str2):
    pivot = 0
    if len(str1) != len(str2):
        return False
    else:
        for i in range(len(str1)):
            if str1[i] == str2[0]:
                pivot = i
                break
        if isSubstring(str1[pivot:], str2):
            if str1[0:pivot] == str2[len(str1[pivot:]):]:
                return True
        return False


def isRotation_2(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        return isSubstring(s2, s1s1)
    return False


def testFun(s1, s2, bool_val):
    if isRotation(s1, s2) == bool_val:
        print("Test passed.")
    else:
        print("Test failed.")
    if isRotation_2(s1, s2) == bool_val:
        print("Test passed.")
    else:
        print("Test failed.")


testFun("waterbottle", "erbottlewat", True)
testFun("lbeardk", "beardkl", True)
testFun("abcdef", "cdefba", False)
