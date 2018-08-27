#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")
#-*-coding:utf8;-*-
print("calculated day consume")
import random
def rndm(a,i):
  c = a/i
  c1 = c+c*0.05
  c2 = c-c*0.05
  c1 = int(c1)
  c2 = int(c2)
  ai = random.randint(c2, c1)
  return ai
i = 1
ai = 0
a = input("2000/10:before ")
a = int(a)
aa = input("2000/10:after ")
aa = int(aa)
a = aa - a
#b = input("2000/11:before ")
#b = int(b)
#bb = input("2000/10:after ")
#bb = int(bb)
#b = bb - b
#a = 3890
#rashod
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
print ("nachalo", a, day)
while i <= day:
 if i == day:
  second[0][i-1] = i
  second[1][i-1] = a
  second[2][i-1] = f
  i = i +1
 else: 
  ai = rndm(a,d)
  second[0][d-1] = d
  second[1][d-1] = ai
  second[2][d-1] = a
  a = a - ai
  d = d - 1
  i = i + 1
  f = f + ai
  print("0")

print ("finish", f,a)
print ("all", second)
