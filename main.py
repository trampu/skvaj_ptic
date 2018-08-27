#-*-coding:utf8;-*-
#qpy:3
#qpy:console
print("This is console module")
print("calculated day consume")
import random
def rndm(firstA,i):
  c = firstA[2]/i
  c1 = c+c*0.05
  c2 = c-c*0.05
  c1 = int(c1)
  c2 = int(c2)
  ai = random.randint(c2, c1)
  return ai
i = 1
ai = 0
firstA = [1,1,1]
firstA[0] = input("2000/10:before ")
firstA[0] = int(firstA[0])
firstA[1] = input("2000/10:after ")
firstA[1] = int(firstA[1])
firstA[2] = firstA[1] - firstA[0]

b = 13
day = input("day: ")
wday = day = int(day)
secondA = [1]
secondA = secondA*(day)
secondB = [1]
secondB = secondB*(day)
secondD = [1]
secondD = secondD*(day)
second = [secondD, secondA, secondB]

#print (second)
#srok
d = day
f = 0
print ("nachalo", firstA[2], day)
while i <= day:
 if i == day:
  second[0][i-1] = i
  second[1][i-1] = firstA[2]
  second[2][i-1] = f
  i = i +1
 else:
  ai = rndm(firstA,d)
  second[0][d-1] = d
  second[1][d-1] = ai
  second[2][d-1] = firstA[2]
  firstA[2] = firstA[2] - ai
  d = d - 1
  i = i + 1
  f = f + ai
  print("0")

print ("finish", f,firstA[2])
print ("all", second)
