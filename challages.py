# calculate salary
# working_hours=[int(x) for x in input('enter working hours:').split()]
# wages=int(input('enter working hours:'))
# total_hours=sum(working_hours)
# salary= wages*total_hours
# print(salary)

# remove the duplicate element

# l1=[int(x) for x in input('enter numbers:').split()]
# l2=[]
# for x in l1:
#     if x not in l2:
#         l2.append(x)
# print(l1)
# print(l2)

# concatenate all integer
# l1=[1,6,8,7,6]
# n=[]
# l=''
# for x in l1:
#     l+=str(x)
#
# print(int(l))

# overlaping list elements
# l1=[10,5,3,6,9,7]
# l2=[5,6,4,1,20,3,9]
# l3=[]
# for x in l1:
#     if x in l2:
#         l3.append(x)
# print(l3)

# most occuring item in list
# l1=["a", "d", "e", "a", "c", 'e', 'f', 'd', 'a']
# result=[]
#
# for x in l1:
#     if (x,l1.count(x)) not in result:
#         result.append((x,l1.count(x)))
# print(result[0])

# find the words starts with given letter
l1=["asda", "dsds","rerer", "masda","raskjd", "dkjlk"]
letter= input("enter a letter: ")
for x in l1:
    if x[0]==letter:
        print(x)
