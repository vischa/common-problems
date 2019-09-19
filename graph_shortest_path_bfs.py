'''

Find shortest path in a given graph using Breadth First Search (BFS).

Traversal:

1. Start BFS by adding a vertex to the "queue". Mark this vertex into "visited".
2. Pop the vertex from "queue" and add its neighbors to the "queue" if they are not in "visited".
3. Repeat step 2 until "queue" is empty.

Trace shortest path:

1. Retrace end node all the way to start node by following back on "visited".

'''

from collections import deque

def bfs(graph, vertex, end=None):
    queue = deque()
    visited = deque()
    queue.appendleft(vertex)
    visited.appendleft(vertex)
    level = {vertex: 0}
    parent_dict = {vertex: None}
    level_index = 1
    while queue:
        parent = queue.popleft()
        for items in graph[parent]:
            if items not in visited:
                queue.append(items)
                visited.append(items)
                level[items] = level_index
                parent_dict[items] = parent
        level_index += 1

    node = end
    path = [end]
    while node != vertex:
        path.append(parent_dict[node])
        node = parent_dict[node]

    return path[::-1]

#Driver code to test functionality

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

print('Graph to be searched: {}.'.format(graph))
print('\nPath from node A to E in the given graph is {}.'.format(bfs(graph, 'A', 'E')))
