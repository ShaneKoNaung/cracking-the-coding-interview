'''
Write code to remove duplicates from an unsorted linked list.
'''
from linked_list import LinkedList


def removeDups(n):
    '''
    n is the doubly linked list
    remove duplicates from n
    '''
    node_dict = {}
    current = n.get_head()
    while current is not None:
        if current.get_data() in node_dict:
            n.delete(current.get_data())
        else:
            node_dict[current.get_data()] = True
        current = current.get_next()
    return n


def removeDups2(n):
    '''
    n is the doubly linked list
    remove duplicates from n without using additional data structure
    '''
    current = n.get_head()
    while current is not None:
        runner = current.get_next()
        while runner is not None:
            if runner.get_data() == current.get_data():
                n.delete(runner.get_data())
            runner = runner.get_next()
        current = current.get_next()
    return n


def printLinkedList(n):
    current = n.get_head()
    while current is not None:
        print(current.get_data(), end=" ")
        current = current.get_next()
    print()


def main():
    n = LinkedList()
    n.push_front(10)
    n.push_front(20)
    n.push_front(30)
    n.push_front(20)
    printLinkedList(n)
    result = removeDups(n)
    result2 = removeDups2(n)
    printLinkedList(result)
    printLinkedList(result2)


if __name__ == "__main__":
    main()
