print("*** multiplication or sum ***")
num1, num2 = (input("Enter num1 num2 : ").split())

multi = int(num1)*int(num2)
sum = int(num1)+int(num2)

if multi<=1000 :
    print("The result is" , multi)
else :
    print("The result is" , sum)