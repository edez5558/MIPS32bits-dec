import sys
import type_r as R
import type_i as I
import type_j as J
import little_lexer as Lexer

print('Argument List', str(sys.argv))

def error_handler(error):
    print(error)

def get_text_binary(instruction):
    if binary_text := R.detect(instruction,error_handler):
        return binary_text

    if binary_text := I.detect(instruction,error_handler):
        return binary_text

    if binary_text := J.detect(instruction,error_handler):
        return binary_text
    
    return ""


def main():
    if len(sys.argv) < 3:
        print("Se necesitan dos argumentos: el archivo de entrada y de salida")
        print("Ejemplo: main.py archivo_entrada.extension archivo_salida.extension")

        return

    name_input = sys.argv[1]
    name_output = sys.argv[2]

    instructions , is_ok = Lexer.getInstructionsFrom(name_input,error_handler)

    if not is_ok:
        return

    file_output = open(name_output,"w")

    for i , instruction in enumerate(instructions):
        text = get_text_binary(instruction)

        if len(text) != 32:
            print("({0}) Un valor esta fuera de rango".format(instruction.column))
            return

        file_output.write(text[0:8] + "\n")
        file_output.write(text[8:16] + "\n")
        file_output.write(text[16:24] + "\n")

        if i == len(instructions) - 1:
            file_output.write(text[24:32])
        else:
            file_output.write(text[24:32] + "\n")

    file_output.close()

main()
