from little_lexer import Instruction

permitted_instructions = ["addi","ori","andi","lw","sw","beq","bne","bgtz","slti"]
#SUBI no tiene opcode lol
instructions_opcode    = ["001000","001101","001100","100011","101011","000100","000101","000111","001010"]

def tobinary(strnumber,maxlenght):
    try:
        integer = int(strnumber)
    except:
        return 'x' * maxlenght

    if integer < 0:
        return bin(((1 << maxlenght) - 1) & integer)[2:]
    else:
        return format(int(strnumber),"b").zfill(maxlenght)

def detect(instr : Instruction, callback_error):
    instruction = instr.elements[0]["value"]

    #ADDI rt, rs, immediate [opcode,rs,rt,immediate] addi $0, $1, -8
    #ORI  rt, rs, immediate [opcode,rs,rt,immediate] ori  $0, $2, 250
    #ANDI rt, rs, immediate [opcode,rs,rt,immediate] andi $0, $2, 250
    #SLTI rt, rs, immediate [opcode,rs,rt,immediate] slti $0, $2, 250
    #LW   rt, offset(base) [opcode,base,rt,offset] lw $0, 4($1)
    #SW   rt, offset(base) [opcode,base,rt,offset] sw $0, 4($1)
    #BEQ  rs, rt, offset   [opcode,rs,rt,offset] beq $0, $1, LABEL
    #BNE  rs, rt, offset   [opcode,rs,rt,offset] bne $0, $1, LABEL
    #BGTZ rs, offset [opcode,rs,00000,offset]

    try:
        index = permitted_instructions.index(instruction)
    except ValueError as e:
        return ""

    if instruction == "bgtz":
        try:
            instr.verify(['instruction','register','immediate'])
        except Exception as ex:
            errstr = "({0}) {1}".format(instr.column,str(ex))
            callback_error(errstr.format(instr.elements[0]["value"]))
            return 'x' * 32

        #bgtz solo tiene 2 parametros
        return instructions_opcode[index] + tobinary(instr.elements[1]["value"]) + tobinary("0",5) + tobinary(instr.elements[2]["value"],16)

    try:
        instr.verify(['instruction','register','register','immediate'])
    except Exception as ex:
        errstr = "({0}) {1}".format(instr.column,str(ex))
        callback_error(errstr.format(instr.elements[0]["value"]))
        return 'x' * 32

    if instruction == "beq" or instruction == "bne":
       
        #beq y bne tienen diferente posicion para el rs y rt
                #opcode                        rs                                              rt                                   immediate
        return instructions_opcode[index] + tobinary(instr.elements[1]["value"],5) + tobinary(instr.elements[2]["value"],5) + tobinary(instr.elements[3]["value"],16)

            #opcode                        rs                                              rt                                   immediate
    return instructions_opcode[index] + tobinary(instr.elements[2]["value"],5) + tobinary(instr.elements[1]["value"],5) + tobinary(instr.elements[3]["value"],16)
