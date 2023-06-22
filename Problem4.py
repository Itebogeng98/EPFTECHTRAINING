product =0
productChar =0
largest_palidrom=0


for i in range(999,100,-1):
    for x in range(999,100,-1):
        product=i*x
        productChar = str(product)
        productRv = str(product)[::-1]
        if (productChar == productRv and product>largest_palidrom):
            largest_palidrom = product

print(largest_palidrom) 



