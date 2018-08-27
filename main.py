#-*-coding:utf8;-*-
#qpy:3
#qpy:console
print("This is console module calculated day consume")
import random
def rndm(firstA,i):
  c = firstA[2]/i
  c1 = c+c*0.05
  c2 = c-c*0.05
  c1 = int(c1)
  c2 = int(c2)
  ai = random.randint(c2, c1)
  return ai

firstA = [1,1,1]
firstA[0] = int (input("2000/10:before "))
firstA[1] = int (input("2000/10:after "))
firstA[2] = firstA[1] - firstA[0]

d = day = int(input("day: "))
secondA = secondB = secondD = [1]
secondA = secondA*(day)
secondB = secondB*(day)
secondD = secondD*(day)
second = [secondD, secondA, secondB]

print ("raznica", firstA[2])
f = 0
i = 1
ai = 0
while i <= day:
 if i == day:
  second[0][i-1] = i
  second[1][0] = firstA[2]
  second[2][i-1] = f + firstA[2] + firstA[0]
  i = i + 1
 else:
  ai = rndm(firstA,d)
  second[0][d-1] = d
  second[1][d-1] = ai
  firstA[2] = firstA[2] - ai
  second[2][d-2] = firstA[2] + firstA[0]
  d = d - 1
  i = i + 1
  f = f + ai
print ("days", second[0])
print ("potr", second[1])
print ("itog", second[2])
