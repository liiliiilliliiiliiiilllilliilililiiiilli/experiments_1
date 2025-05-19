#
#  This is Display! Like a real one, but virtual!
#  Initially it stretches to the CLI window sides Jelley lauched on and then showes a desired graphics: ui, games and any interfases built.
#


import os
import time

import configuration


display_stats = {'width': 0, 'height': 0, 'data': ''}  # actually stretched with CLI sizes
is_resize_allowed = True
fps = configuration.display_fps




def set_sizes (width, height):

    display_stats['width'], display_stats['height'] = width, height


def sizes ():

    return {'width': display_stats['width'], 'height': display_stats['height']}


def width ():

    return display_stats['width']


def height ():

    return display_stats['height']


def update (data):

    display_stats['data'] = data


def get ():

    return display_stats['data']


# -----


def subsribe_size_changes ():

    global resize_allowed
    resize_allowed = True


def unsubscribe_size_changes ():

    global resize_allowed
    resize_allowed = False


def resize_allowed ():

    return is_resize_allowed & True


# -----


def activate ():  # the display proccess itself

    while 1:

        if resize_allowed ():

            cli_sizes = list (os.get_terminal_size ())
            set_sizes (cli_sizes[0], cli_sizes[1]-2)

        print (get ())
        time.sleep (1 / fps)