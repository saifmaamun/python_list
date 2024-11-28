# calculate salary
working_hours=[int(x) for x in input('enter working hours:').split()]
wages=int(input('enter working hours:'))
total_hours=sum(working_hours)
salary= wages*total_hours
print(salary)