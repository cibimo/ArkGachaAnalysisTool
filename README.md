# ArkGachaAnalysisTool
本工具为明日方舟抽卡数据获取分析工具，其功能模仿原神的那个分析工具，但无图形化部分

## 注意事项
本工具在Mac OS下开发，Windows下的print输出可能有问题（shell的颜色代码不知道能不能显示）

## 使用方法
1. 安装python3，并安装requests库
2. clone本仓库
3. 在 https://ak.hypergryph.com/user/inquiryGacha 登录自己的账号，在F12的Network中将 https://ak.hypergryph.com/user/api/inquiry/gacha?page=1 的Cookie放入 获取.py 中的COOKIE变量
4. 运行 一键获取分析.command 即可（非Mac用户可进行 5、6两步
5. 运行 获取.py 脚本会将所有未保存的抽卡记录记录在 gachaRecords.json 中（因为方舟仅保存30天
6. 运行 分析.py 脚本会将保存的抽卡记录进行分析

## 运行示例（我的

正在获取第 1 页
新增成功

总计 289 抽
平均 9.63 抽一个五星
平均 28.90 抽一个六星

已累计 6 未出五星
已累计 0 未出六星

三星 103 占 35.64%
四星 146 占 50.52%
五星 30 占 10.38%
六星 10 占 3.46%

五星历史记录: 蜜蜡[9] 断崖[20] 华法琳[5] 送葬人[14] 拉普兰德[4] 卡夫卡[2] 慑砂[21] 熔泉[1] 慑砂[7] 慑砂[4] 慑砂[10] 熔泉[28] 华法琳[5] 空[13] 极境[17] 月禾[2] 德克萨斯[2] 赤冬[7] 赤冬[7] 幽灵鲨[32] 赤冬[14] 芙兰卡[4] 慑砂[8] 槐琥[14] 絮雨[6] 赤冬[4] 赤冬[15] 赤冬[2] 初雪[2] 惊蛰[4]
六星历史记录: 赫拉格[8] 赫拉格[58] 泥岩[3] 山[17] 安洁莉娜[23] 异客[15] 凯尔希[62] 陈[59] 浊心斯卡蒂[39] 森蚺[5]
