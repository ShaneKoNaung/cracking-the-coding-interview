def urlify(string, n):
    add_this = "%20"
    string_list = list(string[:n])
    for i in range(len(string_list)):
        if string[i] == " ":
            string_list[i] = add_this
    string_updated = "".join(string_list)
    return string_updated


def testFun(s, n, ans):
    if urlify(s, n) == ans:
        print("Test passed.")
    else:
        print("Test failed.")


testFun("Mr John Smith    ", 13, "Mr%20John%20Smith")
testFun("Shane Ko Naung    ", 14, "Shane%20Ko%20Naung")
testFun("", 0, "")
testFun("   ", 1, "%20")
