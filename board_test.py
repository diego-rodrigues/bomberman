import unittest
from board import Board


board = Board(3, 3, 0)
expected_board = [[3, 0, 2], [0, 1, 0], [0, 2, 2]]


class BoardTestCase(unittest.TestCase):
    def test_create_simple_board(self):
        self.assertEqual(board.x_size, 3)
        self.assertEqual(board.y_size, 3)
        self.assertEqual(expected_board, board.board)
        self.assertEqual(3, board.get_element_at(0, 0))
        self.assertEqual(-1, board.get_element_at(-1, 0))
        self.assertEqual(1, board.get_element_at(1, 1))

    def test_position_man(self):
        self.assertEqual(True, board.can_position_at(0, 1))
        self.assertEqual(False, board.can_position_at(0, 2))
        self.assertEqual(True, board.can_position_at(1, 0))
        self.assertEqual(False, board.can_position_at(1, 1))

if __name__ == '__main__':
    unittest.main()
