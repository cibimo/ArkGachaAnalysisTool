# -*- coding: utf-8 -*-
# @Author  : cibimo
# @Bilibili  : 38238808

import json, os

def avgGacha(starNum,gachaList):
    num = 0
    for i in gachaList:
        if i[1] == starNum:
            num += 1
    return "{:.2f}".format(len(gachaList)/num)

def perGacha(starNum,gachaList):
    num = 0
    for i in gachaList:
        if i[1] == starNum:
            num += 1
    return num, "{:.2%}".format(num/len(gachaList))

def accumulativeGacha(starNum,gachaList):
    starRecord = []
    num = 0
    for i in gachaList:
        if i[1] == starNum:
            num += 1
            starRecord.append(f"{i[2]}[{num}]")
            num = 0
        else:
            num += 1
    return num, starRecord

jsonPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'gachaRecords.json')
if os.path.exists(jsonPath) == False or open(jsonPath).read() == '':
    print('还未获取过抽卡数据')
    input('按回车结束程序')
    exit()

gachaList = []
gachaRecords = json.loads(open(jsonPath).read())
for i in gachaRecords:
    for p in gachaRecords[i]:
        gachaList.append((i,p['rarity']+1,p['name'],p['isNew']))

if os.name == 'posix':
    print(f"""
    \033[1;31m总计 {len(gachaList)} 抽\033[0m

    \033[1;35m平均 {avgGacha(5,gachaList)} 抽一个五星\033[0m
    \033[1;33m平均 {avgGacha(6,gachaList)} 抽一个六星\033[0m

    \033[1;35m已累计 {accumulativeGacha(5,gachaList)[0]} 未出五星\033[0m
    \033[1;33m已累计 {accumulativeGacha(6,gachaList)[0]} 未出六星\033[0m

    \033[1;37m三星 {perGacha(3,gachaList)[0]} 占 {perGacha(3,gachaList)[1]}\033[0m
    \033[1;36m四星 {perGacha(4,gachaList)[0]} 占 {perGacha(4,gachaList)[1]}\033[0m
    \033[1;35m五星 {perGacha(5,gachaList)[0]} 占 {perGacha(5,gachaList)[1]}\033[0m
    \033[1;33m六星 {perGacha(6,gachaList)[0]} 占 {perGacha(6,gachaList)[1]}\033[0m

    \033[1;35m五星历史记录: {' '.join(accumulativeGacha(5,gachaList)[1])}\033[0m
    \033[1;33m六星历史记录: {' '.join(accumulativeGacha(6,gachaList)[1])}\033[0m
    """)
elif os.name == 'nt':
    import ctypes,sys

    STD_INPUT_HANDLE = -10
    STD_OUTPUT_HANDLE = -11
    STD_ERROR_HANDLE = -12

    FOREGROUND_BLUE = 0x09 # blue.
    FOREGROUND_GREEN = 0x0a # green.
    FOREGROUND_SKYBLUE = 0x0b # skyblue.
    FOREGROUND_RED = 0x0c # red.
    FOREGROUND_DARKYELLOW = 0x06 # dark yellow.
    FOREGROUND_YELLOW = 0x0e # yellow.
    FOREGROUND_WHITE = 0x0f # white.

    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

    def set_cmd_text_color(color, handle=std_out_handle):
        Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return Bool

    def resetColor():
        set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

    def printSkyBlue(mess):
        set_cmd_text_color(FOREGROUND_SKYBLUE)
        sys.stdout.write(mess+'\n')
        resetColor()

    def printRed(mess):
        set_cmd_text_color(FOREGROUND_RED)
        sys.stdout.write(mess+'\n')
        resetColor()

    def printDarkYellow(mess):
        set_cmd_text_color(FOREGROUND_DARKYELLOW)
        sys.stdout.write(mess+'\n')
        resetColor()

    def printYellow(mess):
        set_cmd_text_color(FOREGROUND_YELLOW)
        sys.stdout.write(mess+'\n')
        resetColor()

    def printWhite(mess):
        set_cmd_text_color(FOREGROUND_WHITE)
        sys.stdout.write(mess+'\n')
        resetColor()

    printRed(f"总计 {len(gachaList)} 抽")
    print()
    printYellow(f"平均 {avgGacha(5,gachaList)} 抽一个五星")
    printDarkYellow(f"平均 {avgGacha(6,gachaList)} 抽一个六星")
    print()
    printYellow(f"已累计 {accumulativeGacha(5,gachaList)[0]} 未出五星")
    printDarkYellow(f"已累计 {accumulativeGacha(6,gachaList)[0]} 未出六星")
    print()
    printWhite(f"三星 {perGacha(3,gachaList)[0]} 占 {perGacha(3,gachaList)[1]}")
    printSkyBlue(f"四星 {perGacha(4,gachaList)[0]} 占 {perGacha(4,gachaList)[1]}")
    printYellow(f"五星 {perGacha(5,gachaList)[0]} 占 {perGacha(5,gachaList)[1]}")
    printDarkYellow(f"六星 {perGacha(6,gachaList)[0]} 占 {perGacha(6,gachaList)[1]}")
    print()
    printYellow(f"五星历史记录: {' '.join(accumulativeGacha(5,gachaList)[1])}")
    printDarkYellow(f"六星历史记录: {' '.join(accumulativeGacha(6,gachaList)[1])}")
else:
    print(f"""
    总计 {len(gachaList)} 抽

    平均 {avgGacha(5,gachaList)} 抽一个五星
    平均 {avgGacha(6,gachaList)} 抽一个六星

    已累计 {accumulativeGacha(5,gachaList)[0]} 未出五星
    已累计 {accumulativeGacha(6,gachaList)[0]} 未出六星

    三星 {perGacha(3,gachaList)[0]} 占 {perGacha(3,gachaList)[1]}
    四星 {perGacha(4,gachaList)[0]} 占 {perGacha(4,gachaList)[1]}
    五星 {perGacha(5,gachaList)[0]} 占 {perGacha(5,gachaList)[1]}
    六星 {perGacha(6,gachaList)[0]} 占 {perGacha(6,gachaList)[1]}

    五星历史记录: {' '.join(accumulativeGacha(5,gachaList)[1])}
    六星历史记录: {' '.join(accumulativeGacha(6,gachaList)[1])}
    """)
print()
input('按回车关闭')
