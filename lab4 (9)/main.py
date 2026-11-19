from collections import deque


START = "AAA_NNN"
GOAL = "NNN_AAA"


def legal_moves(board):
    """Выдать допустимые ходы как (новая доска, откуда, куда)."""
    empty = board.index("_")
    for pawn, opponent, direction in (("A", "N", 1), ("N", "A", -1)):
        for distance in (1, 2):
            source = empty - direction * distance
            if not 0 <= source < len(board) or board[source] != pawn:
                continue
            if distance == 2 and board[source + direction] != opponent:
                continue
            cells = list(board)
            cells[source], cells[empty] = cells[empty], cells[source]
            yield "".join(cells), source, empty


def solve(start=START, goal=GOAL):
    """Найти кратчайший путь или вернуть None, если цель недостижима."""
    queue = deque([start])
    previous = {start: None}

    while queue:
        board = queue.popleft()
        if board == goal:
            path = []
            while previous[board] is not None:
                parent, source, target = previous[board]
                path.append((board, source, target))
                board = parent
            return path[::-1]

        for neighbor, source, target in legal_moves(board):
            if neighbor not in previous:
                previous[neighbor] = (board, source, target)
                queue.append(neighbor)

    return None


def main():
    path = solve()
    if path is None:
        print("Решение не найдено.")
        return

    print(f" 0. {START}")
    for number, (board, source, target) in enumerate(path, 1):
        move = "шаг" if abs(source - target) == 1 else "прыжок"
        print(f"{number:2}. {board}  {board[target]} {source + 1} → {target + 1} ({move})")
    print(f"Всего ходов: {len(path)}")


if __name__ == "__main__":
    main()
