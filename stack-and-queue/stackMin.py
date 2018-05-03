'''
 design a stack which, in addition to push and pop, has a function min which
returns the minimum element? Push, pop and min should all operate in 0(1) time.
'''
# In every node there is a min slot for the min element in the existing stack
# and update everytime an element is pushed


class Stack():
    # Node implementation
    class Node():
        # Node initializing
        def __init__(self, data, next=None, min=None):
            self._data = data
            self._next = next
            self._min = min  # a minimun in the stack below this element

    def __init__(self):
        self._head = None
        self._size = 0

    def min(self):
        ''' return the minimum element in the stack '''
        return self._head._min

    def push(self, e):
        ''' add the element to the top of the stack '''
        node = self.Node(e)
        # if the stack is empty
        if self._size == 0:
            node._min = node._data  # the element is the minimun element
        else:
            # if the element is less then the existing stack's minimun
            if node._data < self._head._min:
                node._min = node._data  # the element is the new minimun
            else:
                node._min = self._head._min  # element takes the existing min
        node._next = self._head
        self._head = node
        self._size += 1

    def pop(self):
        ''' return and remove the element from the top of the stack '''
        if self._size == 0:
            raise IndexError("stack is empty")
        answer = self._head._data
        self._head = self._head._next
        return answer
