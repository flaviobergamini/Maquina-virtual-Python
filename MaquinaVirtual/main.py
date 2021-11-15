'''
 ----------------------------18 BITS--------------------------------
  Codigo de maquina:
        OpCode               [0  -  3]  -> 3 BITS
        Registro de destino  [4  -  9]  -> 5 BITS
        Registro source 1    [10 - 15]  -> 5 BITS
        Registro source 2    [16 - 21]  -> 5 BITS
        Imediate             [16 - 21]  -> 5 BITS
 -------------------------------------------------------------------
  Instruções do tipo R:
        ADD => op = 000
        [OP] [RD] [RS1] [RS2]

        SUB => op = 001
        [OP] [RD] [RS1] [RS2]
 -------------------------------------------------------------------
  Instruções do tipo I:
        SUBi => op = 010
        [OP] [RD] [RS1] [IMEDIATE]

        ADDi => op = 011
        [OP] [RD] [RS1] [IMEDIATE]
 -------------------------------------------------------------------
 Instruções lógicas:
        AND => op = 100
        [OP] [RD] [RS1] [RS2]

        OR => op = 101
        [OP] [RD] [RS1] [RS2]
 -------------------------------------------------------------------
  10 Registradores:
        $f0
        $f1
        $f2
        $f3
        $f4
        $f5
        $f6
        $f7
        $f8
        $f9
       $PC
 -------------------------------------------------------------------
'''

LENGTH_REGISTERS = 10
ERROR_OP = 0
ERROR_REGISTERS = 1
SUCCESS = 2

registers = []  # lista com no máximo 10 registradores de $f0 à $f9

MNEMONICS = ["ADD", "SUB", "SUBi", "ADDi", "AND", "OR"]

REGISTERS = ["$f0", "$f1", "$f2", "$f3", "$f4", "$f5", "$f6", "$f7", "$f8", "$f9"]

ERRORS_MSG = ["ERROR -> OpCode Nao conhecido!", "ERROR -> Registrador nao existente!"]

class boby_instruction(object):  # instruction_execute

    def __init__(self):
        self.op = None
        self.op = None
        self.rd = None
        self.rs1 = None
        self.rs2 = None
        self.imediate = None

instruction_execute = boby_instruction()

def fetch(instructions, pc):
    return (instructions + pc)

def decode(instruction):
    instruction_execute.op = (instruction & 0x38000) >> 15
    instruction_execute.rd = (instruction & 0x7C00) >> 10
    instruction_execute.rs1 = (instruction & 0x03E0) >> 5

    if instruction_execute.op % 2 != 0:
        instruction_execute.imediate = (instruction & 0x001F)
    else:
        instruction_execute.rs2 = (instruction & 0x001F)

    if instruction_execute.op > 6:  # Se o opcode ultrapassar o limite de instruções
        print('Erro de OPCODE')
        return ERROR_OP  # Retorna 0 para a mensagem de erro de opcode

    if instruction_execute.rd > 6 or instruction_execute.rs1 > 6 or instruction_execute.rs2 > 6:
        print(instruction_execute.rd, instruction_execute.rs1, instruction_execute.rs2)
        print('Erro de registrador')
        return ERROR_REGISTERS  # Retorna 1 para a mensagem de erro de registro

    return SUCCESS # Retorna 2 para o sucesso da operação


def instructionExecute(op, rd, rs1, rs2, IM=False):
    print(f"Instruction -> {MNEMONICS[op]} {REGISTERS[rd]} {REGISTERS[rs1]} ", end="")
    if IM:
        print(rs2)
    else:
        print(REGISTERS[rs2])


def printRegister(name, reg, IM=False):
    print(f'{name} -> {bin(reg).replace("0b", "")}: ', end='')
    if IM:
        print(reg)
    else:
        print(f'{REGISTERS[reg]} = {registers[reg]}')


def execute():
    if instruction_execute.op == 0:  # ADD

        instructionExecute(instruction_execute.op, instruction_execute.rd, instruction_execute.rs1,
                           instruction_execute.rs2)

        print(f"Opcode: {bin(instruction_execute.op).replace('0b', '')}")

        print("Registros Antes: ")
        printRegister("RD", instruction_execute.rd)
        printRegister("RS1", instruction_execute.rs1)
        printRegister("RS2", instruction_execute.rs2)

        registers[instruction_execute.rd] = registers[instruction_execute.rs1] + registers[instruction_execute.rs2]

        print("\nRegistros Depois: ")
        printRegister('RD', instruction_execute.rd)
        print('-='*30)

    elif instruction_execute.op == 1:  # SUB
        instructionExecute(instruction_execute.op, instruction_execute.rd, instruction_execute.rs1,
                           instruction_execute.rs2)
        print(f"Opcode: {bin(instruction_execute.op).replace('0b', '')}\n")

        print("Registros Antes: ")
        printRegister("RD", instruction_execute.rd)
        printRegister("RS1", instruction_execute.rs1)
        printRegister("RS2", instruction_execute.rs2)

        registers[instruction_execute.rd] = registers[instruction_execute.rs1] - registers[instruction_execute.rs2]

        print("\nRegistros Depois: ")
        printRegister('RD', instruction_execute.rd)
        print('-=' * 30)

    elif instruction_execute.op == 2:  # SUBi
        instructionExecute(instruction_execute.op, instruction_execute.rd, instruction_execute.rs1,
                           instruction_execute.imediate, True)

        print(f"Opcode: {bin(instruction_execute.op).replace('0b', '')}\n")

        print("Registros Antes: ")
        printRegister("RD", instruction_execute.rd)
        printRegister("RS1", instruction_execute.rs1)
        printRegister("IMEDIATE", instruction_execute.imediate, True)

        registers[instruction_execute.rd] = registers[instruction_execute.rs1] - instruction_execute.imediate

        print("\nRegistros Depois: ")
        printRegister('RD', instruction_execute.rd)
        print('-=' * 30)

    elif instruction_execute.op == 3:  # ADDi
        instructionExecute(instruction_execute.op, instruction_execute.rd, instruction_execute.rs1,
                           instruction_execute.imediate, True)

        print(f"Opcode: {bin(instruction_execute.op).replace('0b', '')}\n")

        print("Registros Antes: ")
        printRegister("RD", instruction_execute.rd)
        printRegister("RS1", instruction_execute.rs1)
        printRegister("IMEDIATE", instruction_execute.imediate, True)

        registers[instruction_execute.rd] = registers[instruction_execute.rs1] + instruction_execute.imediate

        print("\nRegistros Depois: ")
        printRegister('RD', instruction_execute.rd)
        print('-=' * 30)

    elif instruction_execute.op == 4:  # AND

        instructionExecute(instruction_execute.op, instruction_execute.rd, instruction_execute.rs1,
                           instruction_execute.rs2)

        print(f"Opcode: {bin(instruction_execute.op).replace('0b', '')}")

        print("Registros Antes: ")
        printRegister("RD", instruction_execute.rd)
        printRegister("RS1", instruction_execute.rs1)
        printRegister("RS2", instruction_execute.rs2)

        registers[instruction_execute.rd] = registers[instruction_execute.rs1] and registers[instruction_execute.rs2]

        print("\nRegistros Depois: ")
        printRegister("RD", instruction_execute.rd)
        print('-=' * 30)

    elif instruction_execute.op == 5:  # OR

        instructionExecute(instruction_execute.op, instruction_execute.rd, instruction_execute.rs1,
                           instruction_execute.rs2)

        print(f"Opcode: {bin(instruction_execute.op).replace('0b', '')}")

        print("Registros Antes: ")
        printRegister("RD", instruction_execute.rd)
        printRegister("RS1", instruction_execute.rs1)
        printRegister("RS2", instruction_execute.rs2)

        registers[instruction_execute.rd] = registers[instruction_execute.rs1] or registers[instruction_execute.rs2]

        print("\nRegistros Depois: ")
        printRegister("RD", instruction_execute.rd)
        print('-=' * 30)

    else:
        print('OPCODE não conhecido')


def clearInstruction(body_instruction):
    body_instruction.op = -1
    body_instruction.rd = -1
    body_instruction.rs1 = -1
    body_instruction.imediate = -1
    body_instruction.rs2 = -1

def initRegisters():
    for i in range(LENGTH_REGISTERS):
        registers.append(i)

'''
-------------------------------------------------------------------
MÁSCARA OP   MÁSCARA RD    MÁSCARA RS1    MÁSCARA RS2
  0x38000      0x7C00       0x03E0          0x001F
  
             OP   RD   RS1  RS2        Instrucao:          
  65 	 -> 000 00000 00010 00001       ADD                    
  39076  -> 001 00110 00101 00100       SUB

             OP   RD   RS1  IMEDIATO
  69729  -> 010 00100 00011 00001       SUBi
  98400  -> 011 00000 00011 00000       ADDi

             OP   RD   RS1  RS2
  131168 -> 100 00000 00011 00000      AND
  168033 -> 101 00100 00011 00001       OR
-------------------------------------------------------------------
'''

if __name__ == "__main__":
    print('#'*30, 'Arquitetura AFGL', '#'*30)
    instructions = [65, 39076, 69729, 98400, 131168, 168033]
    IR = []
    pc = 0

    initRegisters()
    clearInstruction(instruction_execute)

    while pc < len(instructions):
        IR.append(fetch(instructions[pc], pc))
        res = decode(IR[pc])

        if res == ERROR_OP:
            ERRORS_MSG[ERROR_OP]
        elif res == ERROR_REGISTERS:
            ERRORS_MSG[ERROR_REGISTERS]
        elif res == SUCCESS:
            execute()

        print()
        pc += 1

    print('#'*15, 'Registradores', '#'*15)
    print(f'{"-"*14}+{"-"*7}')
    print(f' Resgistrador | Valor ')
    print(f'{"-" * 14}+{"-" * 7}')
    for i in range(LENGTH_REGISTERS):
        print(f"     f{i}       | {registers[i]}     ")
    print(f'{"-" * 14}+{"-" * 7}')



