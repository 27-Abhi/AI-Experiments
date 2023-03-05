#dfs using python
'''
Algo:
Three lists:- Open(nodes which are not yet visited)
closed(nodes which are visited)
child(Child nodes of the parent)

->iterate through the open list until it is empty
-->pop from open list and push the same into closed list.
-->push its child nodes in child list
-->check for any unvisited child nodes ie not in closed list
-->push the unvisited child nodes in the open list and repeat.

'''

def dfs(graph, start_node, end_node):
    # Initialize open and closed lists
    open_list = [start_node]
    closed_list = []
    child_list = []

    # Loop until the open list is empty
    while open_list:
        # Get the last node in the open list
        current_node = open_list.pop()

        # Check if the current node is the end node
        if current_node == end_node:
            return True, child_list 

        # Add the current node to the closed list
        closed_list.append(current_node)

        # Get the neighbors of the current node
        neighbors = graph[current_node]

        # Loop through the neighbors
        for neighbor in neighbors:
            # Check if the neighbor is already in the closed list
            if neighbor in closed_list:
                continue

            # Add the neighbor to the open list
            open_list.append(neighbor)
            child_list.append(neighbor)

    # If the open list is empty and we haven't found the end node, return False
    return False, child_list


def main():
    # Sample input dictionary
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H', 'I'],
        'E': ['J'],
        'F': ['K'],
        'G': [],
        'H': [],
        'I': [],
        'J': [],
        'K': []
    }

    start_node = 'A'
    end_node = 'K'

    found, sequence = dfs(graph, start_node, end_node)

    if found:
        print('Path found!')
        print('Sequence:', sequence)
    else:
        print('Path not found.')


if __name__ == '__main__':
    main()


