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

from CPU import AFGL, boby_instruction

if __name__ == "__main__":
    afgl = AFGL()
    instruction_execute = boby_instruction()

    print('#'*30, 'Arquitetura AFGL', '#'*30)
    instructions = [65, 39076, 69729, 98400, 131168, 168033]
    IR = []
    pc = 0

    afgl.initRegisters()
    afgl.clearInstruction(instruction_execute)

    while pc < len(instructions):
        IR.append(afgl.fetch(instructions[pc], pc))
        res = afgl.decode(IR[pc])

        if res == afgl.ERROR_OP:
            afgl.ERRORS_MSG[afgl.ERROR_OP]
        elif res == afgl.ERROR_REGISTERS:
            afgl.ERRORS_MSG[afgl.ERROR_REGISTERS]
        elif res == afgl.SUCCESS:
            afgl.execute()

        print()
        pc += 1

    print('#'*15, 'Registradores', '#'*15)
    print(f'{"-"*14}+{"-"*7}')
    print(f' Resgistrador | Valor ')
    print(f'{"-" * 14}+{"-" * 7}')
    for i in range(afgl.LENGTH_REGISTERS):
        print(f"     f{i}       | {afgl.registers[i]}     ")
    print(f'{"-" * 14}+{"-" * 7}')



