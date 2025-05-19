#  
#  There the system main logic hides.
#  For now the system just does blinks.
#  


import time

from main.project_lib import clear_terminal

from main.system_modules.test_blinks import test_blinks

from main.abstractions_converter_model.abstractions_converter_model import abstractions_converter_model


def system ():

    time.sleep (2.5)

    clear_terminal ()
    test_blinks ()