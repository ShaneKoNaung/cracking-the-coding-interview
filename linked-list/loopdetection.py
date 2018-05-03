'''
Given a circular linked list, implement an algorithm that returns the node at
the beginning of the loop.
'''
from linked_list import LinkedList
from node import Node


def circular_start(n):
    '''
    input: circular linked-list
    returns the beginning of the node
    '''
    adict = {}  # to store nodes
    current = n.get_head()
    while current is not None:
        # if current node is already in the check_list
        if current in adict:
            return current
        adict[current] = 1
        current = current.get_next()
    return "Are you sure that this is a circular linked list?"


def contain(n, ll):
    current = ll.get_head()
    while current is not None:
        if current == n:
            return n
        current = current.get_next()
    return False


def printLinkedList(n):
    current = n.get_head()
    while current is not None:
        print(current.get_data(), end="")
        current = current.get_next()
        if current is None:
            print()
        else:
            print(" -> ", end="")


def main():
    n = LinkedList()
    node1 = Node(0)
    n._head = node1
    n._tail = node1
    for i in range(1, 5):
        node = Node(i)
        n._tail.set_next(node)
        n._tail = node
    printLinkedList(n)
    print(circular_start(n))
    circular_node = Node(5)
    n._tail.set_next(circular_node)
    n._tail = circular_node
    for i in range(6, 10):
        node = Node(i)
        n._tail.set_next(node)
        n._tail = node
    n._tail.set_next(circular_node)
    n._tail = circular_node
    print(circular_start(n))


if __name__ == "__main__":
    main()
