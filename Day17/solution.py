reg_A = 729
reg_B, reg_C = 0, 0

instruction = [0,1,5,4,3,0]

def get_operand(num, type):
    #type 0 = literal, type 1 = combo
    if(type):
        match(num):
            case 0 | 1 | 2 | 3:
                return num
            case 4:
                return reg_A
            case 5:
                return reg_B
            case 6: 
                return reg_C
            case 7: 
                return None
    else:
        return num

def performoperation(op, num):
    match op:
        case 0: 
            numerator = reg_A
            operand = get_operand(num, 1)
            deno = 2**operand
            reg_A = numerator//deno
            return ("", i+2)
        case 1:
            operand = get_operand(num, 0)
            reg_B = reg_B ^ operand
            return ("", i+2)
        case 3:
            operand = get_operand(num, 1)
            reg_B = operand%8
            return ("", i+2)
        case 4:
            operand = get_operand(num, 0)  # Literal operand
            if reg_A != 0:  # Jump only if reg_A is not zero
                return ("", operand - i)  # Set i directly to operand
            return ("", 2)


def simulate(instructions):
    i = 0