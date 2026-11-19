import random


class Maze:
    """Лабиринт W x H клеток. У каждой клетки 4 стены: N, E, S, W."""

    def __init__(self, width=14, height=14):
        self.width = width
        self.height = height
        self.start = (0, 0)                      # вход: левый верхний угол
        self.goal = (width - 1, height - 1)      # выход: правый нижний угол
        self.reset_walls()

    def reset_walls(self):
        self.walls = [
            [{ "N": True, "E": True, "S": True, "W": True }
             for _ in range(self.width)]
            for _ in range(self.height)
        ]

    def generate_backtracker(self, seed=None):
        """Итеративный Recursive Backtracker. Дает perfect maze (путь единственен)."""
        if seed is not None:
            random.seed(seed)
        self.reset_walls()

        visited = [[False] * self.width for _ in range(self.height)]
        stack = [self.start]
        visited[self.start[1]][self.start[0]] = True

        # (dx, dy, стена_текущей, стена_соседа)
        dirs = [(0, -1, "N", "S"), (1, 0, "E", "W"),
                (0, 1, "S", "N"), (-1, 0, "W", "E")]

        while stack:
            x, y = stack[-1]
            candidates = []
            for dx, dy, w1, w2 in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height \
                        and not visited[ny][nx]:
                    candidates.append((nx, ny, w1, w2))
            if candidates:
                nx, ny, w1, w2 = random.choice(candidates)
                self.walls[y][x][w1] = False
                self.walls[ny][nx][w2] = False
                visited[ny][nx] = True
                stack.append((nx, ny))
            else:
                stack.pop()

        # Пробиваем вход (верх (0,0)) и выход (низ (13,13)) для визуализации.
        # На решение не влияет: поиск идет по клеткам внутри поля.
        self.walls[0][0]["N"] = False
        self.walls[self.height - 1][self.width - 1]["S"] = False
        return self

    def can_move(self, x, y, nx, ny):
        """True, если клетки соседние и между ними нет стены."""
        dx, dy = nx - x, ny - y
        if abs(dx) + abs(dy) != 1:
            return False
        if not (0 <= nx < self.width and 0 <= ny < self.height):
            return False
        if dx == 1:
            return not self.walls[y][x]["E"]
        if dx == -1:
            return not self.walls[y][x]["W"]
        if dy == 1:
            return not self.walls[y][x]["S"]
        return not self.walls[y][x]["N"]
