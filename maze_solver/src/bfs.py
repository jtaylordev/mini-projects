def bfs(graph, start, goal):
    queue = deque()
    queue.append([start])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
    return None
