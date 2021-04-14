"""
This module contains tests for main.py
"""
import unittest
from main import run_game


class TestRunGame(unittest.TestCase):
    def test_zero_turns_should_return_initial_position(self):
        self.assertEqual(run_game(0, True), 1)
    
    def test_zero_turns_does_not_depend_on_dice(self):
        self.assertEqual(run_game(0, False), 1)
    
    def test_negative_turns_should_return_initial_position(self):
        self.assertEqual(run_game(-1, True), 1)
    
    def test_final_position_should_be_less_than_or_equal_to_105(self):
        self.assertLessEqual(run_game(10, True), 105)
        self.assertLessEqual(run_game(20, True), 105)
        self.assertLessEqual(run_game(30, True), 105)
        self.assertLessEqual(run_game(40, True), 105)
        self.assertLessEqual(run_game(50, True), 105)

        self.assertLessEqual(run_game(10, False), 105)
        self.assertLessEqual(run_game(20, False), 105)
        self.assertLessEqual(run_game(30, False), 105)
        self.assertLessEqual(run_game(40, False), 105)
        self.assertLessEqual(run_game(50, False), 105)



if __name__ == "__main__":
    unittest.main()
