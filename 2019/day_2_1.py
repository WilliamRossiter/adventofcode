import fileinput
import math

def ProcessFile():
    with fileinput.input(files=('input/day_2_1.txt')) as f:
        for line in f:
            program = line.split(",")
            i = 0
            while i < len(program):
                opcode = int(program[i])

                print(opcode)
                if opcode == 99:
                    print("done")
                    break
                else:
                    input1 = int(program[i + 1])
                    input2 = int(program[i + 2])
                    output = int(program[i + 3])
                    if opcode == 1:
                        print("add")
                        program[output] = int(program[input1]) + int(program[input2])
                    elif opcode == 2:
                        print("multiply")
                        program[output] = int(program[input1]) * int(program[input2])
                    else:
                        print("error! Got opcode " + opcode)
                        break
                    i += 4
            print(program)

ProcessFile()