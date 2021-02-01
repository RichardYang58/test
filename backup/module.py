import sys
print(sys.platform)
print(sys.maxsize)
print(sys.path)
sys.path.append("modules")
print(sys.path)
import geometry
result=geometry.distance(1,1,5,5)
print(result)
result=geometry.slope(1,2,5,6)
print(result)
