list1 = [1,2,3,4,5]

list1.append(12)
print(list1)

list1[len(list1):]=[25,35]
print(list1)

list1.extend([78,10,34])
print(list1)

list1.extend('asd')
print(list1)

list1.insert(1,'gorib')
print(list1)

list1.insert(1,['gorib','56'])
print(list1)

l2 = list1.copy()
print(list1)
print(l2)

l2.pop()
print(l2)

l2.pop(1)
print(l2)

l2.remove(35)
print(l2)

l2.clear()
print(l2)


l3=[1,5,9,7,6,3,4,2,6,8,9,4,0]
print(l3.index(6))
print(l3.index(6,5,-1))

print(l3.count(6))

l3.reverse()
print(l3)

l3.sort()
print(l3)
