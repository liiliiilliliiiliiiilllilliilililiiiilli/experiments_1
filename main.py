# Main file, the only needed to be executed.


from time import sleep


from params.params import mode, output_delay
from components.components import print_screen_size as screen_size, print_separator as separator, print_space as space, execute_and_reinitialize



def main ():

    rules = range (256)

    space ()
    screen_size ()
    space ()

    for rule in rules:

        rule_bin = bin(rule)[2:].rjust(8, '0')
        rule_bin_map = ''.join (f'{bin(i)[2:].rjust(3, '0')} -> {rule_bin[i]}' + (', ' if i else '') for i in range (7, -1, -1))

        separator ()
        space ()
        print (f'mode: {mode}')
        space ()
        print (f'rule: {rule}  |  {rule_bin}  |  {rule_bin_map}')
        space ()
        print ('plot:')
        space ()
        execute_and_reinitialize (rule)
        space ()

        sleep (output_delay)  # delay the field plots print (seconds)



main ()