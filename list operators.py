list = [4, 'kabir', True, 9.8, "amir", "john", "dhaka", "BD"]
print(list[3])  # output 9.8
print(list[-2])  # output dhaka

print(list[2:5])  # output [True, 9.8, 'amir']

print(list[1:6:2])  # output ['kabir', 9.8, 'john']

print(list + [25, 89])  # output [4, 'kabir', True, 9.8, 'amir', 'john', 'dhaka', 'BD', 25, 89]

print(list + ["friday"])  # output [4, 'kabir', True, 9.8, 'amir', 'john', 'dhaka', 'BD', 'friday']

list[0:3] = [20, 30, 40]
print(list)  # output [20, 30, 40, 9.8, 'amir', 'john', 'dhaka', 'BD']
list[0:2] = [45, 98, 45, 26, 48, 5, 6, 79]
print(list)  # output [45, 98, 45, 26, 48, 5, 6, 79, 40, 9.8, 'amir', 'john', 'dhaka', 'BD']

print('dhaka' in list)  # output True

print('Dhaka' in list)  # output False
