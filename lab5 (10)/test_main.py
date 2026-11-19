import random
import unittest

from main import MAX_GENERATIONS, MAX_SCORE, VALUES, crossover, fitness, mutate, solve


class GeneticAlgorithmTests(unittest.TestCase):
    def test_fitness(self):
        self.assertEqual(MAX_SCORE, 150)
        self.assertEqual(fitness((10, 8, 6, 4, 2, 1, 3, 5, 7, 9)), MAX_SCORE)
        self.assertEqual(fitness((10, 7, 6, 3, 2, 1, 4, 5, 8, 9)), MAX_SCORE)
        self.assertEqual(fitness((1, 3, 5, 7, 9, 10, 8, 6, 4, 2)), 70)

    def test_operators_preserve_permutations(self):
        rng = random.Random(7)
        for _ in range(100):
            first, second = (tuple(rng.sample(VALUES, len(VALUES))) for _ in range(2))
            child = crossover(first, second, rng)
            self.assertEqual(tuple(sorted(child)), VALUES)
            mutated = mutate(child, rng)
            self.assertEqual(tuple(sorted(mutated)), VALUES)
            self.assertEqual(sum(a != b for a, b in zip(child, mutated)), 2)

    def test_search_and_reproducibility(self):
        result = solve(42)
        self.assertEqual(result, solve(42))
        best, history = result
        self.assertEqual(tuple(sorted(best)), VALUES)
        self.assertEqual(fitness(best), MAX_SCORE)
        self.assertEqual(history[-1], fitness(best))
        self.assertEqual(history, sorted(history))
        self.assertLessEqual(len(history) - 1, MAX_GENERATIONS)
