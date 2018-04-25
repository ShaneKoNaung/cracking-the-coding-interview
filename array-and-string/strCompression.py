# function to do basic basic string compression. eg. aabbbcccaa -> a2b3c3a2
def compress(str1):
    alpha = str1[0]
    count = 0
    alist = []
    for i in range(len(str1)):
        if str1[i] != alpha:
            alist.append(alpha)
            alist.append(str(count))
            alpha = str1[i]
            count = 1
        else:
            count += 1
    alist.append(alpha)
    alist.append(str(count))
    compressed_string = "".join(alist)
    if len(compressed_string) < len(str1):
        return compressed_string
    else:
        return str1


def testFun(s, result):
    if compress(s) == result:
        print("Test passed.")
    else:
        print("Test failed.")


testFun("aaabbbcccddd", "a3b3c3d3")
testFun("aabbccdde", "aabbccdde")
testFun("zzzzzzbbba", "z6b3a1")
testFun(" ", " ")
testFun("123456", "123456")
testFun("111122333", "142233")
