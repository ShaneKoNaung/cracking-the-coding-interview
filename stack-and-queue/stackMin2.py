# in this implementation, I don't store a min value in each Node
# instead, I keep a seperate stack for the min values


class Stack(object):
    def __init__(self):
        self._data = []

    def push(self, e):
        ''' add element at the top of the stack '''
        self._data.append(e)

    def top(self):
        ''' return the element at the top of the stack '''
        return self._data[-1]

    def pop(self):
        ''' return and remove the element at the top of the stack'''
        return self._data.pop()


class StackWithMin(object):
    def __init__(self):
        self.super = Stack()
        self.min_stack = Stack()

    def push(self, e):
        if len(self.min_stack._data) == 0:
            self.min_stack.push(e)
        elif e <= self.min_stack.top():
            self.min_stack.push(e)
        self.super.push(e)

    def pop(self):
        if self.super.top() == self.min_stack.top():
            self.min_stack.pop()
        return self.super.pop()

    def min(self):
        return self.min_stack.top()
