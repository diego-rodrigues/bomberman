from random import randint
from board import Board
from random import seed


class Bomberman:
    """ Class to define a bomberman. """
    def __init__(self, index: int, color: str, position_x: int = 0, position_y: int = 0, seed_value: int = 0):
        self.index = index
        self.color = color
        self.x = position_x
        self.y = position_y
        self.bombs = 1
        self.fire = 1
        seed(seed_value)

    def move_random(self, board: Board) -> None:
        """ Moves (or not) the bomberman. """
        rnd_move_idx = randint(0,4)
        # moves: stay, up, left, right, down
        moves = [[0,0], [0,-1], [-1,0], [1,0], [0,1]]

        if board.can_position_at(self.x + moves[rnd_move_idx][0], self.y + moves[rnd_move_idx][1]):
            board.set_element_at_position(0, self.x, self.y)
            self.x += moves[rnd_move_idx][0]
            self.y += moves[rnd_move_idx][1]
            board.set_element_at_position(3, self.x, self.y)
            print("Bomberman moved to [", self.x, ",", self.y, "]")




