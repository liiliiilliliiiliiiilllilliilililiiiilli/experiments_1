# File of project's components.


from params.params import o, mode, height, width, field, field_initial_state



def schema (l, c, r, type):  # cells' interaction schema

    dests = list (map (int, bin(type)[2:].rjust(8, '0')))


    match l, c, r:

        case 1, 1, 1: return dests[0]
        case 1, 1, 0: return dests[1]
        case 1, 0, 1: return dests[2]
        case 0, 1, 1: return dests[4]
        case 1, 0, 0: return dests[3]
        case 0, 1, 0: return dests[5]
        case 0, 0, 1: return dests[6]
        case 0, 0, 0: return dests[7]



def evolute_line (line, schema_type):

    def schema_cond (index):


        if mode == 'bounded':  # side cells won't interact with each other
        
            if (index == 0):  # left side cell

                return schema (0, line[index], line[index+1], type = schema_type)

            elif (0 < index < len(line)-1):  # inner cells

                return schema (line[index-1], line[index], line[index+1], type = schema_type)

            elif (index == len(line)-1):  # right side cell

                return schema (line[index-1], line[index], 0, type = schema_type)


        elif mode == 'cycled':  # side cells will interact with each other like field is loop

            if (index == 0):  # left side cell

                return schema (line[-1], line[index], line[index+1], type = schema_type)

            elif (0 < index < len(line)-1):  # inner cells

                return schema (line[index-1], line[index], line[index+1], type = schema_type)

            elif (index == len(line)-1):  # right side cell

                return schema (line[index-1], line[index], line[0], type = schema_type)


    return list (map (schema_cond, range (len (line))))



def evolute_field (schema_type):  # evolute field's initial cells step-by-step according to the given interaction schema stacking the resulting lines

    for h in range (height):

        field.append (evolute_line (field[-1], schema_type = schema_type))



def clear_field ():  # wipe field totally

    global field

    field.clear ()



def reinititialize_field ():  # clear field and apply it's initial state

    global field

    field.clear ()
    field.append (field_initial_state)



def print_field ():  # output each field's line

    for line in field:

        print (''.join (map (lambda u: [o[0], o[4]][u], line)))  # translation line



def execute (schema_type):  # output the result of evolution

    evolute_field (schema_type = schema_type)
    print_field ()



def execute_and_reinitialize (schema_type):  # shortcut. output the result of evolution and reinitialize field

    evolute_field (schema_type = rule_type)
    print_field ()
    reinititialize_field ()



def print_screen_size ():

    print (f'virtual screen: {height}h, {width}w')



def print_separator ():

    print ('-' * width)



def print_space ():

    print ()