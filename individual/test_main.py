import unittest

from main import START, next_states, solve


class JugTests(unittest.TestCase):
    def test_start_only_allows_filling(self):
        self.assertEqual({state for _, state in next_states(START)}, {(7, 0), (0, 5)})

    def test_pours_respect_capacity_and_remaining_water(self):
        self.assertEqual(
            {state for _, state in next_states((2, 3))},
            {(7, 3), (2, 5), (0, 3), (2, 0), (0, 5), (5, 0)},
        )
        self.assertIn((4, 5), {state for _, state in next_states((7, 2))})
        self.assertIn((7, 2), {state for _, state in next_states((4, 5))})

    def test_solution(self):
        path = solve()
        self.assertIsNotNone(path)
        self.assertEqual(
            [state for _, state in path],
            [(7, 0), (2, 5), (2, 0), (0, 2), (7, 2), (4, 5)],
        )

    def test_target_not_reachable_in_five_actions(self):
        reachable = {START}
        for _ in range(5):
            reachable |= {neighbor for state in reachable for _, neighbor in next_states(state)}
        self.assertFalse(any(x == 4 for x, _ in reachable))
