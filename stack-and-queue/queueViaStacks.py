'''
Implement a MyQueue class which implements a queue using two stacks.
'''


class Stack:
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def is_Empty(self):
        return len(self.array) == 0

    def push(self, e):
        self.array.append(e)

    def top(self):
        return self.array[-1]

    def pop(self):
        return self.array.pop()


class MyQueue:
    def __init__(self):
        self.stackOldest = Stack()
        self.stackNewest = Stack()

    def size(self):
        return len(self.stackNewest) + len(self.stackOldest)

    def add(self, e):
        ''' add to the newest elemnt which has the newest element on top'''
        self.stackNewest.push(e)

    def shiftStacks(self):
        ''' move the element from the stackNewest to the stackOldest '''
        if(self.stackOldest.is_Empty()):
            while not self.stackNewest.is_Empty():
                self.stackOldest.push(self.stackNewest.pop())

    def top(self):
        self.shiftStacks()
        return self.stackOldest.top()

    def remove(self):
        self.shiftStacks()
        return self.stackOldest.pop()
