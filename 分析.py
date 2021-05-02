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
    raise

gachaList = []
gachaRecords = json.loads(open(jsonPath).read())
for i in gachaRecords:
    for p in gachaRecords[i]:
        gachaList.append((i,p['rarity']+1,p['name'],p['isNew']))

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
