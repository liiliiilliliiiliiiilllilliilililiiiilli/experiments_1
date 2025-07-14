import os
from math import floor



o = ' ░▒▓█'
mode = 'cycled'  # bounded / cycled



cli_sizes = list (os.get_terminal_size ())
height, width = cli_sizes[1]-1, cli_sizes[0]



field = []  # system's cells field


field_initial_state = []

# empty line with one active cell in the near center:

match width % 2:  # centralizing the cell

    case 1: field_initial_state = [0 for i in range (floor(width/2))] + [1] + [0 for i in range (floor(width/2))]

    case 0: field_initial_state = [0 for i in range (int(width/2))] + [1] + [0 for i in range (int(width/2-1))]


field.append (field_initial_state)