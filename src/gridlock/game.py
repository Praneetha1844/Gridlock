import random
import array as arr
from array import *
import sys
def fullboard():
 for r in table:
    for c in r:
        if(table[s][p]=="x" or table[s][p]=="o" ): # map(int, input().split())
            print("it is a tie")
        else:
            return
def askinput():
   s,p=map(int,input("enter the coordinates").split())
   if (n==1):
      table[s][p]="x"
      for r in table:
        for c in r:
          print(c,end = " ")
        print()
   elif (n==2):
      table[s][p]="o"
      for r in table:
        for c in r:
          print(c,end = " ")
        print()
def checking():
    if (table[0][0]=="x" and table[0][1]=="x" and table[0][2]=="x"):
        print("player 1 won")
        exit()
    elif (table[1][0]=="x" and table[1][1]=="x" and table[1][2]=="x"):
        print("player 1 won")
        exit()
    elif (table[2][0]=="x" and table[2][1]=="x" and table[2][2]=="x"):
        print("player 1 won")
        exit()
    elif (table[0][0]=="x" and table[1][0]=="x" and table[2][0]=="x"):
        print("player 1 won")
        exit()
    elif (table[0][1]=="x" and table[1][1]=="x" and table[2][1]=="x"):
        print("player 1 won")
        exit()
    elif (table[0][2]=="x" and table[1][2]=="x" and table[2][2]=="x"):
        print("player 1 won")
        exit()
    elif (table[0][0]=="x" and table[1][1]=="x" and table[2][2]=="x"):
        print("player 1 won")
        exit()
    elif (table[0][2]=="x" and table[1][1]=="x" and table[2][0]=="x"):
        print("player 1 won")
        exit()
    elif (table[0][0]=="o" and table[0][1]=="o" and table[0][2]=="o"):    #2nd player winning
        print("player 2 won")
        exit()
    elif (table[1][0]=="o" and table[1][1]=="o" and table[1][2]=="o"):
        print("player 2 won")
        exit()
    elif (table[2][0]=="o" and table[2][1]=="o" and table[2][2]=="o"):
        print("player 2 won")
        exit()
    elif (table[0][0]=="o" and table[1][0]=="o" and table[2][0]=="o"):
        print("player 2 won")
        exit()
    elif (table[0][1]=="o" and table[1][1]=="o" and table[2][1]=="o"):
        print("player 2 won")
        exit()
    elif (table[0][2]=="o" and table[1][2]=="o" and table[2][2]=="o"):
        print("player 2 won")
        exit()
    elif (table[0][0]=="o" and table[1][1]=="o" and table[2][2]=="o"):
        print("player 2 won")
        exit()
    elif (table[0][2]=="o" and table[1][1]=="o" and table[2][0]=="o"):
        print("player 2 won")
        exit()
    else:
        return
table=[["-","-","-"],["-","-","-"],["-","-","-"]]
for r in table:
    for c in r:
     print(c,end = " ")
    print()
n=random.randint(1, 2)
print("player",n,"enter the coordinates")
askinput()
checking()
for i in range(0,8):
  if(n==1):
    n=2
    print("its player 2's turn")
    askinput()
    checking()
  elif(n==2):
    n=1
    print("its player 1's turn")
    askinput()
    checking()
print("it is a tie")





