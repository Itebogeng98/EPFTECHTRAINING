num = 600851475143
num2 = 0
prim = 2

while num > 1:
    if num % prim == 0:
        num2= num/ prim
        print(prim)
        num= num2
            #prim+=1
    else:
        prim+=1




