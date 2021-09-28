#List Methods
l1=[1,2,3,4,5,6]
l2=[2,4,6,8]
l3=l1+l2#list Concatenation
print(l3)
n=len(l3)#length of list
print(n)
print(l3[0:2])#subscript operator Slicing of strings
l1.insert(0,10)
print(l1)
#searching in list
target = 5
if target in l1:
    print(l1.index(target))
#alising
list=[1,2,3]
list2=list
list[1]=5
print(list)
print(list2)
