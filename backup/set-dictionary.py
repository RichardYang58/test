s1={3,4,5}
print( 3 in s1)
s2={4,5,6,7}
s3=s1&s2
print(s3)
s3=s1|s2
print(s3)
s3=s1-s2
print(s3)
s3=s2-s1
print(s3)
s3=s1^s2   # 反交集
print(s3)
s=set("Hello")
print("H" in s)
dic = {"apple":"蘋果","bug":"重重"}
dic["apple"]="小蘋果"
print(dic["apple"])
print("apple" in dic)
del dic["apple"]
print(dic)
dic={x:x*2 for x in [3,4,5]}
print(dic)
