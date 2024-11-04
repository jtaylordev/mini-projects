from collections import deque


def maze_to_graph(maze):
    height = len(maze)
    width = len(maze[0])
    graph = {}

    for y in range(height):
        for x in range(width):
            if maze[y][x] == 0:
                node = (x, y)
                neighbors = []
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height:
                        if maze[ny][nx] == 0:
                            neighbors.append((nx, ny))
                graph[node] = neighbors
    return graph
