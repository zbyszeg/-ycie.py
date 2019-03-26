#!/usr/bin/env python3

from board import Board
from effect import Effect
from effect0 import Effect0
from effect1 import Effect1
from effect2 import Effect2
from effect3 import Effect3
from effect4 import Effect4
from effect5 import Effect5
from effect6 import Effect6

boards = [Board(), Board()]

effect: Effect = None
lastD = None
isAssigned: bool = False

while True:
    try:
        numbers = list(map(int, input().split()))
        x = numbers[0]
        y = numbers[1]
        dx = numbers[2]
        dy = numbers[3]
        e = numbers[4]
        d = numbers[5]

        if ((0 <= x <= 15)
                and (0 <= y <= 15)
                and (x <= dx <= 15)
                and (y <= dy <= 15)
                and (0 <= e <= 6)
                and (0 <= d <= 1)):

            if e == 0:
                effect = Effect0(x, y, dx, dy, boards[d], None)
            elif e == 1:
                effect = Effect1(x, y, dx, dy, boards[d], None)
            elif e == 2:
                effect = Effect2(x, y, dx, dy, boards[d], None)
            elif e == 3:
                effect = Effect3(x, y, dx, dy, boards[d], None)
            elif e == 4:
                effect = Effect4(x, y, dx, dy, boards[d], None)
            elif e == 5:
                if d == 0:
                    d2 = 1
                else:
                    d2 = 0
                if not isAssigned:
                    effect_temp = Effect5(x, y, dx, dy, boards[d], boards[d2])
                    effect = effect_temp
                    isAssigned = True
                else:
                    effect = effect_temp
                    isAssigned = False
            elif e == 6:
                if d == 0:
                    d2 = 1
                else:
                    d2 = 0
                effect = Effect6(x, y, dx, dy, boards[d], boards[d2])
            lastD = d
            effect.apply()
    except EOFError:
        print('--koniec--')
        break

if (lastD == 1) or (lastD == 0):
    boards[lastD].display()
