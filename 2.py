import csv
csv_reader = open('C:/Users/zhengyong/Desktop/1.csv')
list = []
for row in csv_reader:
    #print(row)
    #print(row[0],row[1],row[3],row[4],row[6])
    #print(int(row[0]),int(row[1]),int(row[3]),int(row[4]),int(row[6]))
    PS = 10 * (int(row[0])) + int(row[1])
    QM = 10 * (int(row[3])) + int(row[4])
    WC = int(row[6])
    print("平时", PS)
    print("期末", QM)
    print("等级", WC)
    list.append([PS,QM,WC])
print(len(list))
print(list[0])
print(list)

