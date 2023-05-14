closed = []
open = {}

def hill_climbing(node, node_val):
    closed.append(node)
    if node is not goal:
        if graph[node] != {}:
            neighbour = max(graph[node].keys(), key=lambda i: graph[node][i])
            neighbour_val = graph[node][neighbour]
            if node_val > neighbour_val:
                path(closed)
                print("\nReached Local Maxima: ", node)
                print("Global Maxima is: ", goal)
                return
            if node_val == neighbour_val:
                print("Reached Local Maxima: ", node)
                print("Global Maxima is: ", goal)
                path(closed)
                print("\nPlateau reached")
            else:
                hill_climbing(neighbour, neighbour_val)
        else:
            path(closed)
            print("\nReached Local Maxima: ", node)
            print("Global Maxima is: ", goal)
            return
    if node is goal:
        print("Goal", node, "found")
        path(closed)
        print("\nThis is the Global Maxima!")
        if graph[node] != {}:
            # return the max parent node of graph by comparing their child values
            neighbour = max(graph[node].keys(), key=lambda i: graph[node][i])
            neighbour_val = graph[node][neighbour]
            if node_val == neighbour_val:
                print("Plateau reached")
                return

def path(closed):
    print("Path Traversed is :", end="")
    for v in closed:
        print("->", v, end="")

graph = {}
child = {}
print("Implementation of Hill Climbing Algorithm\n")
size = int(input("Enter the number of nodes: "))
# here node refers to the parent/key value
for i in range(size):
    print("Enter node", i + 1, ": ")
    node = input()
    graph[node] = {}
    print("Enter the number of children", node, "has: ")
    n = int(input())
    for j in range(n):
        child = input("Enter the child: ")
        hval = int(input("Enter the value: "))
        graph[node][child] = hval

start = input("Enter start Node: ")
sval = int(input("Enter the value of start node: "))

goal = start
goal_val = 0
for k, v in graph.items():
    if v != {}:
        max_n = max(v.keys(), key=lambda i: v[i])
        max_v = v[max_n]
        if max_v > goal_val:
            goal_val = max_v
            goal = max_n

if sval > goal_val:
    print("Start node is the goal node")
else:
    open = {start: sval}
    hill_climbing(start, sval)
