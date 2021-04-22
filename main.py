from board import Board
from bomberman import Bomberman


def main():
    board = Board(11, 57)
    board.draw_board()
    b1 = Bomberman(0, "white", 0, 0, 0)
    print("-----------------------------------")
    b1.move_random(board)
    board.draw_board()
    print("-----------------------------------")
    b1.move_random(board)
    board.draw_board()
    print("-----------------------------------")
    b1.move_random(board)
    board.draw_board()
    print("-----------------------------------")
    b1.move_random(board)
    board.draw_board()
    print("-----------------------------------")
    b1.move_random(board)
    board.draw_board()
    print("-----------------------------------")
    b1.move_random(board)
    board.draw_board()
    # start_game(board)


if __name__ == "__main__":
    main()
