graph = {}
heu = {}
visited = []
queue = []
q = []

def childadd():
    for x in parent:
        print("Enter the children of ", x, " node: ")
        child = list(input().split())
        graph[x] = child

def leafnode() :
    for i in leaf:
        graph[i] = []

def qsort():
    for i in range(len(q)-1):
        min = heu[q[i]]
        l = i
        for j in range(i+1, len(q)):
            y = heu[q[j]]
            if (ch==1) & (min > y):
                min, l = y, j
            elif (ch==2) & (min < y):
                min, l = y, j
        q[i], q[l] = q[l], q[i]

def acPath(v):
    queue.append(v)
    if v in goal:
        for i in queue:
            print(i, end=" ")
        print("------Goal node", v, " FOUND!!------")
        exit(0)
    for x in graph[v]:
        if x in visited:
            acPath(x)
            queue.pop()

def bbfs(node):
    q.append(node)
    while q:
        qsort()
        m = q.pop(0)
        visited.append(m)
        if m in goal:
            for i in visited:
                print(i, end=" ")
            print("\nThe actual path: ")
            acPath(root)
        for x in graph[m]:
            if x not in visited:
                q.append(x)

root = input("Enter the root node: ")
parent = list(map(str, input("Enter the parent nodes: ").split()))

h = list(map(int, input("Enter the heuristic values of parent nodes resp: ").split()))
for i in range(len(parent)):
    heu[parent[i]] = int(h[i])

leaf = list(map(str, input("Enter the leaf nodes: ").split()))
h = list(input("Enter the heuristic values of leaf nodes resp: ").split())
for i in range(len(leaf)):
    heu[leaf[i]] = int(h[i])

childadd()
leafnode()

ch=int(input("1-> Minimization\n2-> Maximization\nEnter your choice: "))

ele,val=root,heu[root]
for x in heu:
    if (ch==1) & (heu[x] < val):
        val,ele=heu[x],x
    elif (ch==2) & (heu[x] > val):
        val,ele=heu[x],x

goal=ele
if root in goal:
    print("Root node is the goal node")
else:
    print("Following is the Best-First Search\nTraversal path:")
    bbfs(root)
    for i in visited:
        print(i, end=" ")
    print("------Goal node NOT FOUND  :((------")
