'''
Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
'''
from linked_list import LinkedList


def partition(n, x):
    current = n.get_head()
    partition_list = LinkedList()
    while current is not None:
        if current.get_data() < x:
            partition_list.push_front(current.get_data())
        else:
            partition_list.push_back(current.get_data())
        current = current.get_next()
    return partition_list


def printLinkedList(n):
    current = n.get_head()
    while current is not None:
        print(current.get_data(), end=" ")
        current = current.get_next()
    print()


def main():
    n = LinkedList()
    n.push_back(3)
    n.push_back(5)
    n.push_back(8)
    n.push_back(5)
    n.push_back(10)
    n.push_back(2)
    n.push_back(1)
    printLinkedList(n)
    printLinkedList(partition(n, 5))


if __name__ == "__main__":
    main()
