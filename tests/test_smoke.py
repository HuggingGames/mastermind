import unittest
from game import new_game, play

class BasicTest(unittest.TestCase):
    def test_starts_and_responds(self):
        state, text = new_game()
        self.assertIsInstance(state, dict)
        self.assertTrue(text)
        state, text = play(state, "invalid command")
        self.assertIsInstance(state, dict)
        self.assertIsInstance(text, str)

if __name__ == "__main__": unittest.main()
