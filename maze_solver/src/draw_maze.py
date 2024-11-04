import matplotlib.pyplot as plt


def draw_maze(maze, path=None):
    height = len(maze)
    width = len(maze[0])
    plt.figure(figsize=(width / 5, height / 5))
    plt.imshow(maze, cmap=plt.cm.binary, interpolation='nearest')

    if path:
        x_coords = [x for x, y in path]
        y_coords = [y for x, y in path]
        plt.plot(x_coords, y_coords, color='red', linewidth=2)

    plt.xticks([]), plt.yticks([])
    plt.show()
