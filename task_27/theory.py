from math import *
from turtle import *

def sum_dist(starA, klaster):
    return sum(dist(starA, starB) for starB in klaster)

def center(klaster):
    minsum = 10*100
    for starA in klaster:
        d = sum_dist(starA, klaster)
        if d<minsum:
            minsum = d
            ans = starA
    return ans

def draw(klaster, dotsize, color, scale):
    pu()
    for x, y in klaster:
        goto(x*scale, y*scale)
        dot(dotsize, color)

test_klaster = [(0, 0), (0, 1), (1, 0), (1, 1), (5, 5)]

print(center(test_klaster))
# draw(test_klaster, 3, "red", 10)

klasters = [[], []]

for p in open("27-1a.txt"):
    x, y = [float(i) for i in p.replace(",", ".").split()]
    klasters[0 if y < -1.25*x + 2.5 else 1].append((x, y))

tracer(0)
draw(klasters[0], 5, "red", 50)
draw(klasters[1], 5, "green", 50)
draw([center(klasters[0])], 7, "purple", 50)
print([center(klasters[0])])
draw([center(klasters[1])], 7, "blue", 50)
print([center(klasters[1])])

print("x", center(klasters[0])[0] - center(klasters[1])[0])
print("y", center(klasters[0])[1] - center(klasters[1])[1])

# from math import *

def smDist(A,kl): return sum( dist(A,B) for B in kl )

def center(kl):
  mns = +10**100
  for A in kl:
    d = smDist(A,kl)
    if d<mns:
      mns = d
      ans = A
  return ans

KL = [[],[]]
for p in open('27-1a.txt'):
  x,y = [float(e) for e in p.replace(',','.').split()]
  KL[ 0 if x<1.5 else
      1].append([x,y])

print(center(KL[0]), len(KL[0]))
print(center(KL[1]), len(KL[1]))

##from turtle import *
##def draw(kl, clr, m ):
##  pu()
##  for x, y in kl:
##    goto(x*m, y*m)
##    dot(5,clr)
##tracer(0)  
##for kl,clr in zip(KL, ['red', 'blue']):
##  draw(kl,clr, 20)

done()