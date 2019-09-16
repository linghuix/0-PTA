"""import sys
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
"""


# A+B Format
#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# 输入 -546465 -4564
# 输出 格式化和 -551,029

# 格式化输入   正则表达式  https://blog.csdn.net/u010138758/article/details/70163944
# 格式化字符串 https://www.cnblogs.com/fat39/p/7159881.html
# 正则表达式 https://www.jianshu.com/p/5295c5988b7f

#python中的字符数字之间的转换函数
"""
int(x [,base ])         将x转换为一个整数    
long(x [,base ])        将x转换为一个长整数    
float(x )               将x转换到一个浮点数    
complex(real [,imag ])  创建一个复数    
str(x )                 将对象 x 转换为字符串    
repr(x )                将对象 x 转换为表达式字符串    
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象    
tuple(s )               将序列 s 转换为一个元组    
list(s )                将序列 s 转换为一个列表    
chr(x )                 将一个整数转换为一个字符    
unichr(x )              将一个整数转换为Unicode字符    
ord(x )                 将一个字符转换为它的整数值    
hex(x )                 将一个整数转换为一个十六进制字符串    
oct(x )                 将一个整数转换为一个八进制字符串   
"""

import re

def num_format(number):
    # 判断符号
    if number<0:
        sign='-'
        number = abs(number)
    else:
        sign=''
    
    if(number<1000):
        return sign+str(number)
    else:
        str_num = num_format(number//1000)
        # str_num = str_num+','+string(number//1000)是错误的，029会变成29
        # 方案一 str_num = str_num+','+str(number)[-3:]
        # 方案二 str_num = str_num+','+ '%03d' % number//1000
        str_num = str_num+','+ '%03d' % (number%1000)   #3表示数字宽度为3,0表示多余的位置以0填充
        return sign+str_num

string = input()
print(string)
pattern = re.compile(r"(\S+) (\S+)")
match = pattern.match(string)

if match:
    p = match.groups()
    print(match.groups())
    
    number = int(p[0])+int(int(p[1]))
    print(number)
    
    print(num_format(number))
