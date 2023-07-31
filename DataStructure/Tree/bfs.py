graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []
queue = []

def bfs(visited, graph, node):
    queue.append(node)
    print(queue)
    while len(queue) != 0:
        m = queue.pop(0)
        visited.append(m)
        #print(m, end = "->")
        for n in graph[m]:
            if n not in visited:
                queue.append(n)
                visited.append(n)

        print(queue)


if __name__ == '__main__':
    print("Following is the Breadth-First Search")
    bfs(visited, graph, '5')