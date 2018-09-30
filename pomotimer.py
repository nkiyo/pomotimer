#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
import csv

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
    sec = min * 60
    start = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"start;{start}")
    print(f'remain is {sec}sec.')
    while sec > 0:
        time.sleep(1)
        sec -= 1
        disp_min, disp_sec = divmod(sec, 60)
        print(f'remain is {disp_min}:{disp_sec}') # TODO 2ゼロ埋め
    end = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"end;{end}")
    # カウントダウン完了時に通知する
    # 開始時刻、終了時刻をファイルに記録
    save_pomo_log(start, end)

def save_pomo_log(start, end):
    todayStr = time.strftime("%Y-%m-%d")
    logFile = open(f'{todayStr}_pomo.csv', 'w', newline = '')
    logWriter = csv.writer(logFile)
    logWriter.writerow([start, end])
    logFile.close()

# 標準入力トリガで動かす
#min = int(input('countdown min -> '))
type = input('work or break -> ')
min = type_to_min(type)
countdown(min)

