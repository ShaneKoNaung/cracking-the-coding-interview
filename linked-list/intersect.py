'''
Given two (singly) linked lists, determine if the two lists intersect. Return
the inter­secting node. Note that the intersection is defined based on reference
not value. That is, if the kth node of the first linked list is the exact same
node (by reference) as the jth node of the second linked list, then they are
intersecting.
'''
from linked_list import LinkedList
from node import Node


def intersect(l1, l2):
    '''
    two singly linked lists
    return true if one node is in both lists
    '''
    current = l1.get_head()
    while current is not None:
        node = contain(current, l2)
        if node:
            return node
        current = current.get_next()
    return False


def contain(node, ll):
    '''
    inputs: a node and a linked-list
    return True if the node is in the list
    '''
    current = ll.get_head()
    while current is not None:
        if current == node:
            return node
        current = current.get_next()
    return False


def printLinkedList(n):
    '''
    print the elements of the linked_list
    '''
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
    for i in range(2, 11):
        node = Node(i)
        n.push_back(node)
    m = LinkedList()
    for i in range(10, 20):
        node = Node(i)
        m.push_back(node)

    # without the intersection
    print(intersect(n, m))

    node = Node(20)
    n.get_tail().set_next(node)
    m.get_tail().set_next(node)

    # with the intersection
    printLinkedList(m)
    print(intersect(n, m))


if __name__ == "__main__":
    main()
