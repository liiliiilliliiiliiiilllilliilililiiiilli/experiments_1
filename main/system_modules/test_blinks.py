import time

import configuration
from main.project_lib import o
from main import display 


updates_fps = configuration.test_blinks_updates_fps


def test_blinks ():

    while 1:

        width, height = display.sizes().values()

        for pic in o + o[1:-1][::-1]:

            new_frame = ''
            new_frame += ''.join (o[4] for w in range (width)) + '\n'  # Upper line.
            new_frame += ''.join (''.join ([pic, o[4]][w in [0, width-1]] for w in range (width)) + '\n' for h in range (height-2))    # Mediate lines with sides.
            new_frame += ''.join (o[4] for w in range (width)) + '\n'  # Lower line.

            display.update (new_frame)

            time.sleep (1 / updates_fps)  # Note: a dysplay is already updating every FPS. So it is like an upper updates.