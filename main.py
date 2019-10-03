#!/usr/bin/env python3

from effect import Board, Effect, Effect0, Effect1, Effect2, Effect3, Effect4, Effect5, Effect6

boards = [Board(), Board()]

my_effect: Effect = None
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
                my_effect = Effect0(x, y, dx, dy, boards[d], None)
            elif e == 1:
                my_effect = Effect1(x, y, dx, dy, boards[d], None)
            elif e == 2:
                my_effect = Effect2(x, y, dx, dy, boards[d], None)
            elif e == 3:
                my_effect = Effect3(x, y, dx, dy, boards[d], None)
            elif e == 4:
                my_effect = Effect4(x, y, dx, dy, boards[d], None)
            elif e == 5:
                if d == 0:
                    d2 = 1
                else:
                    d2 = 0
                if not isAssigned:
                    effect_temp = Effect5(x, y, dx, dy, boards[d], boards[d2])
                    my_effect = effect_temp
                    isAssigned = True
                else:
                    my_effect = effect_temp
                    isAssigned = False
            elif e == 6:
                if d == 0:
                    d2 = 1
                else:
                    d2 = 0
                my_effect = Effect6(x, y, dx, dy, boards[d], boards[d2])
            lastD = d
            my_effect.apply()
    except EOFError:
        break

if (lastD == 1) or (lastD == 0):
    boards[lastD].display()
