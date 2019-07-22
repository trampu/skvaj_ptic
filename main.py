#-*-coding:utf8;-*-
#qpy:3
#qpy:console
print("This is console module calculated day consume")
import random
from datetime import datetime
now = datetime.today()
now = now.strftime("%d.%m.%Y")
first = [1,1,1,1]
firstA =  [1,1,1,1]
firstB =  [1,1,1,1]
firstC =  [1,1,1,1]
firstD =  [1,1,1,1]
final = []
def rndm(first,i):
  c = first[2]/i
  c1 = c+c*0.05
  c2 = c-c*0.05
  c1 = int(c1)
  c2 = int(c2)
  ai = random.randint(c2, c1)
  return ai

def consume(first, day, output):
    ai = 0
    d = day
    f = 0
    i = 1
    secondA = secondB = secondD = [1]
    secondA = secondA*(day)
    secondB = secondB*(day)
    secondD = secondD*(day)
    print ("---------------_________________---------------_________________")
    while i <= day:
     if i == day:
      secondD[i-1] = i
      secondA[0] = first[2]
      secondB[i-1] = f + first[2] + first[0] + first[3]
      i = i + 1
     else:
      ai = rndm(first,d)
      secondD[d-1] = d
      secondA[d-1] = ai
      first[2] = first[2] - ai
      secondB[d-2] = first[2] + first[0] + first[3]
      d = d - 1
      i = i + 1
      f = f + ai
    print ("days", secondD)
    print ("potr", secondA)
    print ("itog", secondB)
    if output == 0:
        for item in secondD:
            final.append(item)
            final[item-1] = [1,2,3,4,5,6,7,8,9,None,None,None,None,None,None,None,None]
            final[item-1][1] = secondB[item-1]
            final[item-1][2] = secondA[item-1]
        final[len(secondB)-1][9] = first[1]
        final[len(secondB)-1][13] = final[len(secondB)-1][1] - final[len(secondB)-1][9]
    else:
        for item in secondD:
            final[item-1][1+output] = secondB[item-1]
            final[item-1][2+output] = secondA[item-1]
            final[item-1][16] = str(final[len(secondB)-1][16]) + "\n"
        final[len(secondB)-1][0] = now
        final[len(secondB)-1][int(9+output/2)] = first[1]
        final[len(secondB)-1][int(13+output/2)] = final[len(secondB)-1][1+output] - final[len(secondB)-1][int(9+output/2)]
        final[len(secondB)-1][16] = str(final[len(secondB)-1][16]).replace("\n", "")
    return(final)
def iinput():
    file = open("in.csv")
    linelist = file.readlines()
    file.close()
    lastline = linelist[-1]
    print (lastline)
    zero = lastline.split(';')
    print (zero)

    firstA[0] = int (zero[9])
    firstA[1] = int (input("1: "))
    firstA[2] = firstA[1] - firstA[0]
    firstB[0] = int (zero[10])
    firstB[1] = int (input("2: "))
    firstB[2] = firstB[1] - firstB[0]
    firstA[3] = int (zero[13])
    firstB[3] = int (zero[14])
    firstC[0] = int (zero[11])
    firstC[1] = int (input("3: "))
    firstC[2] = firstC[1] - firstC[0]
    firstD[0] = int (zero[12])
    firstD[1] = int (input("4: "))
    firstD[2] = firstD[1] - firstD[0]
    firstC[3] = int (zero[15])
    firstD[3] = int (zero[16])
iinput()
day = int(input("day: "))
#limit = int(input("limit: "))
limit = 200
limit = limit - (limit * 0.08)
limit2 = 60
limit2 = limit2 - (limit2 * 0.1)
print ("raznica 1", firstA[2])
print ("potreblenie 1", int (firstA[2]/day))
print ("raznica 2", firstB[2])
print ("potreblenie 2", int (firstB[2]/day))
print ("raznica 3", firstC[2])
print ("potreblenie 3", int (firstC[2]/day))
print ("raznica 4", firstD[2])
print ("potreblenie 4", int (firstD[2]/day))
if (firstB[2] > day*limit) or (firstA[2] > day*limit) and (firstB[3] < firstA[3]):
    firstA[2] = int(firstA[2] + firstB[2] - (day*limit))
    firstB[2] = int(day*limit)
elif (firstB[2] > day*limit) or (firstA[2] > day*limit) and (firstA[3] < firstB[3]):
    firstB[2] = int(firstB[2] + firstA[2] - (day*limit))
    firstA[2] = int(day*limit)
if (firstD[2] > day*limit2) or (firstC[2] > day*limit2) and (firstD[3] < firstC[3]):
    firstC[2] = int(firstC[2] + firstD[2] - (day*limit2))
    firstD[2] = int(day*limit2)
elif (firstD[2] > day*limit2) or (firstC[2] > day*limit2) and (firstC[3] < firstD[3]):
    firstD[2] = int(firstD[2] + firstC[2] - (day*limit2))
    firstC[2] = int(day*limit2)
consume(firstA, day, 0)
consume(firstB, day, 2)
consume(firstC, day, 4)
consume(firstD, day, 6)
#print(final)
def ioutput():
    file = open("in.csv", 'a+')
    #linelist = file.readlines()
    linelist = []
    file.write('\n')
    for i in final:
        print (i)
        b = ';'.join(map(str, i))
        linelist.append(b)
    print (linelist)
    for item in linelist:
         file.write(item) #file.write(item + '\n')
    file.close()
ioutput()
