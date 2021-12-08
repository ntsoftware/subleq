# SUBLEQ interpreter
# https://esolangs.org/wiki/Subleq
import sys
import msvcrt
with open(sys.argv[1]) as f:
    ram = [int(s) for line in f for s in line.split()]
pc = 0
while pc >= 0:
    a, b, c = ram[pc:pc+3]
    pc += 3
    if a < 0:
        ram[b] += ord(msvcrt.getch())
    elif b < 0:
        print(chr(ram[a]), end='')
    else:
        ram[b] -= ram[a]
        if ram[b] <= 0:
            pc = c
