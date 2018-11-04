x=b'ABC'
print(x)

#list是可变的有序表
classMates=['z1','z2','z3']
classMates.insert(1,'bb')
classMates.insert(2,'cc')
classMates.pop()
classMates.pop(1)
print(len(classMates),classMates,classMates[2],classMates[-1])

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
if 'Bob' in d:
    print(d['Bob'])

s = set([1, 1, 2, 2, 3, 3])
print(len(s),s)


