import random
import math

def runBracket(c):
    round1 = ["", "", "", ""]
    round2 = ["", ""]
    result = [""]

    for i in range(0,4):
        if(i == 0):
            for j in range(0, round(len(c)/2)):
                if(random.randint(0,1) == 1):
                    round1[j] = c[j]
                else:
                    round1[j] = c[len(c)-1]
            print(round1)

        elif(i == 1):
            for k in range(0, round(len(c)/2)):
                if(random.randint(0,1) == 1):
                    round2[k] = round1[k]
                else:
                    round2[k] = round1[len(round1)-k-1]

        else:
            for x in range(0, round(len(c)/2)):
                if(random.randint(0,1) == 1):
                    result[x] = c[x]
                else:
                    result[x] = round2[len(round2)-x-1]
    return(result)

def main():
    upperCase = "ABCDEFGHIJKLOPQRSTUVWXYZ"
    lowerCase = "abcdefghijklopqrstuvwxyz"
    symbols = "!@#$&*"
    numbers = "1234567890"
    finalPass = []
    hold = []

    for i in range(0,5):
        c=[]
        if(i==0):
            for j in range(0,7):
                c.append(random.choice(upperCase))
        if(i==1):
            for k in range(0,7):
                c.append(random.choice(lowerCase))

        if(i>1 and i<4):
            for x in range(0,7):
                c.append(random.choice(symbols))

        if(i>3):
            for y in range(0,7):
                c.append(random.choice(numbers))

        print(c)
        hold = runBracket(c)
        finalPass = finalPass + hold;
    print("Password: ", finalPass)

main()
