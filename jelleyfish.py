#  
#  Hello! This is Jelley - a project i suddenly decided to create.
#  It would be a high-level computer system with things i have always wanted to have.
#  Soon i will add more functionalities. It will be cool!
#  
#  | ░▒▓█|
#  
#  🪼
#  

#  
#  This file is a startpoint. Activates Jelley's asynchronic threads.
#  


from threading import Thread
from filling.display import activate as activale_display
from filling.main import main


display_process = Thread (target = activale_display)
main_process = Thread (target = main)

display_process.start ()
main_process.start ()