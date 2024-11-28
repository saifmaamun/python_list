# calculate salary
# working_hours=[int(x) for x in input('enter working hours:').split()]
# wages=int(input('enter working hours:'))
# total_hours=sum(working_hours)
# salary= wages*total_hours
# print(salary)

# remove the duplicate element

l1=[int(x) for x in input('enter numbers:').split()]
l2=[]
for x in l1:
    if x not in l2:
        l2.append(x)
print(l1)
print(l2)