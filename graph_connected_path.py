'''
Find and print a connected path between two nodes in a given graph.
'''


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


# Sample test i/o zone
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C', 'E'],
         'E': ['F'],
         'F': ['C']}
start_node = 'A'
end_node = 'E'

print('The given graph is: {}\nFinding connected path between nodes {} and {}:\n{}'.format(graph, start_node, end_node,
                                                                                           find_path(graph, start_node,
                                                                                                     end_node)))
