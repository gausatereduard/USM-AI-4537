from collections import deque


CAPACITY_7 = 7
CAPACITY_5 = 5
START = (0, 0)
TARGET = 4


def next_states(state):
    """Перечислить действия, меняющие объёмы воды в бидонах."""
    x, y = state
    to_5 = min(x, CAPACITY_5 - y)
    to_7 = min(y, CAPACITY_7 - x)
    actions = (
        ("Наполнить 7-литровый бидон", (CAPACITY_7, y)),
        ("Наполнить 5-литровый бидон", (x, CAPACITY_5)),
        ("Опустошить 7-литровый бидон", (0, y)),
        ("Опустошить 5-литровый бидон", (x, 0)),
        (f"Перелить {to_5} л из 7-литрового в 5-литровый", (x - to_5, y + to_5)),
        (f"Перелить {to_7} л из 5-литрового в 7-литровый", (x + to_7, y - to_7)),
    )
    for action, neighbor in actions:
        if neighbor != state:
            yield action, neighbor


def solve():
    """Вернуть кратчайший список пар (действие, новое состояние)."""
    queue = deque([START])
    previous = {START: None}
    while queue:
        state = queue.popleft()
        if state[0] == TARGET:
            path = []
            while previous[state] is not None:
                parent, action = previous[state]
                path.append((action, state))
                state = parent
            return path[::-1]

        for action, neighbor in next_states(state):
            if neighbor not in previous:
                previous[neighbor] = (state, action)
                queue.append(neighbor)
    return None


def main():
    path = solve()
    if path is None:
        print("Решение не найдено.")
        return

    print(f"0. Оба бидона пусты → {START}")
    for number, (action, state) in enumerate(path, 1):
        print(f"{number}. {action} → {state}")
    print(f"Всего действий: {len(path)}")


if __name__ == "__main__":
    main()
