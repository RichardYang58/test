def power(base, exp=0):
    print(base**exp)
power(3,2)
power(3)

def divide(n1,n2):
    print(n1/n2)
divide(2,4)
divide(n2=2,n1=4)

def avg(*ns):
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))    

avg(3,4) 
avg(3,5,10)

