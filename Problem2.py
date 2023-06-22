T1 = 1
T2 = 2
prev =T1
temp=T2
sum=0
#temp1 =0

while (temp<= 4000000):
    if temp % 2 ==0:
        sum=sum + temp
    temp1 = temp+prev
    prev= temp
    temp=temp1
print("The sum of the even numbers is :",sum)






  
