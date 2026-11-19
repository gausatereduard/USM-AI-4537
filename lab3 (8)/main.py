"""main.py — генерация 14x14 + DFS по часовой + проверка BFS + картинка."""
import argparse
import time

from maze import Maze
from solver import dfs_clockwise, bfs
from plot import to_ascii, plot_maze


def main():
    ap = argparse.ArgumentParser(description="Лабиринт 14x14")
    ap.add_argument("--size", type=int, default=14)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", type=str, default="maze.png")
    args = ap.parse_args()

    t0 = time.perf_counter()
    maze = Maze(args.size, args.size).generate_backtracker(seed=args.seed)
    t_gen = time.perf_counter() - t0

    t0 = time.perf_counter()
    path, visited_order = dfs_clockwise(maze)
    t_dfs = time.perf_counter() - t0

    ref = bfs(maze)

    print(f"Размер: {args.size}x{args.size}, seed={args.seed}")
    print(f"Генерация (Backtracker): {t_gen * 1000:.2f} мс")
    if path is None:
        print("DFS: путь НЕ найден (не должно случиться в perfect maze)")
        return
    print(f"DFS: длина пути = {len(path)} клеток, посещено = {len(visited_order)}, "
          f"{t_dfs * 1000:.2f} мс")
    print(f"BFS (эталон): длина = {len(ref)} клеток")
    print(f"Оптимальность: {'ДА (len DFS == len BFS)' if len(ref) == len(path) else 'НЕТ!'}")
    print(f"Путь (первые 10): {path[:10]}")
    print(f"Путь (последние 10): {path[-10:]}")
    print()
    print(to_ascii(maze, path))

    saved = plot_maze(maze, path, save_to=args.out,
                      title=f"Maze {args.size}x{args.size} seed={args.seed}, "
                            f"DFS path={len(path)}")
    print(f"\nКартинка сохранена: {saved}")


if __name__ == "__main__":
    main()
