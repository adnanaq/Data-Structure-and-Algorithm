#  Union Find/Disjoint data structure implementation
#  In this implementation, it is assumed that the graph is undirected with bidirectional edge.
#  In undirected graphs we're only intersted in wheather or not the node is part of different component.
# Eelements can be added to the internal storage array by growing it efficienctly,, but efficienctly removing it is not possible without overhead.


class Union_Find(object):
    '''
    Args:
        size (int) is the size of the Union Find at the time of initialization.
    Attributes
        size (int): is the size of Union Find
        _num_components (int): Tracks the number of components in the union find
        _component_size (list): Used to track the size of each of the componenets
        _id (list): id[i] points to the parent i, if id[i] == i, then i is a root node. SInce we created bijection, this is how we access them
    '''

    def __init__(self, size):
        if size <= 0:
            raise Exception('Not a Valid argument')

        self._size = self._num_components = size
        self._component_size = []
        self._id = []

        #  Initializing _id and _compoenent_size to themselves. {_id is root of itself} and {_component_size is size 1 originally}
        for i in range(self._size):
            self._id.append(i)
            self._component_size.append(1)

        #  Find which component/set 'p' belong to, takes amortized constant time.
    def find(self, p):

        #  Find the root of the component
        root = p
        # if the value {root} is not same self._id[root] at the {root} index then it is not root node.
        while root != self._id[root]:
            # while the condition is true, we set the variable root to the next node self._id[root] is pointing to.
            root = self._id[root]

        #  Compress the path leading to the root node
        #  Doing this operation is called 'Path Compression'
        #  and is what gives us amortized constant time complexity.

        while p != root:  # p is not a root mode
            print('second while')
            next = self._id[p]  # saving the value of p to the {next} variable
            # setting the mapping the value at 'p' index to the root node
            self._id[p] = root
            p = next

        return root

    #  Return weather or not the two elements are in the same components/set
    def connected(self, p, q):
        return bool(self.find(p) == self.find(q))

    #  Return the size of componenets/set 'p' belongs to.
    def comp_size(self, p):
        return self._component_size[self.find(p)]

    #  Returns the number of elements in the Union Find/Disjoint Set
    def __len__(self):
        return self._size

    #  Returns the number of remaining components/sets
    def componenets(self):
        return self._num_components

    #  Unify the componenets/sets containing 'p' and 'q'
    def unify(self, p, q):
        root_1 = self.find(p)
        root_2 = self.find(q)

        #  These elements are already in the same set/componenets
        if root_1 == root_2:
            return

        #  Merging two components/sets together
        #  Merging smaller into the larger component/set
        if self._component_size[root_1] < self._component_size[root_2]:
            self._component_size[root_2] += self._component_size[root_1]
            self._id[root_1] = self._id[root_2]
        else:  # if {_component_size[root_1]} > or = to {_component_size[root_2]}
            self._component_size[root_1] += self._component_size[root_2]
            self._id[root_2] = self._id[root_1]

        self._num_components -= 1

    def __str__(self):
        return f'ID: {self._id} \nComponenet SIze: {self._component_size}'


new_li = Union_Find(10)
new_li.unify(3, 6)
new_li.unify(3, 1)
new_li.unify(4, 9)
new_li.unify(4, 0)
new_li.unify(4, 2)
new_li.unify(5, 7)
new_li.unify(5, 8)
new_li.unify(4, 5)
print(new_li)
print('--------')
print(new_li.find(1), 'find')
print('--------')
print(new_li.connected(3, 1), 'connected')
print('--------')
print(new_li.comp_size(3), 'componenet size')
print('--------')
print(new_li.componenets(), 'total components left')
