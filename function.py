def my_abs(x):
    if not isinstance(x,(int,float)):
        return TypeError("error parameter type")
    elif x>=0 :
        return x,1
    else:
        return -x,-1

print(my_abs(-92))


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())

def add_numbers(*numbers):
    sum=0
    for number in numbers:
        sum+=number
    return sum
nums=[2,3,4,5,6]
print(add_numbers(*nums))