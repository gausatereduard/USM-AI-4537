import argparse
import random


VALUES = tuple(range(1, 11))
WEIGHTS = (4, 3, 2, 1, 0, 0, 1, 2, 3, 4)
MAX_SCORE = sum(value * weight for value, weight in zip(VALUES, sorted(WEIGHTS)))
POPULATION_SIZE = 60
MAX_GENERATIONS = 200
MUTATION_RATE = 0.25


def fitness(chromosome):
    return sum(value * weight for value, weight in zip(chromosome, WEIGHTS))


def crossover(first, second, rng):
    """Скрещивание с сохранением порядка (OX)."""
    size = len(first)
    left, right = sorted(rng.sample(range(size + 1), 2))
    child = [0] * size
    child[left:right] = first[left:right]
    used = set(first[left:right])
    free_positions = list(range(right, size)) + list(range(left))
    remaining = (value for value in second[right:] + second[:right] if value not in used)
    for position, value in zip(free_positions, remaining):
        child[position] = value
    return tuple(child)


def mutate(chromosome, rng):
    child = list(chromosome)
    first, second = rng.sample(range(len(child)), 2)
    child[first], child[second] = child[second], child[first]
    return tuple(child)


def solve(seed):
    """Вернуть лучшую перестановку и историю лучших оценок по поколениям."""
    rng = random.Random(seed)
    population = [tuple(rng.sample(VALUES, len(VALUES))) for _ in range(POPULATION_SIZE)]
    history = []

    for generation in range(MAX_GENERATIONS + 1):
        scores = [fitness(chromosome) for chromosome in population]
        best_index = max(range(POPULATION_SIZE), key=scores.__getitem__)
        best = population[best_index]
        history.append(scores[best_index])
        if history[-1] == MAX_SCORE or generation == MAX_GENERATIONS:
            return best, history

        def select_parent():
            candidates = rng.sample(range(POPULATION_SIZE), 3)
            return population[max(candidates, key=scores.__getitem__)]

        next_population = [best]
        while len(next_population) < POPULATION_SIZE:
            child = crossover(select_parent(), select_parent(), rng)
            if rng.random() < MUTATION_RATE:
                child = mutate(child, rng)
            next_population.append(child)
        population = next_population


def main():
    parser = argparse.ArgumentParser(description="Распределение чисел генетическим алгоритмом")
    parser.add_argument("--seed", type=int, default=42, help="Начальное значение генератора, по умолчанию 42")
    args = parser.parse_args()
    best, history = solve(args.seed)

    print("Распределение:", *best)
    print(f"Оценка: {history[-1]} из {MAX_SCORE}")
    print(f"Поколение: {len(history) - 1}")
    print("Лучшая оценка по поколениям:", *history)
    print("Статус:", "достигнут максимум" if history[-1] == MAX_SCORE else "достигнут лимит поколений")


if __name__ == "__main__":
    main()
