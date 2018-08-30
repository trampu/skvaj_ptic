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
    second = [secondD, secondA, secondB]
    print ("---------------_________________---------------_________________")
    while i <= day:
     if i == day:
      second[0][i-1] = i
      second[1][0] = first[2]
      second[2][i-1] = f + first[2] + first[0] - first[3]
      i = i + 1
     else:
      ai = rndm(first,d)
      second[0][d-1] = d
      second[1][d-1] = ai
      first[2] = first[2] - ai
      second[2][d-2] = first[2] + first[0] - first[3]
      d = d - 1
      i = i + 1
      f = f + ai
    print ("days", second[0])
    print ("potr", second[1])
    print ("itog", second[2])
    if output == 0:
        for item in second[0]:
            final.append(item)
            final[item-1] = [1,2,3,4,5,6,7,8,9,None,None,None,None,None,None,None,None]
            final[item-1][1] = second[2][item-1]
            final[item-1][2] = second[1][item-1]
        final[len(second[2])-1][9] = first[1]
        final[len(second[2])-1][13] = first[1] - final[len(second[2])-1][9]
    else:
        for item in second[0]:
            final[item-1][1+output] = second[2][item-1]
            final[item-1][2+output] = second[1][item-1]
        final[len(second[2])-1][0] = now
        final[len(second[2])-1][int(9+output/2)] = first[1]
        final[len(second[2])-1][int(13+output/2)] = first[1] - final[len(second[2])-1][9]
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
iinput()
day = int(input("day: "))
limit = int(input("limit: "))
limit = limit - (limit * 0.08)
#delta - raznica s faktom
print ("raznica 1", firstA[2])
print ("potreblenie 1", int (firstA[2]/day))
print ("raznica 2", firstB[2])
print ("potreblenie 2", int (firstB[2]/day))
if (firstB[2] > day*limit) or (firstA[2] > day*limit) and (firstB[3] < firstA[3]):
    firstA[2] = int(firstA[2] + firstB[2] - (day*limit))
    firstB[2] = int(day*limit)
elif (firstB[2] > day*limit) or (firstA[2] > day*limit) and (firstA[3] < firstB[3]):
    firstB[2] = int(firstB[2] + firstA[2] - (day*limit))
    firstA[2] = int(day*limit)

consume(firstA, day, 0)
consume(firstB, day, 2)
print(final)
