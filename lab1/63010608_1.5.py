num = int(input("Enter Input : "))

x=4+(num*2)
y=x/2
num2=0
for i in range(int(y)):
    for j in range(1,x+1):
        if(j<((x/2)-i)):
            print(".", end = '')
        elif(j>=((x/2)-i) and j<=(x/2)):
            print("#", end = '')
        elif(i==0):
            print("+", end = '')
        elif(i==y-1):
            print("+", end = '')
        elif(i<y and j==y+1):
            print("+", end = '')
        elif(i<x/2 and j<x):
             print("#", end = '')
        elif(i<x/2 and j==x):
             print("+", end = '')
    print('')
for i in range(int(y),x):
    for j in range(1,x+1):
        if(i==y and j<=y):
            print("#", end = '')
        elif(i==y and j<=x):
            print("+", end = '')
        elif(i==x-1 and j<y):
            print("#", end = '')
        elif(i<x and j==1):
            print("#", end = '')
        elif(i<x and j<y):
            print("+", end = '')
        elif(i<x and j==y):
            print("#", end = '')
        elif(i<x and j<=(x-num2)):
            print("+", end = '')
        elif(i<x and j<=x):
            print(".", end = '')
    num2+=1
    print('')