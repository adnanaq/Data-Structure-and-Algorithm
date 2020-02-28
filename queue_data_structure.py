# implementation on Doubly Linked List


class Queue():
    # def __int__(self):  # we can instantiate an object with empty constructor pr forst element
    #     pass

    def __init__(self):
        self.size = 0
        offer(first_element)

    # return the size of the queue
    def __len__(self):
        return self.size

    # check if queue is empty
    def isEmpty(self):
        return bool(self.size == 0)

    # peek element from the front of the queue
    # throws error if it's empty
    def peek(self):
        if self.isEmpty():
            raise Exception('Queue Empty')
        return list.peek_first()

    # Poll the element from the front of the queue
    # error if the queue is empty
    def poll(self):
        if self.isEmpty():
            raise Exception('Queue Empty')
        return list.remove_first():

            # Adding element to the back of the queue.
    def offer(self, elem):
        list.append(elen)

    # implementation of iteration
    def __iter__(self):
        pass
