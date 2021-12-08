# SUBLEQ interpreter
# https://esolangs.org/wiki/Subleq
import sys
import msvcrt
with open(sys.argv[1]) as f:
    ram = [int(s) for line in f for s in line.split()]
ip = 0
while ip >= 0:
    a, b, c = ram[ip:ip+3]
    if a < 0:
        x = ord(msvcrt.getch())
    else:
        x = ram[a]
    if b < 0:
        print(chr(x), end='')
    else:
        ram[b] -= x
    ip = c if b >= 0 and ram[b] <= 0 else ip+3
