#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
import csv
import sys

hasCanceled = False

class pycolor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'

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

def handle_input_cmd(cmd):
    if cmd.lower() == 'c' or cmd.lower() == 'cancel':
        global hasCanceled
        hasCanceled = True
    elif cmd.lower() == 'r' or cmd.lower() == 'resume':
        # 何もせずに処理を再開
        return
    elif cmd.lower() == 'e' or cmd.lower() == 'exit':
        sys.exit()
    else:
        return

def sec_to_mmss(sec):
    disp_min, disp_sec = divmod(sec, 60)
    return f'{str(disp_min).zfill(2)}:{str(disp_sec).zfill(2)}'

def countdown(min):
    # min(秒)カウントダウン
    sec = min * 60
    start = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{pycolor.GREEN}start at {start}{pycolor.END}")
    print(sec_to_mmss(sec), end = "\r")

    while sec > 0:
        try:
            time.sleep(1)
            sec -= 1
            print(sec_to_mmss(sec), end = "\r")
        except KeyboardInterrupt:
            cmd = input('Input.\n  - cancel\n  - resume\n  - exit\n=> ')
            handle_input_cmd(cmd)

            global hasCanceled
            if hasCanceled == True:
                hasCanceled = False
                break

    end = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{pycolor.RED}end at {end}{pycolor.END}")

    # カウントダウン完了時に派手に通知する TODO

    # 開始時刻、終了時刻をファイルに記録
    save_pomo_log(start, end)

def save_pomo_log(start, end):
    todayStr = time.strftime("%Y-%m-%d")
    logFile = open(f'{todayStr}_pomo.csv', 'a', newline = '')
    logWriter = csv.writer(logFile)
    logWriter.writerow([start, end])
    logFile.close()

while True:
    type = input('work or break -> ')
    min = type_to_min(type)
    countdown(min)

