#ps=平时成绩，qm=期末成绩，pszy=平时作业,kq=考勤成绩;wc=网络测试等级
#sjbg= 实践报告
import csv
import pandas as pd
list_total = []  #存储输出
def score_cal(ps,qm,wc):
    if (wc > 0 and wc <= 3):
        rank = 1
    elif (wc >= 4 and wc <= 7):
        rank = 2
    elif (wc >= 8 and wc <= 10):
        rank = 3
    else:
        rank = 4
    #print(rank)    #算出考勤和平时的差

    kq = ps - rank  #算考勤成绩

    pszy = (ps - 0.333 * kq) / 0.667  #pszy=平时作业
    if((pszy % 1) >= 0.5):
        pszy = pszy - (pszy % 1) + 1
    else:
        pszy = pszy - (pszy % 1)
    #print(pszy)

    zswc = 72 + 2 * wc # zswc=真实网络测试
    #print(zswc)
    sjbg = (qm - (3/11) * zswc) / (8/11)
    if((sjbg % 1) >= 0.5):
        sjbg = sjbg - (sjbg % 1) + 1
    else:
        sjbg = sjbg - (sjbg % 1)
    #print(sjbg)

    list_sc = [kq,pszy,zswc,sjbg]
    #print(list_sc)    #每次计算出的输出数据
    list_total.append(list_sc)
    print(list_total)

csv_reader = open('C:/Users/zhengyong/Desktop/1.csv')
list = []   #csv中的总数据
for row in csv_reader:
    #print(row)
    #print(row[0],row[1],row[3],row[4],row[6])
    #print(int(row[0]),int(row[1]),int(row[3]),int(row[4]),int(row[6]))
    PS = 10 * (int(row[0])) + int(row[1])
    QM = 10 * (int(row[3])) + int(row[4])
    WC = int(row[6])
    #print("平时", PS)
    #print("期末", QM)
    #print("等级", WC)
    list.append([PS,QM,WC])

for i in range(0,len(list)):
    #print(list[0])
    PS = list[i][0]
    QM = list[i][1]
    WC = list[i][2]
    score_cal(PS,QM,WC)   #平时，期末，等级
print(list_total)

name = ['kq','ps','zswc','sjbg']
test = pd.DataFrame(columns=name,data=list_total)
test.to_csv('C:/Users/zhengyong/Desktop/2.csv')
print(name)