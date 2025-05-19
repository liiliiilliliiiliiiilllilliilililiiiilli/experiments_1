import time

from main.project_lib import o
from main import display 


updates_fps = 1


def test_blinks ():

    while 1:

        width, height = display.sizes().values()

        # for pic in o + o[1:-1][::-1]:
        for pic in o[:-2] + o[1:-3][::-1]:
        # for pic in o[:-1] + o[1:-2][::-1]:
        # for pic in (o[1:] + o[2:-1][::-1])[1:] + (o[1:] + o[2:-1][::-1])[0]:  # More smooth not so blinking variant.

            new_frame = ''
            new_frame += ''.join (o[4] for w in range (width)) + '\n'
            new_frame += ''.join (''.join ([pic, o[4]][w in [0, width-1]] for w in range (width)) + '\n' for h in range (height-2))
            new_frame += ''.join (o[4] for w in range (width)) + '\n'

            display.update (new_frame)

            time.sleep (1 / updates_fps)  # Note: a dysplay is already updating every FPS. So it is like an upper updates.