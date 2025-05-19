#  
#  There the system main logic hides.
#  For now the system just does blinks.
#  


import time

import configuration
from main.project_lib import clear_terminal
from main.system_modules.test_blinks import test_blinks
from main.abstractions_converter_model.abstractions_converter_model import abstractions_converter_model


def system ():

    time.sleep (configuration.time_sleep_before_system_start)

    clear_terminal ()
    test_blinks ()  # <-- Place where all system's logic connects.