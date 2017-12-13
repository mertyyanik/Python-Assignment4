import sys
import math
command = open('commands','r')
parametre = sys.argv[1]
dic = {}
dic2 = {}
dic3 = {}
liste3 = []
send = {}
move = {}
chbttry = {}
rmnode = ""

read = command.readline()
while read != "":
    liste = read.split("\t")
    if liste[0] == '0':
        if liste[1] == 'CRNODE':
            dic[liste[2]] = liste[3].split(';')
            liste2 = liste[4].split(';')
            dic2[liste[2]] = liste2
        elif liste[1] == 'SEND':
            send[liste[2]] = liste[3]
        elif liste[1] == 'MOVE':
            move[liste[2]] = liste[3].split(';')
        elif liste[1] == 'CHBTTRY':
            chbttry[liste[2]] = liste[3]
        elif liste[1] == 'RMNODE':
            rmnode = liste[2]
    read = command.readline()

for nodul in dic:
    x1 = int(dic[nodul][0]) + int(dic2[nodul][0])
    x2 = int(dic[nodul][0]) - int(dic2[nodul][1])
    y1 = int(dic[nodul][1]) + int(dic2[nodul][2])
    y2 = int(dic[nodul][1]) - int(dic2[nodul][3])
    for nodul2 in dic:
        if nodul != nodul2:
            if (int(dic[nodul2][0]) <= x1 and int(dic[nodul2][1]) <= y1) and (int(dic[nodul2][0]) >= x2 and int(dic[nodul2][1]) >= y2):
                liste3.append(nodul2)
    dic3[nodul] = liste3[0:len(liste3)]
    liste3.clear()
print(dic3)
