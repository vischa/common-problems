'''
Pseudocode:

Initialization:
    1. shortest_distance as empty dict
    2. predecessor as empty dict
    3. unseenNode = graph
    4. set infinity value
    5. initialize path array

For all nodes in unseenNode, set shortest distances as infinity except start node distance which is 0.

Do the following for each node in unseenNode:
 1. Select vertex node with the minimum shortest distance value from start, which resides in shortest_distance.
 2. For child, weight pair for connected nodes of selected minNode:
    a. Apply relaxation
    b. Update predecessor
    c. Pop the worked upon node
 3. Traverse predecessor to find shortest path and extract cost to shortest path through shortest_distance dict.

'''


def dijkstra(graph, start, end):
    shortest_distance = {}
    predecessor = {}
    unseenNode = graph
    infinity = float('inf')
    path = []

    for nodes in unseenNode:
        shortest_distance[nodes] = infinity
    shortest_distance[start] = 0

    while unseenNode:
        minNode = None
        for nodes in unseenNode:
            if minNode is None:
                minNode = nodes
            elif shortest_distance[nodes] < shortest_distance[minNode]:
                minNode = nodes
        for items, weight in graph[minNode].items():
            if shortest_distance[minNode] + weight < shortest_distance[items]:
                shortest_distance[items] = shortest_distance[minNode] + weight
                predecessor[items] = minNode
        unseenNode.pop(minNode)

    path.append(end)
    currentNode = end

    while currentNode != start:

        try:
            path.append(predecessor[currentNode])
            currentNode = predecessor[currentNode]

        except Exception as IndexError:
            print('Path from "{}" to "{}" does not exist in the graph.'.format(start, end))
            break

    if shortest_distance[end] != infinity:
        print('Shortest path between "{}" and "{}" is {} with cost {}.'.format(start, end, path[::-1],
                                                                               shortest_distance[end]))


# Driver code to test functionality
graph = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}}

dijkstra(graph, 'a', 'e')
