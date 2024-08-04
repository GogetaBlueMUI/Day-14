def find(num):
    collect=[]
    for i in range(1, num+1):
        if num%i==0:
            a=0
            for j in range(1, i+1):
                if i%j==0:
                    a+=1
            if a==2:
                collect.append(i)
    for i in collect:
        print(i)
    product = 1
    for i in collect:
        product *= i
    print("Product: ", product)
num=int(input("Enter number: "))
find(num)