#  
#  There the system main logic hides.
#  For now the system just does blinks.
#  


import time
from filling import display 
from filling.project_lib import *


o = ' ░▒▓█'  # Pixels! These are the main graphics building blocks!


def main ():

    clear_terminal ()
    test_blinks ()


def test_blinks ():

    while 1:

        width, height = display.sizes().values()

        for pic in o + o[1:-1][::-1]:

            new_frame = ''.join (''.join (pic for w in range(width)) + '\n' for h in range(height))

            display.update (new_frame)

            time.sleep(1/25)  # Note: a dysplay is already updating every FPS. So it is like an upper updates.