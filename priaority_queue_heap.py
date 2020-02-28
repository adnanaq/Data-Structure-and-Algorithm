class PQueue(object):

    #  Contruction of Priority Queue using heapify in 0(n) time
    def __init__(self, data):
        self.data = data
        self.heap_size = self.heap_capacity = len(self.data)
        self.heap = []
        self.dict = {}

        #  adding elements to the heap to heapify and to dict for hash table
        for i, v in enumerate(self.data):
            self._map_add(v, i)
            self.heap.append(v)

        # heapify process O(n)
        for i in range(self.heap_size//2 - 1, -1, -1):
            self._sink(i)

    def isEmpty(self):
        return bool(self.heap_size == 0)

    #  Clear everything in O(n) times
    def clear(self):
        for i in range(self.heap_capacity):
            self.heap[i] = None
        self.heap_size = 0
        self.dict.clear()

    #  Returns the size of the heaps
    def __len__(self):
        return self.heap_size

    #  Returns the value of the element with the lowest
    #  priority in this priority queue. If the prioarity is empty
    #  None is returned
    def peek(self):
        if self.isEmpty():
            return None
        return self.heap[0]

    #  Removes the room of the heap, O(log(n))
    def poll(self):
        return self.remove_at(0)

    #  Tet if the element is in the heap O(1)
    def contains(self, elem):
        if elem == None:
            return False
        return bool(elem in dict.keys())

    ''' Linear scan to check containment, O(n)
    for i in dict:
        if elem == i:
            return True
    return False
    '''

    #  Adding elements to the priority queue, and should not be None O(log(n))
    def add(self, elem):
        if elem == None:
            raise Exception('Enter Valid Data')
        if self.heap_size < self.heap_capacity:
            self.heap[self.heap_size] = elem
        else:
            self.heap.append(elem)
            self.heap_capacity += 1

        self._map_add(elem, self.heap_size)
        self._swim(self.heap_size)
        self.heap_size += 1
    #  Comparing two node values at index i and j

    def _less(self, i, j):
        first_node = self.heap[i]
        second_node = self.heap[j]
        if first_node <= second_node:
            return True

    def _swim(self, k):
        #  Grabbing the parent of the k index
        parent = (k-1)//2
        # keep swimming until the conditions until we have not
        #  reached the room and while we;re _less than parent.
        while k > 0 and self._less(k, parent):
            #  Exchnage k with parent
            self._swap(parent, k)
            k = parent

            # Grab the index of the next parent node WRT to k
            parent = (k-1)//2

    #  Top-down node _sink O(log(n))
    def _sink(self, k):
        while True:
            left_node = 2 * k + 1
            right_node = 2 * k + 2

            smallest = left_node

            if right_node < self.heap_size and self._less(right_node, left_node):
                smallest = right_node

            if left_node >= self.heap_size or self._less(k, smallest):
                break

            self._swap(smallest, k)
            k = smallest

    def _swap(self, i, j):
        if i != self.heap_size:
            i_elem = self.heap[i]
            j_elem = self.heap[j]

            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

            self._map_swap(i_elem, j_elem, i, j)

    def remove(self, element):
        if element == None:
            return False

        index = self.dict[element][0]
        # if len(index) > 1:
        #     index = index[0]
        if index != None:
            self.remove_at(index)
        return index != None

    def remove_at(self, i):
        if self.isEmpty():
            return None
        self.heap_size -= 1
        removed_data = self.heap[i]

        self._swap(i, self.heap_size)

        self.heap[self.heap_size] = None
        self._mad_remove(removed_data, self.heap_size)
        if i == self.heap_size:
            return removed_data

        elem = self.heap[i]

        self._sink(i)

        if self.heap[i] is elem:
            self._swim(i)
        return removed_data

    # Add node value and index to the map
    def _map_add(self, value, index):
        if value not in self.dict:
            self.dict[value] = [index]
        if index not in self.dict[value]:
            self.dict[value].append(index)

    #  Remove the index for/at the givn value O(log(n))
    def _mad_remove(self, value, index):
        set_mapping = self.dict[value]
        set_mapping.remove(index)

        if len(self.dict[value]) == 0:
            del self.dict[value]

    def _map_swap(self, val_1, val_2, val_index_1, val_index_2):
        set_mapping_1 = self.dict.get(val_1)
        set_mapping_2 = self.dict.get(val_2)

        set_mapping_1.remove(val_index_1)
        if set_mapping_1 != set_mapping_2:
            set_mapping_2.remove(val_index_2)

        self.dict[val_1].append(val_index_2)
        self.dict[val_2].append(val_index_1)

    def is_min_heap(self, k):
        #  If we are outside the bound of the heap size, return True
        if k >= self.heap_size:
            return True

        left_child = 2*k + 1
        right_child = 2*k + 2

        #  Make sure current node is less than the size of the heap and
        #  less than it's left and right child. Return False if current node is
        #  smaller than it's children, to indicate invalid heap.
        if left_child < self.heap_size and not self._less(k, left_child):
            return False
        if right_child < self.heap_size and not self._less(k, right_child):
            return False

        return self.is_min_heap(left_child) and self.is_min_heap(right_child)

    def __str__(self):
        res = list(filter(None, self.heap))
        return f'heap_size: {self.heap_size}, \nheap_capacity: {self.heap_capacity}, \nheap: {res}, \ndict: {self.dict}'


new_pq = PQueue([1, 0, 3, 3, 6, 5, 9, 2])
print(new_pq.is_min_heap(0))
