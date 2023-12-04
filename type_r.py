#Función para obtener los valores de los registros y el valor binario
def registros(instruccion,instruccion2):
    if len(instruccion2) == 3:
        #Registro de destino (rd)
        i=0
        for let in instruccion2[0]:
            if ord(let) >= 48 and ord(let) <= 57 and i == 0:
                c1=let
                rd=c1
                i=i+1
            elif ord(let) >= 48 and ord(let) <= 57 and i != 0:
                c2=let
                rd=c1+c2
        #Registro del primer operando fuente (rs)
        i=0
        for let in instruccion2[1]:
            if ord(let) >= 48 and ord(let) <= 57 and i == 0:
                c1=let
                rs=c1
                i=i+1
            elif ord(let) >= 48 and ord(let) <= 57 and i != 0:
                c2=let
                rs=c1+c2
        #Registro del segundo operando fuente (rt)
        i=0
        for let in instruccion2[2]:
            if ord(let) >= 48 and ord(let) <= 57 and i == 0:
                c1=let
                rt=c1
                i=i+1
            elif ord(let) >= 48 and ord(let) <= 57 and i != 0:
                c2=let
                rt=c1+c2
    else:
        #Registro de destino (rd)
        i=0
        for let in instruccion[1]:
            if ord(let) >= 48 and ord(let) <= 57 and i == 0:
                c1=let
                rd=c1
                i=i+1
            elif ord(let) >= 48 and ord(let) <= 57 and i != 0:
                c2=let
                rd=c1+c2
        #Registro del primer operando fuente (rs)
        i=0
        for let in instruccion[2]:
            if ord(let) >= 48 and ord(let) <= 57 and i == 0:
                c1=let
                rs=c1
                i=i+1
            elif ord(let) >= 48 and ord(let) <= 57 and i != 0:
                c2=let
                rs=c1+c2
        #Registro del segundo operando fuente (rt)
        i=0
        for let in instruccion[3]:
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
    print("\nInstrucción en código binario:\n",str(op).zfill(6),rs.zfill(5), rt.zfill(5), rd.zfill(5), str(sh).zfill(5), str(fnc).zfill(6))

instruccion = input("Ingresa la instrucción tipo R: ")
instruccion = instruccion.lower()
instruccion = instruccion.split(" ")
instruccion2 = instruccion[1].split(",")
if instruccion[0] == "add":
    op=000000
    sh=00000
    fnc=100000
    registros(instruccion,instruccion2)
elif instruccion[0] == "and":
    op=000000
    sh=00000
    fnc=100100
    registros(instruccion,instruccion2)
elif instruccion[0] == "nor":
    op=000000
    sh=00000
    fnc=100111
    registros(instruccion,instruccion2)
elif instruccion[0] == "or":
    op=000000
    sh=00000
    fnc=100101
    registros(instruccion,instruccion2)
elif instruccion[0] == "slt":
    op=000000
    sh=00000
    fnc=101010
    registros(instruccion,instruccion2)
elif instruccion[0] == "sub":
    op=000000
    sh=00000
    fnc=100010
    registros(instruccion,instruccion2)
else:
    print("Instrucción inválida")
