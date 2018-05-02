'''
Implement an algorithm to find the kth to last element of a singly linked list.
'''
from linked_list import LinkedList


def kthToLast(n, k):
    '''
    input: Singly Linked List n
    return the kth element to the last element
    '''
    current = n.get_head()
    runner = n.get_head()

    for i in range(k):
        if runner is None:
            return None
        runner = runner.get_next()

    while runner is not None:
        current = current.get_next()
        runner = runner.get_next()
    return current.get_data()


def printLinkedList(n):
    current = n.get_head()
    while current is not None:
        print(current.get_data(), end=" ")
        current = current.get_next()
    print()


def main():
    n = LinkedList()
    for i in range(10):
        n.push_back(i)
    printLinkedList(n)
    result = kthToLast(n, 3)
    print(result)


if __name__ == "__main__":
    main()
