import sys

a = input()
a=int(a)
step=0

if a>1000:
    raise Exception('Number > 1000')
    
while(a!=1):
    if a%2:
        a = (3*a+1)//2
        print(a)
    else:
        a=a//2
        print(a)
    step=step+1


print('---------')
print(step)


