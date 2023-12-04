permitted_instructions = ["j"]
instructions_opcode = ["000010"]

def tobinary(strnumber,maxlenght):
    integer = int(strnumber)
    if integer < 0:
        return bin(((1 << maxlenght) - 1) & integer)[2:]
    else:
        return format(int(strnumber),"b").zfill(maxlenght)

def detect(instr):
    instruction = instr.elements[0]["value"]

    #J INDEX [opcode,rs,rt,immediate] J 5

    try:
        index = permitted_instructions.index(instruction)
    except ValueError as e:
        return ""

            #opcode                          index
    return instructions_opcode[index] + tobinary(instr.elements[1]["value"],26)
