from itertools import permutations
l = ['-25', '-10', '-7', '-3', '2', '4', '8', '10']  
seq = permutations(l,3)  
print(seq)
s=[] 
for p in list(seq):  
   if((p[0]+p[1]+p[2]) == 5) :
       s.append(p[0])
       s.append(p[1])
       s.append(p[2])