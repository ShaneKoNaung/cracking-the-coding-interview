'''
Implement an algorithm to delete a node in the middle (i.e., any node but the
first and last node, not necessarily the exact middle) of a singly linked list,
given only access to that node.
'''


def delMiddle(ll, n):
    '''
    remove a node in the middle
    '''
    if n is None or n.get_next() is None:
        return False
    else:
        next = n.get_next()
        n.set_data(next.get_data())
        n.set_next(next.get_next())
        return True
