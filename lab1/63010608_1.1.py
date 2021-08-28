print("*** Rabbit & Turtle ***")

d,Vr,Vt,Vf = (input("Enter Input : ")).split()

t = float(d) / (int(Vt)-int(Vr))
s = int(Vf)*t
print('%.2f'%(s))