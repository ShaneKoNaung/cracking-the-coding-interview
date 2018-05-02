''' is this linked-list palindrome '''
from linked_list import LinkedList


def isPalin(n):
    a = clone(n)
    return isPalin2(a)


def isPalin2(n):
    # if the front and end element are not equal
    if n.get_head().get_data() != n.get_tail().get_data():
        return False
    # the elements are equal and length is less than 3
    if len(n) == 2 or len(n) == 1:
        return True
    else:
        # remove the first and end elements
        n.pop_front()
        n.pop_back()
        return isPalin2(n)


# clone the linked-list
def clone(n):
    a = LinkedList()
    current = n.get_head()
    while current is not None:
        a.push_back(current.get_data())
        current = current.get_next()
    return a


def printLinkedList(n):
    current = n.get_head()
    while current is not None:
        print(current.get_data(), end=" ")
        current = current.get_next()
    print()


def main():
    n = LinkedList()
    n.push_front("a")
    n.push_front("b")
    n.push_front("c")
    n.push_front("b")
    n.push_front("a")
    printLinkedList(n)
    print(isPalin(n))


if __name__ == "__main__":
    main()
