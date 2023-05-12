from typing import Any, List
import random

def testing_par(l):
    print(str(l)+" sqd")

"""

for i in range(15):
    if i % 2 == 0:
        print("par")
    else:
        print("impar")  """


def randome4(passing,minimum,n):
    fails = 0
    for j in range(n):
        hits = 0
        for i in range(minimum):
            if random.random() >= .25:
                hits += 1
        if hits >= passing:
            fails += 1
    return (fails/n)*100

ipairs = [i for i in range(10) if i%2 == 0]

def multNum(num,steps):
    if steps == 0:
        print(num)
    lista = [int(i) for i in str(num)]
    counter = 1
    steps+=1
    for i in lista:
        counter *= i
    if len(str(counter)) == 1:
        print(counter)
        print("Number of steps: " + str(steps))
        return counter
    else:
        print(counter)
        return multNum(counter,steps)

#multNum(277777788888899,0)


def multNum2(num,steps):
    if steps == 0:
        print(num)
    count = 1
    steps += 1
    for i in str(num):
        count *= int(i)
    if len(str(count)) == 1:
        print(count)
        print("Number of steps: " + str(steps))
        return (count)
    else:
        print(count)
        return(multNum2(count,steps))

def revString(x):
    result = ""
    lista = []
    for i in range(len(x)):
        if x[-1-i] != " ":
            result += x[-1-i]
        else:
            lista.insert(0,result)
            result = ""
            PPMD = True
    if PPMD:
        lista.insert(0,result)
    result = ""
    for i in range(len(lista)):
        if i != len(lista)-1:
            result += lista[i] + " "
        else:
            result += lista[i]
    return(result)

def revString(x):
    x = [i for i in str(x)]
    for i in range(len(x)//2):
            x[i], x[-1-i] = x[-1-i], x[i]
    x = ''.join(x)
    return(x)


print(revString("Hello World!"))


