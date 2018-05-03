''' use a single array to implement three stacks '''
# Fixed length solution


class FixedMultiStack(object):
    numberOfStacks = 3

    def __init__(self, stackCapacity):
        # max number of elements in each stack
        self.stackCapacity = stackCapacity
        # array to store elements of all stacks
        self.data = [None] * (FixedMultiStack.numberOfStacks * stackCapacity)
        # array to store lengths of the stacks
        self.sizes = [0] * FixedMultiStack.numberOfStacks

    def isFull(self, stackNum):
        ''' return True if the stack is full '''
        return self.sizes[stackNum] == self.stackCapacity

    def indexOfTop(self, stackNum):
        ''' return the top index of the stack '''
        offset = stackNum * self.stackCapacity
        size = self.sizes[stackNum]
        return offset + size

    def push(self, stackNum, element):
        ''' add an element at the top of the desired array '''
        if self.isFull(stackNum):
            raise IndexError("stack is full.")
        self.data[self.indexOfTop(stackNum)] = element
        self.sizes[stackNum] += 1

    def top(self, stackNum):
        ''' return the element at the top of the stack '''
        if self.sizes[stackNum] == 0:
            raise IndexError("stack is empty.")
        return self.data[self.indexOfTop(stackNum) - 1]
