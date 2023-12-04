#Función para obtener los valores de los registros y el valor binario
def registros(instruccion,op,sh,fnc):
    #Registro de destino (rd)
    i=0
    for let in instruccion[1]["value"]:
        if ord(let) >= 48 and ord(let) <= 57 and i == 0:
            c1=let
            rd=c1
            i=i+1
        elif ord(let) >= 48 and ord(let) <= 57 and i != 0:
            c2=let
            rd=c1+c2
    #Registro del primer operando fuente (rs)
    i=0
    for let in instruccion[2]["value"]:
        if ord(let) >= 48 and ord(let) <= 57 and i == 0:
            c1=let
            rs=c1
            i=i+1
        elif ord(let) >= 48 and ord(let) <= 57 and i != 0:
            c2=let
            rs=c1+c2
    #Registro del segundo operando fuente (rt)
    i=0
    for let in instruccion[3]["value"]:
        if ord(let) >= 48 and ord(let) <= 57 and i == 0:
            c1=let
            rt=c1
            i=i+1
        elif ord(let) >= 48 and ord(let) <= 57 and i != 0:
            c2=let
            rt=c1+c2
    rd=int(rd)
    rs=int(rs)
    rt=int(rt)
    rd=format(rd,"b")
    rs=format(rs,"b")
    rt=format(rt,"b")

    return str(op).zfill(6) + rs.zfill(5) + rt.zfill(5) + rd.zfill(5) + str(sh).zfill(5) + str(fnc).zfill(6)

def detect(instr,callback_error):
    instruccion = instr.elements[0]["value"]

    binary = ""
    if instruccion == "add":
        try:
            instr.verify(['instruction','register','register','register'])
        except Exception as ex:
            errstr = "({0}) {1}".format(instr.column,str(ex))
            callback_error(errstr.format(instr.elements[0]["value"]))
            return 'x' * 32
        op=000000
        sh=00000
        fnc=100000
        binary = registros(instr.elements,op,sh,fnc)
    elif instruccion == "and":
        try:
            instr.verify(['instruction','register','register','register'])
        except Exception as ex:
            errstr = "({0}) {1}".format(instr.column,str(ex))
            callback_error(errstr.format(instr.elements[0]["value"]))
            return 'x' * 32
        op=000000
        sh=00000
        fnc=100100
        binary = registros(instr.elements,op,sh,fnc)
    elif instruccion == "nor":
        try:
            instr.verify(['instruction','register','register','register'])
        except Exception as ex:
            errstr = "({0}) {1}".format(instr.column,str(ex))
            callback_error(errstr.format(instr.elements[0]["value"]))
            return 'x' * 32
        op=000000
        sh=00000
        fnc=100111
        binary = registros(instr.elements,op,sh,fnc)
    elif instruccion == "or":
        try:
            instr.verify(['instruction','register','register','register'])
        except Exception as ex:
            errstr = "({0}) {1}".format(instr.column,str(ex))
            callback_error(errstr.format(instr.elements[0]["value"]))
            return 'x' * 32
        op=000000
        sh=00000
        fnc=100101
        binary = registros(instr.elements,op,sh,fnc)
    elif instruccion == "slt":
        try:
            instr.verify(['instruction','register','register','register'])
        except Exception as ex:
            errstr = "({0}) {1}".format(instr.column,str(ex))
            callback_error(errstr.format(instr.elements[0]["value"]))
            return 'x' * 32
        op=000000
        sh=00000
        fnc=101010
        binary = registros(instr.elements,op,sh,fnc)
    elif instruccion == "sub":
        try:
            instr.verify(['instruction','register','register','register'])
        except Exception as ex:
            errstr = "({0}) {1}".format(instr.column,str(ex))
            callback_error(errstr.format(instr.elements[0]["value"]))
            return 'x' * 32
        op=000000
        sh=00000
        fnc=100010
        binary = registros(instr.elements,op,sh,fnc)
    elif instruccion == "nop":
        try:
            instr.verify(['instruction'])
        except Exception as ex:
            errstr = "({0}) {1}".format(instr.column,str(ex))
            callback_error(errstr.format(instr.elements[0]["value"]))
            return 'x' * 32
        return str(0).zfill(32)
    
    return binary
