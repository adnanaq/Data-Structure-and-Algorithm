# Pesudo Code


def (Graph, started_node)  # G is graph and s is source, starting node


let Q be the queue
# enqueuing the first/source node to start the search from
Q.enqueue(started_node)

started_node.visited = True  # marking the source node to True as  we visit it

while Q is not empty:   # while there is node/neighbour in the Q, keep looping
    # Once the node is marked visited, it is dequeued from the Q and set to node variable
    node = Q.dequeue()

    # visiting every neighbour of the node variable, set earlier.
    for neighbour in Graph(node):
        if neighbour is not visited:
            # Adding every new neighbour to the Q which isn't visited before.
            Q.enqueue(neighbour)
            neighbour.visited = True    # and marking them to True.
