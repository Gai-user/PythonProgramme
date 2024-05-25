import copy


def getRoute(x_value, nodeNum):
    X = copy.deepcopy(x_value)
    route = [0]
    current_node = 0
    while len(set(route)) < nodeNum+1:
        print(route)
        for i in range(nodeNum+1):
            if X[current_node, i] > 0:
                route.append(i)
                current_node = i
    # route.append(0)
    return route
