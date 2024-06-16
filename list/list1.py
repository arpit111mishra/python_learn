ls=[1,2,3,4,"arpit","mishra"]
print(ls)
print(ls[0])
print(ls[3])
ls[0]=100
print(ls)
#list slicilng
print(ls[0:])
print(ls[-3:-1])
print(ls[1:3])
print(ls[:4])
#list methods
lis=[2,3,1]
lis.sort()
print(lis)
lis.append(4)
print(lis)
lis.sort(reverse=True)
print(lis)
lis.insert(2,6)
print(lis)
lis.remove(6)
print(lis)
lis.pop(0)
print(lis)