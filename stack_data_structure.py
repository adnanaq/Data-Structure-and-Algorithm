class Stack(object):
    # initialize with empty instance variable or with instance variable.
    def __init__(self):
        self.size = 0

    # return the size of the stack
    def __len__(self):
        return self.size

    # Check if stack is empty or not
    def isEmpty(self):
        return bool(self.size == 0)

    # push/append the element on the stack at the end in the internal linked list.
    def push(self, elem):
        list.append(elem)

    # pop the element off the stack, throws error if it's empty.
    def pop(self):
        if self.isEmpty():
            raise Exception('Empty Stack')
        return list.remove_last()

    # peek the top of the stack without removing the element, throws exception if empty.
    def peek(self):
        if self.isEmpty():
            raise Exception('Empty Stack')
        return list.peek_last()
