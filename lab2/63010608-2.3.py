def mod_position(arr,s):
    l = []
    for x in range(1,len(arr)+1):
        if x%s==0 :
            l.append(arr[x-1])
        else:
            x+=1
    print(l)

print("*** Mod Position ***")
txt,num = input("Enter Input : ").split(",")
mod_position(txt,int(num))
