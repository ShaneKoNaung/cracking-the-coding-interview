''' implementation of a set of stacks '''


class Stack:
    class Node:
        def __init__(self, e, next=None):
            self.data = e
            self.next = next

    def __init__(self):
        self.head = None
        self.next = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        node = Stack.Node(e)
        if self.is_empty():
            self.head = node
            self.size += 1
        else:
            node.next = self.head
            self.head = node
            self.size += 1

    def top(self):
        return self.head.data

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        answer = self.head
        self.head = self.head.next
        self.size -= 1
        return answer.data


class SetOfStacks:
    def __init__(self, capacity):
        ''' initialize the stack of stacks '''
        self.stack_array = []       # array for stacks
        self.capacity = capacity

    def getLastStack(self):
        ''' get the last stack in the stack_array '''
        if len(self.stack_array) == 0:
            return None
        return self.stack_array[-1]

    def isFull(self, stack):
        ''' return True if the stack is full '''
        return stack.size == self.capacity

    def push(self, e):
        ''' add the element at the top of the stack '''
        # if the set of stacks is empty
        if len(self.stack_array) == 0:
            # create a new stack
            stack = Stack()
            # add the stack to the top of the stack_array
            self.stack_array.append(stack)
            stack.push(e)
        else:
            lastStack = self.getLastStack()
            if not self.isFull(lastStack):
                lastStack.push(e)
            else:
                stack = Stack()
                self.stack_array.append(stack)
                stack.push(e)

    def pop(self):
        lastStack = self.getLastStack()
        if lastStack is None:
            return IndexError("Stack is empty")
        answer = lastStack.pop()
        if lastStack.is_empty():
            self.stack_array.remove(lastStack)
        return answer

    # function popAt(int index) which performs a pop operation on a specific
    # sub­ stack.
    def popAt(self, index):
        stack = self.stack_array[index]
        if stack.is_empty():
            raise IndexError("stack is empty")
        answer = stack.pop()
        return answer
