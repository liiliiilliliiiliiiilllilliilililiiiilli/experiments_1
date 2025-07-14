from params.params import o, mode, height, width, field, field_initial_state



def rule (l, c, r, type):

    dests = list(map(int, bin(type)[2:].rjust(8, '0')))


    match l, c, r:

        case 1, 1, 1: return dests[0]
        case 1, 1, 0: return dests[1]
        case 1, 0, 1: return dests[2]
        case 0, 1, 1: return dests[4]
        case 1, 0, 0: return dests[3]
        case 0, 1, 0: return dests[5]
        case 0, 0, 1: return dests[6]
        case 0, 0, 0: return dests[7]



def evolute_line (line, rule_type):

    def cond_rule (index):


        if mode == 'bounded':  # side cells don't interact with each other
        
            if (index == 0):  # left side cell

                return rule (0, line[index], line[index+1], type = rule_type)

            elif (0 < index < len(line)-1):  # center cells

                return rule (line[index-1], line[index], line[index+1], type = rule_type)

            elif (index == len(line)-1):  # right side cell

                return rule (line[index-1], line[index], 0, type = rule_type)


        elif mode == 'cycled':  # side cells interact with each other like in a loop

            if (index == 0):  # left side cell

                return rule (line[-1], line[index], line[index+1], type = rule_type)

            elif (0 < index < len(line)-1):  # center cells

                return rule (line[index-1], line[index], line[index+1], type = rule_type)

            elif (index == len(line)-1):  # right side cell

                return rule (line[index-1], line[index], line[0], type = rule_type)


    return list(map(cond_rule, range(len(line))))



def evalute_field (rule_type):

    for h in range (height):

        field.append (evolute_line (field[-1], rule_type = rule_type))



def clear_field ():

    global field

    field.clear ()



def reinititialize_field ():

    global field

    field.clear ()
    field.append (field_initial_state)



def print_field ():

    for line in field:

        line_symbols = ''

        for u in line:

            match u:

                case 0: line_symbols += (o[0])
                case 1: line_symbols += (o[4])

        print (line_symbols)



def execute (rule_type):

    evalute_field (rule_type = rule_type)
    print_field ()



def execute_and_reinitialize (rule_type):

    evalute_field (rule_type = rule_type)
    print_field ()
    reinititialize_field ()



def screen_stats ():

    print (f'width: {width}, height: {height}')



def separator ():

    print ('-' * width)



def space ():

    print ()