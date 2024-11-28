l1= [x for x in range(1,11)]
print(l1)

l2=[x for x in 'my name is john cena']
print(l2)

l3=[x**2 for x in range(2,100) if x**2%2==0  and x**2 <100]
print(l3)

l4=[x.lower() for x in 'BanGalasGehgas']
print(l4)

l5=[x for x in 'a8b*c;d[e23f g[hh-03j43;.' if x.isalpha() ]
print(l5)

data=input('Enter names using space: ')
l6=[x for x in data.split()]
print(l6)

l7=input('Enter occupation using space: ').split()
print(l7)