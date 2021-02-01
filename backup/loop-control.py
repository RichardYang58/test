n=0
while n<5:
    if n==3:
        break
    print(n)
    n+=1
print(n)  

n=0
for x in [0,1,2,3,4]:
    if x%2==0:
        continue
    print(x)
    n+=1
print("最後",n)

sum=0
for n in range(11):
    sum+=n
else:
    print(sum)    

n=input("輸入")   
n=int(n)
for i in range(n):
    if i*i==n:
        print("整數平方根",i)
        break  #break強制結束回圈，不會執行else區塊
else:
    print("沒有整數平方根") 