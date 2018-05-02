from linked_list import LinkedList


def sumList(l1, l2):
    if len(l1) > len(l2):
        return addList(l1, l2)
    else:
        return addList(l2, l1)


def addList(l1, l2):
    result_list = LinkedList()
    carry = 0
    num1 = l1.get_head()
    num2 = l2.get_head()
    for i in range(len(l1)):
        if num2 is None:
            result_list.push_back(num1.get_data() + carry)
        else:
            result = num1.get_data() + num2.get_data() + carry
            carry = result // 10
            result = result % 10
            result_list.push_back(result)
            num1 = num1.get_next()
            num2 = num2.get_next()
    return result_list


def printLinkedList(n):
    current = n.get_head()
    while current is not None:
        print(current.get_data(), end=" ")
        current = current.get_next()
    print()


def main():
    n1 = LinkedList()
    n2 = LinkedList()
    n1.push_back(7)
    n1.push_back(1)
    n1.push_back(6)
    n2.push_back(5)
    n2.push_back(9)
    printLinkedList(n1)
    printLinkedList(n2)
    result = sumList(n1, n2)

    printLinkedList(result)


if __name__ == "__main__":
    main()
