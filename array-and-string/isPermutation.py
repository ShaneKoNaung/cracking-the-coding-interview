def isPermutation(str1, str2):
    return sorted(str1) == sorted(str2)


def isPermutation_2(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        letters = [0 for i in range(128)]
        str1_array = list(str1)
        for i in str1_array:
            letters[ord(i)] += 1
        for i in str2:
            letters[ord(i)] -= 1
            if letters[ord(i)] < 0:
                return False
        return True


def test(str1, str2, bool_value):
    if isPermutation(str1, str2) == bool_value:
        print("test passed.")
    else:
        print("test failed.")
    if isPermutation_2(str1, str2) == bool_value:
        print("test passed.")
    else:
        print("test failed.")


test("abcdef", "abcefd", True)
test("abc$01", "10$abc", True)
test("", "", True)
test("", "abc", False)
test("ajf;f", "eafhf", False)
