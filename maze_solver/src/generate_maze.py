import random


def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]
    visited = [[False for _ in range(width)] for _ in range(height)]

    def carve_passages(cx, cy):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(directions)

        visited[cy][cx] = True
        maze[cy][cx] = 0  # Mark the cell as a passage

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx]:
                # Remove wall between current cell and neighbor
                maze[ny][nx] = 0
                carve_passages(nx, ny)

    carve_passages(0, 0)
    return maze
