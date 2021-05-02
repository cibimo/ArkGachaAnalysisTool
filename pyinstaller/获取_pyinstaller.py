# -*- coding: utf-8 -*-
# @Author  : cibimo
# @Bilibili  : 38238808
import requests, json, os, time

cookiePath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'cookie.txt')
if os.path.exists(cookiePath) == False:
    f = open(cookiePath,'w+')
    f.close()
    input('请在生成的cookie.txt中填入你的cookie')
    input('按回车结束程序')
    exit()

if open(cookiePath).read() == '':
    print('cookie.txt为空')
    input('按回车结束程序')
    exit()

COOKIE = open(cookiePath).read()

def getGachaRecords(page=1):
    global COOKIE
    try:
        print(f"正在获取第 {page} 页")
        return requests.get(f"https://ak.hypergryph.com/user/api/inquiry/gacha?page={page}",headers={'cookie':COOKIE}).json()
    except:
        print('获取失败，请检查cookie是否填写正确')
        input('按回车结束程序')
        exit()

def sortedDict(adict):
    keylist = list(adict)
    for i in keylist:
        i = int(i)
    keylist = sorted(keylist)
    bdict = {}
    for i in keylist:
        bdict[str(i)] = adict[str(i)]
    return bdict

def saveGachaRecores(gachaList):
    jsonPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'gachaRecords.json')
    if os.path.exists(jsonPath) == False or open(jsonPath).read() == '':
        f = open(jsonPath,'w+')
        f.write(json.dumps({},ensure_ascii=False,separators=(',',':')))
        f.close()
    jsonContent = json.loads(open(jsonPath).read())
    for i in gachaList:
        if str(i['ts']) not in jsonContent:
            jsonContent[str(i['ts'])] = i['chars']
        else:
            f = open(jsonPath,'w+')
            f.write(json.dumps(sortedDict(jsonContent),ensure_ascii=False,separators=(',',':')))
            f.close()
            return False
    f = open(jsonPath,'w+')
    f.write(json.dumps(sortedDict(jsonContent),ensure_ascii=False,separators=(',',':')))
    f.close()
    return True

firstPage = getGachaRecords(page=1)['data']
if firstPage['pagination']['total'] == 0:
    print('暂无抽卡记录')
    input('按回车结束程序')
    exit()

# 获取总页数
allPage = divmod(firstPage['pagination']['total'],10)
if allPage[1] != 0:
    allPage = allPage[0] + 1
else:
    allPage = allPage[0]

# 记录数据
if saveGachaRecores(firstPage['list']) == False:
    print('新增成功')
    input('按回车结束程序')
    exit()

for i in range(allPage-1):
    if saveGachaRecores(getGachaRecords(i+2)['data']['list']) == False:
        print('新增成功')
        exit(0)
    time.sleep(0.5)

print('数据不连续，分析报告会不准确（第一次获取除外）')
input('按回车结束程序')
