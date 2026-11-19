import unittest

from main import GOAL, START, legal_moves, solve


class PawnTests(unittest.TestCase):
    def test_examples_from_assignment(self):
        examples = (
            ("ANA_NNA", "ANAN_NA", 4, 3),  # шаг чёрной
            ("AN_ANNA", "ANNA_NA", 4, 2),  # прыжок чёрной
            ("ANA_NNA", "AN_ANNA", 2, 3),  # шаг белой
            ("AAN_NNA", "A_NANNA", 1, 3),  # прыжок белой
        )
        for before, after, source, target in examples:
            with self.subTest(before=before, after=after):
                self.assertIn((after, source, target), list(legal_moves(before)))

    def test_start_allows_only_steps(self):
        self.assertEqual(
            set(legal_moves(START)), {("AA_ANNN", 2, 3), ("AAAN_NN", 4, 3)}
        )

    def test_goal_is_a_dead_end(self):
        self.assertEqual(list(legal_moves(GOAL)), [])
        self.assertIsNone(solve(GOAL, START))

    def test_already_solved(self):
        self.assertEqual(solve(GOAL, GOAL), [])

    def test_solution(self):
        path = solve()
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 15)
        before = START
        jumps = 0
        for after, source, target in path:
            with self.subTest(board=before, source=source, target=target):
                pawn = before[source]
                self.assertIn(pawn, "AN")
                self.assertEqual(before[target], "_")
                delta = target - source
                self.assertIn(delta, (1, 2) if pawn == "A" else (-1, -2))
                if abs(delta) == 2:
                    self.assertEqual(before[(source + target) // 2], "N" if pawn == "A" else "A")
                    jumps += 1
                expected = list(before)
                expected[source], expected[target] = "_", pawn
                self.assertEqual(after, "".join(expected))
            before = after
        self.assertEqual(before, GOAL)
        self.assertEqual(jumps, 9)


if __name__ == "__main__":
    unittest.main()
