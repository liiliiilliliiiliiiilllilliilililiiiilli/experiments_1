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

from main.display import activate as display
from main.system import system


display_process = Thread (target = display)
system_process = Thread (target = system)

display_process.start ()
system_process.start ()