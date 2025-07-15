# File of project's parameters.
# 
# 
# There you can switch parameters as follows:
# 
#   o: [whatever string chars you want] - responsable of outputted graphics view.
# 
#   mode: "bounded" / "cycled" - responsable of field's cells interraction.
# 
#   output_delay: [int] - delay outputs go.
# 
#   height, width: [int, int] - AUTOMATIC! responsable of field's plot size. Default is the terminal size.


import os
from math import floor



o = ' ░▒▓█'  # graphics units
mode = 'cycled'  # cells interaction type: bounded / cycled
output_delay = 1  # outputs delay



cli_sizes = list (os.get_terminal_size ())
height, width = cli_sizes[1]-1, cli_sizes[0]



field = []  # cells field

field_initial_state = []  # cells field initial state, setted to an empty line with one active cell in a near center:

match width % 2:  # centralizing the cell

    case 1: field_initial_state = [0] * floor(width/2) + [1] + [0] * floor(width/2)  # even width value

    case 0: field_initial_state = [0] * int(width/2) + [1] + [0] * int(width/2-1)  # odd width value

field.append (field_initial_state)