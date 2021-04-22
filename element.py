
element = {
    # blank space, bomberman, hard block, block, bomb3, bomb2, bomb1, bomb0, fire
    0: ' ',  # blank space
    1: '▉',  # hard block
    2: '░',  # soft block -- can be broken
    3: 'Ô',  # bomberman
    4: '❖',  # bomb
}


def draw_element(value: int) -> str:
    """ Draws an element in the screen. """
    return element[value]
