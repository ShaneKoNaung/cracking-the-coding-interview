'''
program to sort a stack such that the smallest items are on the top using an
additional stack
'''


class Stack:
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.array[-1]

    def push(self, e):
        self.array.append(e)

    def pop(self):
        return self.array.pop()


def sortStack(stack):
    # create a temp Stack
    temp_stack = Stack()
    temp = None  # temp variable to store the top element
    while not stack.is_empty():
        temp = stack.pop()
        while not temp_stack.is_empty() and temp < temp_stack.peek():
            stack.push(temp_stack.pop())
        temp_stack.push(temp)
    return shiftStack(temp_stack, stack)


def shiftStack(a, b):
    while not a.is_empty():
        b.push(a.pop())
    return b


def main():
    a = Stack()
    for i in range(20, 0, -1):
        a.push(i)
    sortStack(a)
    while not a.is_empty():
        print(a.pop())


if __name__ == "__main__":
    main()
