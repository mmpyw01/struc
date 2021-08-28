print("*** Reading E-Book ***")
txt , hl = input("Text , Highlight : ").split(",")

for i in range (0,len(txt)) :
    if (hl != txt[i]) :
        print(txt[i],end ="")
    else:
        print("[",end="")
        print(txt[i],end="")
        print("]",end="")
