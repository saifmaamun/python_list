list1 = [45, 98, 5, 40, 9.8, 'amir',]

for i in list1:
    print(i)
# output 45
# 98
# 5
# 40
# 9.8
# amir

for i in range(len(list1)):
    print(list1[i])
# output 45
# 98
# 5
# 40
# 9.8
# amir

for i in range(3,len(list1),2):
    print(list1[i])
# output
# 40
# amir

for i in range(-1, -(len(list1)+1),-1):
    print(list1[i])
# output
# amir
# 9.8
# 40
# 5
# 98
# 45