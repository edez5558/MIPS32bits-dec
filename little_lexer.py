class Instruction:
    __all__ = ['isEmpty','verify']

    def read_number(self):
        try:
            while self.line[self.next_index].isnumeric():
                self.next_index += 1
        except IndexError as e:
            return
        
    
    def read_instruction(self):
        try:
            while self.line[self.next_index].isalpha():
                self.next_index += 1
        except IndexError as e:
            return

    def read_label(self):
        try:
            while self.line[self.next_index].isalpha() or self.line[self.next_index].isnumeric():
                self.next_index += 1
        except IndexError as e:
            return


    def __init__(self,line,column,valid_instr,label_dictionary):
        self.elements = []
        self.next_index = 0
        self.line = line

        current = ''

        save = {}
        previous_save = {}

        self.column = column + 1

        first =  True
        self.is_correct = True
        while self.next_index < len(line):
            current = line[self.next_index]
            self.next_index += 1

            if current.isspace(): #Ignorar espacios vacios
                continue

            if current == '/':
                break
            
            if save: #Guardar valor?
                if current == ',' and not previous_save:
                    self.elements.append(save)
                    save = {}
                    continue
                elif current == '(' and not previous_save:
                    previous_save = save
                    save = {}
                    continue
                elif current == ')' and previous_save:
                    self.elements.append(save) 
                    self.elements.append(previous_save) 

                    save = {}
                    previous_save= {}
                    continue
                elif current == ':':
                    if not save["value"] in label_dictionary:
                        label_dictionary[save["value"]] = valid_instr
                    else:
                        print("({0},{1}) la etiqueta '{2}' ya habia sido especificada".format(self.column,self.next_index - (len(save["value"])),save["value"]))
                        self.is_correct = False
                    save = {}
                    continue
                elif first:
                    self.elements.append(save)
                    first = False
                else:
                    self.is_correct = False
                    print("({0},{1}) caracter inesperado: ".format(self.column,self.next_index - 1),current)
                    break
            
            if current.isnumeric() or current == '-' or current == '#': #Leer un numero
                data = current

                if current == '#':
                    data = line[self.next_index]
                    self.next_index += 1;

                previous_index = self.next_index
                self.read_number()

                data += line[previous_index:self.next_index]
                save = {"value":data,"type":"immediate"}
            elif current.isalpha() and first: #Leer la instruccion
                data = current

                previous_index = self.next_index
                self.read_label()

                data += line[previous_index:self.next_index]
                save = {"value":data,"type":"instruction"}
            elif current.isalpha() and not first: #Leer una label
                data = current

                previous_index = self.next_index
                self.read_label()

                data += line[previous_index:self.next_index]
                save = {"value":data,"type":"label"}
            elif current == '$': #Leer registro
                data = ""

                previous_index = self.next_index
                self.read_number()

                data += line[previous_index:self.next_index]
                save = {"value":data,"type":"register"}
            else:
                self.is_correct = False
                print("({0},{1}) caracter inesperado: ".format(self.column,self.next_index - 1),current)


        if save:
            self.elements.append(save)

    def verify(self,grammar):
        for element in self.elements:
            print("a")
    def isEmpty(self):
        return len(self.elements) == 0

def labelToImmediate(instructions,label_dictionary):
    for from_index,instr in enumerate(instructions):
        #Obtener los indices de los elementos en la instruccion que sean una label
        indexes = [i for i, element in enumerate(instr.elements) if element["type"]=="label"]

        for index in indexes:
            element = instr.elements[index]
            instruction = instr.elements[0]["value"]

            try:
                to_index = label_dictionary[element["value"]]
            except KeyError as e:
                print("({0}) La etiqueta '{1}' no esta definida".format(instr.column,element["value"]))
                return False
            if(instruction == "beq" or instruction == "bne" or instruction == "bgtz"):
                offset = to_index  - (from_index + 1)
                element["value"] = str(offset)
            else:
                element["value"] = str(to_index)
            
            element["type"] = "immediate"
        
    return True

def getInstructionsFrom(file):
    instructions = []
    label_dictionary = {}

    try:
        file_input = open(file,"r")
    except FileNotFoundError as e:
        print(e)
        is_ok = False
        return instructions, is_ok

    valid_instr = 0
    is_ok = True
    for column,line in enumerate(file_input):
        instr = Instruction(line.lower(),column,valid_instr,label_dictionary)

        if not instr.isEmpty():
            print(instr.elements)
            instructions.append(instr)
            valid_instr += 1

            if not instr.is_correct:
                is_ok = False
        

    file_input.close()

    print(label_dictionary)
    labelToImmediate(instructions,label_dictionary)

    return instructions, is_ok
