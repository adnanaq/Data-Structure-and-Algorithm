class Node(object):
    def __init__(self, data, p=None, n=None):
        self.data = data
        self.previous = p
        self.next = n

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

    def get_previous(self):
        return self.previous

    def set_previous(self, p):
        self.previous = p

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class ListIterator(object):
    def __init__(self, node):
        self.current = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == None:
            raise StopIteration

        result = self.current.data
        self.current = self.current.next

        return result


class DoublyLinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    def isEmpty(self):
        return bool(self.size == 0)

    def add_first(self, elem):
        if self.isEmpty():  # checking if it's true to false., if true,
            # instantiate new Node object and set it to self.head
            self.head = Node(elem)
            self.tail = self.head   # and set the self.tail to the object itself
        else:
            '''instantiating new Node object and setting to current head's previous pointer, 
            and setting the new Node object's previous instance pointer valriable to None, and next instance
            variable to the current self.head'''
            self.head.previous = Node(elem, None, self.head)
            # changing the current head to the recently added Node.
            self.head = self.head.previous
        self.size += 1

    def append(self, elem):
        ''' Same as add_first func but appending at tail'''
        if self.isEmpty():
            self.head = Node(elem)
            self.tail = self.head
        else:
            self.tail.next = Node(elem, self.tail)
            self.tail = self.tail.next
        self.size += 1

    def peek_first(self):
        if self.isEmpty():
            raise Exception('Empty List')
        return self.head.data

    def peek_last(self):
        if self.isEmpty():
            raise Exception('Empty List')
        return self.tail.data

    def clear_list(self):
        trav = self.head
        while trav != None:
            next = trav.next
            trav.previous = trav.next = None
            trav.data = None
            trav = next
        self.head = self.tail = trav = None
        self.size = 0

    def remove_first(self):
        if self.isEmpty():
            raise Exception('Empty List')
        data = self.head.data
        self.head = self.head.next
        self.size -= 1

        if self.isEmpty():
            self.tail = None
        else:
            self.head.previous = None
        return data

    def remove_last(self):
        if self.isEmpty():
            raise Exception('Empty List')
        data = self.tail.data
        self.tail = self.tail.previous
        self.size -= 1

        if self.isEmpty():
            self.head = None
        else:
            self.tail.next = None
        return data

    def remove(self, node):
        if node.previous == None:
            return self.remove_first()
        if node.next == None:
            return self.remove_last()

        node.next.previous = node.previous
        node.previous.next = node.next

        data = node.data

        node.data = None
        node.previous = node.next = node = None

        self.size -= 1
        return data

    def remove_at(self, index):
        if index < 0 or index > self.size - 1:
            raise Exception(IndexError)

        if index <= self.size//2:
            trav = self.head
            for i in range(self.size//2 + 1):
                if i != index:
                    next = trav.next
                    trav = next
                else:
                    return self.remove(trav)
        else:
            trav = self.tail
            for i in range(self.size-1, self.size//2, -1):
                if i != index:
                    previous = trav.previous
                    trav = previous
                else:
                    return self.remove(trav)

    def remove_value(self, obj):
        trav = self.head
        if obj == None:
            for _ in range(self.size):
                next = trav.next
                if trav.data is None:
                    self.remove(trav)
                    return True
                trav = next
        else:
            for _ in range(self.size):
                next = trav.next
                if obj is trav.data:
                    self.remove(trav)
                    return True
                trav = next
            return False

    def index_of(self, obj):
        trav = self.head
        if obj == None:
            for index in range(self.size):
                next = trav.next
                if trav.data is None:
                    return index
                trav = next
        else:
            for index in range(self.size):
                next = trav.next
                if trav.data is obj:
                    return index
                trav = next
        return -1

    def contains(self, obj):
        return bool(self.index_of(obj) != -1)

    def __iter__(self):
        return ListIterator(self.head)

    def __str__(self):
        if self.isEmpty():
            return '[]'
        else:
            new_st = '['
            trav = self.head
            for _ in range(self.size):
                next = trav.next
                new_st += str(trav.data) + ', '
                trav = next
            return new_st[:-2] + ']'


new_n = DoublyLinkedList()

new_n.append(1)
new_n.append(2)
new_n.append(3)
new_n.append(4)
new_n.append(5)
new_n.append(6)

new_n.add_first(0)
new_n.append(None)

# new_n.remove_first()

# print(new_n.peek_first())
# print(new_n.peek_last())

# new_n.remove_at(5)
# print(new_n.remove_value(7))

print(new_n.index_of(4))
print(new_n.contains(9))
print(len(new_n))
print(new_n)

for i in new_n:
    print(i)
