#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time

def type_to_min(type):
    # type => min
    if type.lower() == 'w' or type.lower() == 'work':
        min = 2 # for test
        #min = 25
    elif type.lower() == 'b' or type.lower() == 'break':
        min = 1 # for test
        #min = 5
    else:
        min = 0
    return min

def countdown(min):
    min = 2
    sec = min * 60
    start = time.strftime("%Y-%m-%d %H:%M:%S(%Z)")
    print(f"start;{start}")
    print(f'remain is {sec}sec.')
    while sec > 0:
        time.sleep(1)
        sec -= 1
        disp_min, disp_sec = divmod(sec, 60)
        print(f'remain is {disp_min}:{disp_sec}') # TODO 2ゼロ埋め
    end = time.strftime("%Y-%m-%d %H:%M:%S(%Z)")
    print(f"end;{end}")

# 標準入力トリガで動かす
#min = int(input('countdown min -> '))
type = input('work or break -> ')
min = type_to_min(type)
countdown(min)

#countdown(25)
#countdown(5)
#countdown(25)
#countdown(5)
