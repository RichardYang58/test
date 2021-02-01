import random
data=random.choice([1,5,7,8,11,23,34])
print(data)
data=random.sample([1,5,7,8,11,23,34],3)
print(data)
data=[1,5,8,11]
print(data)
random.shuffle(data)
print(data)
data=random.random()
print(data)
data=random.uniform(60,100)
print(data)
data=random.normalvariate(100,10)
print(data)
import statistics as stat
data=stat.mean([1,4,5,8])
print(data)
