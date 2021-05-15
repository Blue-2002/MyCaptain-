a=[]
n=int(input("No of elements :"))
for i in range(0,n):
    x=int(input("Enter the elements :"))
    a.append(x)
for num in a:
    if num>0:
        print(num,end=" ")
