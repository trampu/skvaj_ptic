#-*-coding:utf8;-*-
#qpy:3
#qpy:console
print("This is console module calculated day consume")
import random
def rndm(first,i):
  c = first[2]/i
  c1 = c+c*0.05
  c2 = c-c*0.05
  c1 = int(c1)
  c2 = int(c2)
  ai = random.randint(c2, c1)
  return ai

def consume(first, day):
    ai = 0
    d = day
    f = 0
    i = 1
    secondA = secondB = secondD = [1]
    secondA = secondA*(day)
    secondB = secondB*(day)
    secondD = secondD*(day)
    second = [secondD, secondA, secondB]
    print ("_________________---------------_________________")
    while i <= day:
     if i == day:
      second[0][i-1] = i
      second[1][0] = first[2]
      second[2][i-1] = f + first[2] + first[0]
      i = i + 1
     else:
      ai = rndm(first,d)
      second[0][d-1] = d
      second[1][d-1] = ai
      first[2] = first[2] - ai
      second[2][d-2] = first[2] + first[0]
      d = d - 1
      i = i + 1
      f = f + ai
    print ("days", second[0])
    print ("potr", second[1])
    print ("itog", second[2])

firstA =  [1,1,1]
firstB =  [1,1,1]
first = [1,1,1]
firstA[0] = int (input("2000/10:before "))
firstA[1] = int (input("2000/10:after "))
firstA[2] = firstA[1] - firstA[0]

firstB[0] = int (input("2000/10:before "))
firstB[1] = int (input("2000/10:after "))
firstB[2] = firstB[1] - firstB[0]

day = int(input("day: "))

print ("raznica 2000/10", firstA[2])
print ("raznica 2000/11", firstB[2])
consume(firstA, day)
consume(firstB, day)
