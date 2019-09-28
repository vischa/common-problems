'''
Pseudocode:

Initialization:

1. shortest_distance = {}
2. predecessor = {}
3. unseenNodes = graph
4. set infinity
5. initialize path = []
6. For all nodes in unseenNodes, set shortest distances as infinity except start node distance which is 0

Do the following for each node in unseenNodes:

 1. Select vertex node with the minimum shortest distance value, which resides in shortest_distance. This is
    found by iterating through all nodes and getting the lowest distance value node from "shortest_distance".

    minNode = None
    for nodes in unseenNodes:
        if minNode = None:
            minNode = nodes
        elif shortest_distance[nodes] < shortest_distance[minNode]:
            minNode = nodes

 2. For child, weight pair in graph[minNode].items():     [e.g. {'b':10,'c':3} for {'a':{'b':10,'c':3},...}]

    a. Apply relaxation:

        if shortest_distance[minNode] + weight < shortest_distance [child]:
            shortest_distance [child] = shortest_distance[minNode] + weight

    b. Update predecessor:

        predecessor[childNode] = minNode

    c. Pop the worked upon node:

        unseenNodes.pop(minNode)


Traverse predecessor to find path

'''


def dijkstra (graph, start, end):

    predecessor = {}
    unseenNode = graph
    path=[]
    shortest_path={}
    infinity = float('inf')

    for nodes in unseenNode:
        shortest_path[nodes] = infinity
    shortest_path[start] = 0

    while unseenNode:

        minNode = None
        for nodes in unseenNode:

            if minNode is None:
                minNode = nodes
            elif shortest_path[nodes] < shortest_path[minNode]:
                minNode=nodes


        for child, weight in graph[minNode].items():

            if shortest_path[minNode] + weight < shortest_path[child]:
                shortest_path[child] = shortest_path[minNode] + weight
                predecessor[child] = minNode
        unseenNode.pop(minNode)


    path=[end]
    current=end

    while current!=start:

        path.append(predecessor[current])
        current=predecessor[current]

    return path[::-1]











graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}

print(dijkstra(graph,'a','d'))