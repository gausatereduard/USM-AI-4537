"""Отрисовка лабиринта: ASCII + matplotlib."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def to_ascii(maze, path=None):
    path_set = set(path or [])
    W, H = maze.width, maze.height
    lines = []
    for y in range(H):
        top, mid = "", ""
        for x in range(W):
            top += "+" + ("---" if maze.walls[y][x]["N"] else "   ")
            if (x, y) in path_set:
                cell = " . "
            elif (x, y) == maze.start:
                cell = " S "
            elif (x, y) == maze.goal:
                cell = " F "
            else:
                cell = "   "
            mid += ("|" if maze.walls[y][x]["W"] else " ") + cell
        lines.append(top + "+")
        lines.append(mid + ("|" if maze.walls[y][W - 1]["E"] else " "))
    bottom = ""
    for x in range(W):
        bottom += "+" + ("---" if maze.walls[H - 1][x]["S"] else "   ")
    lines.append(bottom + "+")
    return "\n".join(lines)


def plot_maze(maze, path=None, save_to="maze.png", title=None):
    fig, ax = plt.subplots(figsize=(8, 8))
    W, H = maze.width, maze.height

    # стены
    for y in range(H):
        for x in range(W):
            w = maze.walls[y][x]
            if w["N"]:
                ax.plot([x, x + 1], [y, y], color="black", linewidth=1.5)
            if w["S"]:
                ax.plot([x, x + 1], [y + 1, y + 1], color="black", linewidth=1.5)
            if w["W"]:
                ax.plot([x, x], [y, y + 1], color="black", linewidth=1.5)
            if w["E"]:
                ax.plot([x + 1, x + 1], [y, y + 1], color="black", linewidth=1.5)

    # путь: красная линия по центрам клеток
    if path:
        xs = [x + 0.5 for x, y in path]
        ys = [y + 0.5 for x, y in path]
        ax.plot(xs, ys, color="red", linewidth=2.5)

    # старт / финиш
    sx, sy = maze.start
    gx, gy = maze.goal
    ax.plot(sx + 0.5, sy + 0.5, marker="o", color="green", markersize=10, zorder=3)
    ax.plot(gx + 0.5, gy + 0.5, marker="X", color="red", markersize=10, zorder=3)

    ax.set_xlim(-0.2, W + 0.2)
    ax.set_ylim(H + 0.2, -0.2)  # y вниз: (0,0) сверху слева
    ax.set_aspect("equal")
    ax.axis("off")
    if title:
        ax.set_title(title)
    fig.tight_layout()
    fig.savefig(save_to, dpi=150)
    plt.close(fig)
    return save_to
