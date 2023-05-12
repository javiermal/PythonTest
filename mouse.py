import random as r



def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string)-len(sub_string)+1):
        for j in range(len(sub_string)):
            if string[i+j] != sub_string[j]:
                break
            if (j) == len(sub_string)-1:
                count += 1
    return count




def wrap(string, max_width):
    t = string[0:]
    count = 0
    for i in range(len(string)):
        if count == max_width:
            t = t[:i] + '\n' + t[i:]
            count = -1
        count += 1
    return t

def wrap(string, max_width):
    lista = []
    t = ""
    count = 0
    for i in range(0,len(string)):
        if count == max_width:
            lista.append(string[i-max_width:i])
            count = 0
        count += 1
    if len(string) % max_width != 0:
        lista.append(string[-(len(string) % max_width):])
    
    for i in range(0,len(lista)-1):
        t = t + lista[i] + "\n"
    t = t + lista[-1]
    return t


def cabras(n):
    lista = [i for i in range(1,n+1)]
    print(lista)
    user = int(input("Select a number from 1 to " + str(n) + ": "))
    y = r.randint(1,n)
    print ("I will remove some options")
    print("The two options are: ")
    if user == y:
        other = r.randint(1,n)
        while (other == user):
            other = r.randint(1,n)
        lista = [other,user]
        
        print(lista)
    else:
        lista = [y,user]
        print(lista)

    
    answer = input("Do you wanna change? (Y/N)")

    if answer == "Y":
        user = lista[0]
    
    print(str(user) + " is your final option")
    print("The answer is ..." + str(y))
    if user == y:
        print("We have a winner !!")
    else:
        print("Better luck next time")



def Autocabras(n, answer):
    winner = 0
    loser = 0
    for i in range(100000):
        x = r.randint(1,n-1)
        y = r.randint(1,n-1)
        if x == y:
            other = r.randint(1,n-1)
            while (other == x):
                other = r.randint(1,n-1)
                lista = [other,x]
        else:
            lista = [y,x]

        if answer:
            x = lista[0]

        if  x == y:
            winner = winner + 1
        else:
            loser = loser + 1
    print("Percentage Losers: " + str((loser/(winner+loser))*100) + "% Percentaje Winners: " + str((winner/(winner+loser)*100))+"%")

Autocabras(100, True)



