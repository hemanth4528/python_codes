def armstrong(number):
    temp = number
    d=0
    while temp>0:
        d=d*10+temp%10
        temp=temp//10
    if d==number:
        return True
    else:
        return False
n=int(input("Enter a number: "))
m=int(input("Enter a number: "))
for i in range(n,m+1):
    if armstrong(i):
        print(i,"is armstrong")