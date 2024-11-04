import random
from collections import deque
import matplotlib.pyplot as plt

def generate_maze(width, height):
    # Adjust the maze dimensions to include walls and cells
    maze_width = width * 2 + 1
    maze_height = height * 2 + 1

    # Initialize the maze grid with walls
    maze = [[1 for _ in range(maze_width)] for _ in range(maze_height)]
    visited = [[False for _ in range(width)] for _ in range(height)]

    def carve_passages(cx, cy):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        random.shuffle(directions)

        visited[cy][cx] = True
        x, y = cx * 2 + 1, cy * 2 + 1
        maze[y][x] = 0  # Mark the current cell as a path

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx]:
                # Remove wall between current cell and neighbor
                wall_x = x + dx
                wall_y = y + dy
                maze[wall_y][wall_x] = 0  # Remove the wall
                carve_passages(nx, ny)

    carve_passages(0, 0)
    return maze

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

def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if result is not None:
                return result
    return None

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
        for neighbor in graph.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
    return None

def draw_maze(maze, path=None):
    height = len(maze)
    width = len(maze[0])
    plt.figure(figsize=(width / 10, height / 10))
    plt.imshow(maze, cmap=plt.cm.binary, interpolation='nearest')

    if path:
        # Adjust path coordinates for display
        x_coords = [x for x, y in path]
        y_coords = [y for x, y in path]
        plt.plot(x_coords, y_coords, color='red', linewidth=2)

    plt.xticks([]), plt.yticks([])
    plt.show()

def main():
    # Maze dimensions (number of cells)
    width, height = 10, 10  # Adjust these values for larger or smaller mazes
    maze = generate_maze(width, height)
    graph = maze_to_graph(maze)
    start = (1, 1)  # Starting position in the maze
    goal = (width * 2 - 1, height * 2 - 1)  # Goal position in the maze

    # Choose algorithm
    path = dfs(graph, start, goal)
    # Or use BFS by commenting the above line and uncommenting the line below
    # path = bfs(graph, start, goal)

    if path:
        print("Path found!")
    else:
        print("No path found.")

    draw_maze(maze, path)

if __name__ == "__main__":
    main()
