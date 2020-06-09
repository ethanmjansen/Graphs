
def earliest_ancestor(ancestors, starting_node):
    parents = []
    children = []

    graph_list = {}

    # Making a dictionary that has children as key and parents as value
    for i in ancestors:
        parents.append(i[0])
        children.append(i[1])

    for i in ancestors:
        if i[1] in children:
            graph_list[i[1]] = []

    for i in ancestors:
        if i[0] in parents:
            graph_list[i[1]].append(i[0])

    # Logic for an integer that doesn't have a parent
    orphans = []
    
    for i in ancestors:
        if i[0] not in children:
            orphans.append(i[0])
    
    if starting_node in orphans:
        return -1

    elif starting_node in children:
        node = starting_node
        while node not in orphans:
            smallest = min(graph_list[node])
            node = smallest
        return smallest
