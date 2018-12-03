graph1 = {"A" : [["B", 10], ["D", 5]], "B" : [["A", 10], ["C", 5]], "C" : [["B", 5], ["D", 15]], "D" : [["C", 15], ["A", 5]]}
graph2 = {"A" : [["B", 10], ["D", 5]], "B" : [["A", 10], ["C", 5]], "C" : [["B", 5], ["D", 15]], "D" : [["C", 15], ["A", 5]], "E" : [["F", 5]], "F" : [["E", 5]]}

def infty(graph):
    """ Returns the highest possible weight of any path plus 1
        to represent infinity.
    """
    visited = []
    sum = 0
    for key, value in graph.items():
        for l in value:
            if (l[0] in visited):
                sum += l[1]
        visited.append(key)
    return sum + 1

def initial(graph, source):
    """ Initializes dijkstra's algorithm by returning a dictionary with starting
        weights associated with each vertex.
    """
    out = {}
    inf = infty(graph)
    for key, value in graph.items():
        if (key == source):
            out[key] = 0
        else:
            out[key] = inf
    return out

def find_min(color, queue):
    """ Finds the minimum weight vertex in the graph that intersects with the queueself.
    """
    if (len(queue) < 1):
        return -1
    min_color = color[queue[0]]
    min = queue[0]
    for key in queue:
        if (color[key] < min_color):
            min_color = color[key]
            min = key
    return min

def dijkstra(graph, source):
    """ Runs dijkstra's algorithm
    """
    inf = infty(graph)
    colors = initial(graph, source)
    currentSrc = source
    previousSrcs = []
    children = []
    for key in graph:
        children.append(key)
    while (len(previousSrcs) != len(graph)):
        for weight in graph[currentSrc]:
            if (weight[0] not in previousSrcs):
                children.append(weight[0])
                if (weight[1] + colors[currentSrc] < colors[weight[0]]):
                    colors[weight[0]] = weight[1] + colors[currentSrc]
        previousSrcs.append(currentSrc)
        if (currentSrc in children):
            children.remove(currentSrc)
        currentSrc = find_min(colors, children)
    return colors

def is_connected(graph):
    """ Determines if a graph is connected
    """
    result = dijkstra(graph, list(graph.keys())[0])
    inf = infty(graph)
    for key, value in result.items():
        if value >= inf:
            return False
    return True

print(dijkstra(graph1, "A"))
print(dijkstra(graph2, "A"))
print(is_connected(graph1))
print(is_connected(graph2))
