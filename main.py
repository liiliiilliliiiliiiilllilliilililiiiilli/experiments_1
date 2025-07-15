# Main file, the only needed to be executed.


from time import sleep
from params.params import output_mode as mode, output_delay
from components.components import print_space as space, print_separator as separator, print_screen_size as screen_size, execute_and_reinitialize



def main ():

    schemas = range (256)


    space ()
    print ('[system start]')
    space ()
    separator ()
    space ()
    screen_size ()
    space ()
    separator ()
    space ()

    for schema in schemas:

        schema_bin = bin(schema)[2:].rjust(8, '0')
        schema_bin_map = ''.join (f'{bin(i)[2:].rjust(3, '0')} -> {schema_bin[i]}' + (', ' if i else '') for i in range (7, -1, -1))


        print (f'mode: {mode}')
        space ()
        print (f'schema: {schema} | {schema_bin} | {schema_bin_map}')
        space ()
        print ('plot:')
        space ()
        execute_and_reinitialize (schema)
        space ()
        separator ()
        space ()

        sleep (output_delay)  # delay the field plots print (seconds)

    print ('[system end]')
    space ()



main ()