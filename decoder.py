import sys
import type_r as R
import type_i as I
import type_j as J
import little_lexer as Lexer

class Decoder:
    def __init__(self,callback):
        self.callback = callback
        self.errors = []
    
    def add_error(self,error : str):
        print(error)
        self.errors.append(error)

    def get_text_binary(self,instruction):
        if binary_text := R.detect(instruction,self.add_error):
            return binary_text

        if binary_text := I.detect(instruction,self.add_error):
            return binary_text

        if binary_text := J.detect(instruction,self.add_error):
            return binary_text

        return ""


    def text_to_binary(self,str):
        instructions , is_ok = Lexer.getInstructionFromString(str,self.add_error)
        str_out = ""

        if not is_ok:
            return

        for i , instruction in enumerate(instructions):
            text = self.get_text_binary(instruction)

            if not text:
                self.add_error("({0}) The entered instruction isn't supported by the decoder.".format(instruction.column))
            elif len(text) != 32:
                self.add_error("({0}) One assigned value exceeds the capacity.".format(instruction.column))
                return

            str_out += text[0:8] + "\n"
            str_out += text[8:16] + "\n"
            str_out += text[16:24] + "\n"

            if i == len(instructions) - 1:
                str_out += text[24:32]
            else:
                str_out += text[24:32] + "\n"

        
        self.callback(self.errors)
        self.errors.clear()

        return str_out