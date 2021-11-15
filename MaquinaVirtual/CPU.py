
class boby_instruction(object):  # instruction_execute
    def __init__(self):
        self.op = None
        self.op = None
        self.rd = None
        self.rs1 = None
        self.rs2 = None
        self.imediate = None

class AFGL(object):
    def __init__(self):
        self.instruction_execute = boby_instruction()
        self.LENGTH_REGISTERS = 10
        self.ERROR_OP = 0
        self.ERROR_REGISTERS = 1
        self.SUCCESS = 2
        self.registers = []  # lista com no máximo 10 registradores de $f0 à $f9

        self.MNEMONICS = ["ADD", "SUB", "SUBi", "ADDi", "AND", "OR"]

        self.REGISTERS = ["$f0", "$f1", "$f2", "$f3", "$f4", "$f5", "$f6", "$f7", "$f8", "$f9"]

        self.ERRORS_MSG = ["ERROR -> OpCode Nao conhecido!", "ERROR -> Registrador nao existente!"]

    def fetch(self, instructions, pc):
        return (instructions + pc)

    def decode(self, instruction):
        self.instruction_execute.op = (instruction & 0x38000) >> 15
        self.instruction_execute.rd = (instruction & 0x7C00) >> 10
        self.instruction_execute.rs1 = (instruction & 0x03E0) >> 5

        if self.instruction_execute.op % 2 != 0:
            self.instruction_execute.imediate = (instruction & 0x001F)
        else:
            self.instruction_execute.rs2 = (instruction & 0x001F)

        if self.instruction_execute.op > 6:                       # Se o opcode ultrapassar o limite de instruções
            print('Erro de OPCODE')
            return self.ERROR_OP                                  # Retorna 0 para a mensagem de erro de opcode

        if self.instruction_execute.rd > 6 or self.instruction_execute.rs1 > 6 or self.instruction_execute.rs2 > 6:
            print(self.instruction_execute.rd, self.instruction_execute.rs1, self.instruction_execute.rs2)
            print('Erro de registrador')
            return self.ERROR_REGISTERS                           # Retorna 1 para a mensagem de erro de registro

        return self.SUCCESS                                       # Retorna 2 para o sucesso da operação

    def instructionExecute(self, op, rd, rs1, rs2, IM=False):
        print(f"Instruction -> {self.MNEMONICS[op]} {self.REGISTERS[rd]} {self.REGISTERS[rs1]} ", end="")
        if IM:
            print(rs2)
        else:
            print(self.REGISTERS[rs2])

    def printRegister(self, name, reg, IM=False):
        print(f'{name} -> {bin(reg).replace("0b", "")}: ', end='')
        if IM:
            print(reg)
        else:
            print(f'{self.REGISTERS[reg]} = {self.registers[reg]}')

    def execute(self):
        if self.instruction_execute.op == 0:  # ADD

            self.instructionExecute(self.instruction_execute.op, self.instruction_execute.rd,
                                    self.instruction_execute.rs1, self.instruction_execute.rs2)

            print(f"Opcode: {bin(self.instruction_execute.op).replace('0b', '')}")

            print("Registros Antes: ")
            self.printRegister("RD", self.instruction_execute.rd)
            self.printRegister("RS1", self.instruction_execute.rs1)
            self.printRegister("RS2", self.instruction_execute.rs2)

            self.registers[self.instruction_execute.rd] = self.registers[self.instruction_execute.rs1] + \
                                                          self.registers[self.instruction_execute.rs2]

            print("\nRegistros Depois: ")
            self.printRegister('RD', self.instruction_execute.rd)
            print('-=' * 30)

        elif self.instruction_execute.op == 1:  # SUB
            self.instructionExecute(self.instruction_execute.op, self.instruction_execute.rd,
                                    self.instruction_execute.rs1, self.instruction_execute.rs2)
            print(f"Opcode: {bin(self.instruction_execute.op).replace('0b', '')}\n")

            print("Registros Antes: ")
            self.printRegister("RD", self.instruction_execute.rd)
            self.printRegister("RS1", self.instruction_execute.rs1)
            self.printRegister("RS2", self.instruction_execute.rs2)

            self.registers[self.instruction_execute.rd] = self.registers[self.instruction_execute.rs1] - \
                                                          self.registers[self.instruction_execute.rs2]

            print("\nRegistros Depois: ")
            self.printRegister('RD', self.instruction_execute.rd)
            print('-=' * 30)

        elif self.instruction_execute.op == 2:  # SUBi
            self.instructionExecute(self.instruction_execute.op, self.instruction_execute.rd,
                                    self.instruction_execute.rs1, self.instruction_execute.imediate, True)

            print(f"Opcode: {bin(self.instruction_execute.op).replace('0b', '')}\n")

            print("Registros Antes: ")
            self.printRegister("RD", self.instruction_execute.rd)
            self.printRegister("RS1", self.instruction_execute.rs1)
            self.printRegister("IMEDIATE", self.instruction_execute.imediate, True)

            self.registers[self.instruction_execute.rd] = self.registers[self.instruction_execute.rs1] - \
                                                          self.instruction_execute.imediate

            print("\nRegistros Depois: ")
            self.printRegister('RD', self.instruction_execute.rd)
            print('-=' * 30)

        elif self.instruction_execute.op == 3:  # ADDi
            self.instructionExecute(self.instruction_execute.op, self.instruction_execute.rd,
                                    self.instruction_execute.rs1, self.instruction_execute.imediate, True)

            print(f"Opcode: {bin(self.instruction_execute.op).replace('0b', '')}\n")

            print("Registros Antes: ")
            self.printRegister("RD", self.instruction_execute.rd)
            self.printRegister("RS1", self.instruction_execute.rs1)
            self.printRegister("IMEDIATE", self.instruction_execute.imediate, True)

            self.registers[self.instruction_execute.rd] = self.registers[self.instruction_execute.rs1] + \
                                                          self.instruction_execute.imediate

            print("\nRegistros Depois: ")
            self.printRegister('RD', self.instruction_execute.rd)
            print('-=' * 30)

        elif self.instruction_execute.op == 4:  # AND

            self.instructionExecute(self.instruction_execute.op, self.instruction_execute.rd,
                                    self.instruction_execute.rs1, self.instruction_execute.rs2)

            print(f"Opcode: {bin(self.instruction_execute.op).replace('0b', '')}")

            print("Registros Antes: ")
            self.printRegister("RD", self.instruction_execute.rd)
            self.printRegister("RS1", self.instruction_execute.rs1)
            self.printRegister("RS2", self.instruction_execute.rs2)

            self.registers[self.instruction_execute.rd] = self.registers[self.instruction_execute.rs1] and self.registers[
                self.instruction_execute.rs2]

            print("\nRegistros Depois: ")
            self.printRegister("RD", self.instruction_execute.rd)
            print('-=' * 30)

        elif self.instruction_execute.op == 5:  # OR

            self.instructionExecute(self.instruction_execute.op, self.instruction_execute.rd, self.instruction_execute.rs1,
                               self.instruction_execute.rs2)

            print(f"Opcode: {bin(self.instruction_execute.op).replace('0b', '')}")

            print("Registros Antes: ")
            self.printRegister("RD", self.instruction_execute.rd)
            self.printRegister("RS1", self.instruction_execute.rs1)
            self.printRegister("RS2", self.instruction_execute.rs2)

            self.registers[self.instruction_execute.rd] = self.registers[self.instruction_execute.rs1] or \
                                                          self.registers[self.instruction_execute.rs2]

            print("\nRegistros Depois: ")
            self.printRegister("RD", self.instruction_execute.rd)
            print('-=' * 30)

        else:
            print('OPCODE não conhecido')

    def clearInstruction(self, body_instruction):
        body_instruction.op = -1
        body_instruction.rd = -1
        body_instruction.rs1 = -1
        body_instruction.imediate = -1
        body_instruction.rs2 = -1

    def initRegisters(self):
        for i in range(self.LENGTH_REGISTERS):
            self.registers.append(i)
