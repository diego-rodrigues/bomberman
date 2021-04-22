from random import seed, sample, randint
from element import draw_element


def generate_list_of_blocks(positions: [int], number_of_blocks: int) -> [int]:
    """ Randomly generates a list of positions for blocks from the possible positions list. """
    return sample(positions, number_of_blocks)
    # number_of_positions = len(positions)
    # number_of_positions_to_remove = len(positions) - number_of_blocks
    # for i in range(0, number_of_positions_to_remove):
    #     number_of_positions -= 1
    #     positions.pop(randint(0, number_of_positions))
    #
    # return positions


class Board:
    """ Class to define the game board. """

    def __init__(self, size, n_blocks: int, seed_number: int = None):
        if seed_number is not None:
            seed(seed_number)
        self.x_size = size
        self.y_size = size
        self.board = []
        self.generate_board(size, n_blocks)

    def generate_board(self, size: int, blocks: int) -> [int, int]:
        """ Generates the board, puts in bomberman, and blocks. """
        board = []
        for i in range(0, size):
            line = []
            if i % 2 == 0:
                for j in range(0, size):
                    line.append(0)
            else:
                for j in range(0, size):
                    if j % 2 == 0:
                        line.append(0)
                    else:
                        line.append(1)
            board.append(line)

        self.board = board
        self.put_bomberman()
        self.place_blocks(blocks)

    def put_bomberman(self, bomberman_x: int = 0, bomberman_y: int = 0) -> None:
        if self.board[bomberman_x][bomberman_y] == 0:
            self.board[bomberman_x][bomberman_y] = 3

    def place_blocks(self, blocks: int):
        """ Places blocks in the board. """
        available_blocks_positions = self.generate_available_blocks_list()
        positions = generate_list_of_blocks(available_blocks_positions, blocks)
        return self.put_blocks_in_board(positions)

    def put_blocks_in_board(self, positions: [int]) -> None:
        """ Puts blocks in the board according to the blocks positions list. """
        for position in positions:
            x = int(position / self.x_size)
            y = position % self.x_size
            self.board[x][y] = 2

    def generate_available_blocks_list(self) -> [int]:
        """ Generates a list of possible position for blocks. """
        board_list = []
        for y in range(0, self.y_size):
            for x in range(0, self.x_size):
                if self.board[x][y] == 0:
                    board_list.append(x + (y * self.x_size))
                if self.board[x][y] == 3:
                    bomberman_x = x
                    bomberman_y = y

        if ((bomberman_x - 1) + (bomberman_y * self.x_size)) in board_list:  # removes bomberman left
            board_list.remove((bomberman_x - 1) + (bomberman_y * self.x_size))

        if ((bomberman_x + 1) + (bomberman_y * self.x_size)) in board_list:  # removes bomberman right
            board_list.remove((bomberman_x + 1) + (bomberman_y * self.x_size))

        if (bomberman_x + ((bomberman_y - 1) * self.x_size)) in board_list:  # removes bomberman up
            board_list.remove(bomberman_x + ((bomberman_y - 1) * self.x_size))

        if (bomberman_x + ((bomberman_y + 1) * self.x_size)) in board_list:  # removes bomberman down
            board_list.remove(bomberman_x + ((bomberman_y + 1) * self.x_size))

        return board_list

    def get_element_at(self, x: int, y: int) -> int:
        """ Returns the element index at the specified position. """
        if (x < self.x_size) and (y < self.y_size) and (x >= 0) and (y >= 0):
            return self.board[x][y]
        return -1

    def can_position_at(self, x: int, y: int) -> bool:
        """ Returns whether or not a bomberman can be positioned at the specified position. """
        return self.get_element_at(x, y) == 0 or self.get_element_at(x, y) == 3

    def set_element_at_position(self, element_id: int, x: int, y: int) -> bool:
        if (x < self.x_size) and (y < self.y_size) and (x >= 0) and (y >= 0):
            self.board[x][y] = element_id
            return True
        return False

    def draw_board(self) -> None:
        """ Draws the board. """
        for row in self.board:
            for column in row:
                print(draw_element(column), end=" ")
            print()
