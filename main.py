from time import sleep


from params.params import mode
from components.components import screen_stats, separator, space, execute_and_reinitialize



def main ():

    rools = range (256)


    screen_stats ()

    for rool in rools:

        rool_bin = bin(rool)[2:].rjust(8, '0')
        rool_bin_map = ''.join (f'{bin(i)[2:].rjust(3, '0')} -> {rool_bin[i]}' + (', ' if i else '') for i in range (7, -1, -1))

        separator ()
        space ()
        print (f'mode: {mode}')
        space ()
        print (f'rule: {rool} ·•· {rool_bin} ·•· {rool_bin_map}')
        space ()
        print ('plot:')
        space ()
        execute_and_reinitialize (rool)
        space ()

        # sleep (0.5)



main ()