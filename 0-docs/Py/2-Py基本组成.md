C 语言是默认以utf-8编码的，可以显示中文，C语言的源文件编码方式可以任意修改，只要编译器能认识就可以。
关键：编译器编译得到的*.o文件为ANSI编码（GB2312，GBK），支持中文的，因此可以在命令行输出中文
生成的exe也是ANSI编码

# 1.0 基本数据类型


## 数据基本类型

1 数据类型关键字
A.基本数据类型（5个）
void ：声明函数无返回值或无参数，声明无类型指针，显式丢弃运算结果
char ：字符型类型数据，属于整型数据的一种
int ：整型数据，通常为编译器指定的机器字长
float ：单精度浮点型数据，属于浮点数据的一种
double ：双精度浮点型数据，属于浮点数据的一种
B .类型修饰关键字（4个）
short ：修饰int，短整型数据，可省略被修饰的int。
long ：修饰int，长整形数据，可省略被修饰的int。
signed ：修饰整型数据，有符号数据类型
unsigned ：修饰整型数据，无符号数据类型
C .复杂类型关键字（5个）
struct ：结构体声明
union ：共用体声明
enum ：枚举声明
typedef ：声明类型别名
sizeof ：得到特定类型或特定类型变量的大小
D .存储级别关键字（6个）
auto ：指定为自动变量，由编译器自动分配及释放。通常在栈上分配
static ：指定为静态变量，分配在静态变量区，修饰函数时，指定函数作用域为文件内部
register ：指定为寄存器变量，建议编译器将变量存储到寄存器中使用，也可以修饰函数形参，建议编译器通过寄存器而不是堆栈传递参数
extern ：指定对应变量为外部变量，即标示变量或者函数的定义在别的文件中，提示编译器遇到此变量和函数时在其他模块中寻找其定义。
const ：与volatile合称“cv特性”，指定变量不可被当前线程/进程改变（但有可能被系统或其他线程/进程改变）
volatile ：与const合称“cv特性”，指定变量的值有可能会被系统或其他进程/线程改变，强制编译器每次从内存中取得该变量的值



```c
int 		//16位或者32位，机器中整型的自然长度
float		//32位，至少6位有效数字。单精度浮点型
char		//一个字节，8位。可以看成整数，也可以看成本地字符集中的字符
double		//双精度浮点

// 限定符
short		//限定整型，16位,不长于int。short int counter 可以省略int
long		//限定整型，32位，不短于int。long int counter 可以省略int
signed 		//限定char或者任意整型。对signed char 0~255
unsigned	//限定char或者任意整型。对unsigned char -128~127（-128~-1，0~127）。注意，可打印的字符永远是正值
const 		//不可变
register    //可以将使用频繁的变量放在CPU的通用寄存器中，这样使用该变量时就不必访问内存，直接从寄存器中读取，大大提高程序的运行效率。比如for中的i。
```

****

register

> * 能被CPU寄存器所接受的类型。意味着?register变量必须是一个单个的值，并且其长度应小于或等于整型的长度。
>
> * CPU的寄存器数目有限，因此，即使定义了寄存器变量，编译器可能并不真正为其分配寄存器
> * 局部静态变量不能定义为寄存器变量，因为一个变量只能声明为一种存储类别。
> * 为寄存器变量分配寄存器是动态完成的，因此，只有局部变量和形式参数才能定义为寄存器变量。
> * 变量不在内存中，不能&来获取内存地址

![img](F:\100-语言\S6-C\image\寄存器.png)

* 寄存器是最贴近CPU的，而且CPU只在寄存器中进行存取。
* 缓存的速度远高于内存，把使用频繁的数据暂时保存到缓存，如果寄存器需要读取内存中同一地址上的数据，直接从缓存中读取即可。缓存又被分为一级缓存、二级缓存和三级缓存
* 内存。硬盘等，容量大，但是读取速度无法苟同

**类型长度定义的符号常量以及其它与机器和编译器有关的属性见<limits.h>，<float.h>***

## 类型转换

### 自动转换
> 类型转换场合，1. 运算符两端数据类型不同时  2. 赋值语句，将右边类型转化为左边类型

* 数字之间转换类型。通常运算符两端自动转换是把比较窄的操作数转化为比较宽的操作数，比如int转float。***但是不同于JavaScript，自动转换是有限制的，float就不能够做为数组的下标，float赋给int类型变量，不会禁止但是会警告***

* 字符转整型 char->int  在机器上可能是正值也可能是负值，为保证可移植性，最好加上signed/unsigned限定。C规定可打印的字符集不会是负值，但转化为int就不一定了

* 赋值语句的转换可能会导致较长的整型转化为较短的整数或者char类型，导致高位被丢弃。double--> float 会截取后者四舍五入。float-->int 小数部分被截取

```c
	long aa = 1000000;
	short ee = aa;
	char gg = aa;
	printf("类型转换: %x\t%x\t%x\n",aa,ee,gg) ;
	//output:类型转换： f4240	4240	40
```
### 强制转换
> 可以发生在任何地方。语法： （类型名）表达式
> 函数被调用时，传入的参数会自动的强制转换
> ```c
> double sqrt(double);		//定义于<math.h>
> root2 = sqrt(2);			//2 会强制转化为2.0
> ```


# 2.0 数据结构

## String

> 属于constant，无法修改，只能重新创建一个string，将地址赋值给变量。
>
> 可以用整数索引引用某个位置的字符。



操作

![1565884105630](C:\Users\pc\AppData\Roaming\Typora\typora-user-images\1565884105630.png)

len()返回长度

string[x]返回x处的字符

### list -> string

```c
# 注意，使用该方法list必须是string类型的
list = ['1','2','3']
str = 'ab'
print(str.join(list))

# 上述代码等价于
list = [1,2,3]
list = [str(index) for index in list]
print(list)
str = 'ab'
print(str.join(list))
```





## list

> list 的索引必须是整数，但是比起string可以修改
>
> 
>
> 注意，修改list 的函数传入的是指针，没有返回值，
>
> list = list.append(x) 结果list就是None

### list特性

在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。

### string -> list

```c
# string.split(char)
'4564 54 56 4'.split(' ') -> ['4564', '54', '56', '4']

list(string)	# 返回单个字符的list
'1 2 3' -》 ['1', ' ', '2', ' ', '3']
```







### list操作

| list.append(x)    | 把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。        |
| ----------------- | ------------------------------------------------------------ |
| list.extend(L)    | 通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。 |
| list.insert(i, x) | 在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。 |
| list.remove(x)    | 删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。 |
| list.pop([i])     | 从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。） |
| list.clear()      | 移除列表中的所有项，等于del a[:]。                           |
| list.index(x)     | 返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。 |
| list.count(x)     | 返回 x 在列表中出现的次数。                                  |
| list.sort()       | 对列表中的元素进行排序。                                     |
| list.reverse()    | 倒排列表中的元素。                                           |
| list.copy()       | 返回列表的浅复制，等于a[:]。                                 |

通过list生成list

```python
# 快速生成list
vec = [2, 4, 6]
[[x, x**2] for x in vec]
> [[2, 4], [4, 16], [6, 36]]

# if
[3*x for x in vec if x > 3]
> [12, 18]
```

**del** a[0]

 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用 pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]	# 不包含左边
>>> a
[1, 66.25, 1234.5]
```



### 嵌套list

```c
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
    
# 以下实例将3X4的矩阵列表转换为4X3列表：
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# i=1时，[row[i] for row in matrix] = 【1，5，9】

# 实现转置方法二
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
```

## 字典dict

> list的升级版 —— 字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值，元组。
>
> 理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。

```python
>>> tel = {'jack': 4098, 'sape': 4139}

>>> tel['guido'] = 4127
>>> tel
{'sape': 4139, 'guido': 4127, 'jack': 4098}

>>> tel['jack']
4098
>>> del tel['sape']

>>> tel['irv'] = 4127
>>> tel
{'guido': 4127, 'irv': 4127, 'jack': 4098}

>>> list(tel.keys())
['irv', 'guido', 'jack']

>>> sorted(tel.keys())
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
```

快速创建

```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

# 索引是简单的字符串时：
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}

>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}
```

遍历操作

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave


# 同时遍历两个或更多的序列，可以使用 zip() 组合：
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.

# 反向遍历
for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```

| 序号 | 函数及描述                                                   |
| :--- | :----------------------------------------------------------- |
| 1    | [dict.clear()](https://www.runoob.com/python/att-dictionary-clear.html) 删除字典内所有元素 |
| 2    | [dict.copy()](https://www.runoob.com/python/att-dictionary-copy.html) 返回一个字典的浅复制 |
| 3    | [dict.fromkeys(seq[, val\])](https://www.runoob.com/python/att-dictionary-fromkeys.html) 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值 |
| 4    | [dict.get(key, default=None)](https://www.runoob.com/python/att-dictionary-get.html) 返回指定键的值，如果值不在字典中返回default值 |
| 5    | [dict.has_key(key)](https://www.runoob.com/python/att-dictionary-has_key.html) 如果键在字典dict里返回true，否则返回false |
| 6    | [dict.items()](https://www.runoob.com/python/att-dictionary-items.html) 以列表返回可遍历的(键, 值) 元组数组 |
| 7    | [dict.keys()](https://www.runoob.com/python/att-dictionary-keys.html) 以列表返回一个字典所有的键 |
| 8    | [dict.setdefault(key, default=None)](https://www.runoob.com/python/att-dictionary-setdefault.html) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default |
| 9    | [dict.update(dict2)](https://www.runoob.com/python/att-dictionary-update.html) 把字典dict2的键/值对更新到dict里 |
| 10   | [dict.values()](https://www.runoob.com/python/att-dictionary-values.html) 以列表返回字典中的所有值 |
| 11   | [pop(key[,default\])](https://www.runoob.com/python/python-att-dictionary-pop.html) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。 |
| 12   | [popitem()](https://www.runoob.com/python/python-att-dictionary-popitem.html) 随机返回并删除字典中的一对键和值。 |

## 元组Tuples 

> 元组无法修改，所以可以用于dict的键
> dict的升级版，索引必须是整数，但对应的可以是多个值，而不仅仅是dict的单个值，
>
> 对应值内容可以是list，但不能修改list，会报错。

```c
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
```

## 集合set

> 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典

```c
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # 删除重复的
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # 检测成员
True
>>> 'crabgrass' in basket
False

>>> # 以下演示了两个集合的操作
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # a 中唯一的字母
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # 在 a 中的字母，但不在 b 中
{'r', 'd', 'b'}
>>> a | b                              # 在 a 或 b 中的字母
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # 在 a 和 b 中都有的字母
{'a', 'c'}
>>> a ^ b                              # 在 a 或 b 中的字母，但不同时在 a 和 b 中
{'r', 'd', 'b', 'm', 'z', 'l'}
```



# 2. 常量，直接量

## 基本常量

```c
/*如下数据类型大小取决于具体的机器*/
//整型常量
1234						//int类型
123456789L/123456789l		//long类型
123u/123U					//unsigned 无符号常量
123456789ul/12345689UL		//unsigned long
0256						//八进制256，后缀也可加上U，L，UL
0x256/0X256					//十六进制256,后缀也可加上U，L，UL


//浮点数常量
2.5/1e-3					//double类型
2.56f						//float类型
2.56L/2.5l					//long double

```

## 字符常量

单引号中的字符表示一个整型值，值等于此字符在机器字符集（ASCII码或者其他编码格式，取决于系统）中对应的数值，称为字符常量。可以看成是整数也可以看成是字符

> * <ctype.h> 提供了一组与字符集无关的测试和转换函数，支持EBCDIC字符集，ASCII字符集等。tolower(c),isdigit(c)
> * 如何查看本机上的使用的字符集，在cmd中右击菜单选择属性，
> * ![字符集](image\字符集.jpg)
>
*  **ANSI编码**是扩展的**ASCII字符集**，它的0x00~0x7f(0~127) 与ASCII相同，从(0x80~0xFFFF)128~65536不同国家引入了不同的字符。中国制定了**GB2312编码**，用来把中文编进去另外，日本把日文编到Shift_JIS里，韩国把韩文编到Euc-kr里，各国有各国的标准。不同语言之间的ANSI码之间不能互相转换，这就会导致在多语言混合的文本中会有乱码。
*  为了解决不同国家**ANSI编码**的冲突问题，Unicode应运而生。中文为
*  **Unicode**虽好，但是问题在于，原本可以用一个字节存储的英文字母在**Unicode**里面必须存两个字节，从而出现了**UTF-8编码**，一种变长的编码方式：它可以使用1~4个字节表示一个符号，根据不同的符号而变化字节长度，当字符在ASCII码的范围时，就用一个字节表示，如此一来UTF-8编码也可以是为视为一种对ASCII码的拓展。中文为3个字节


* 简单字符
	* 如：在ASCII编码或者ANSI中字符'A' == 65，
	* GB2312编码中```char m[] = {'\xC4','\xE3','\0'};printf("%s \n", m);```输出‘你’字符
* 转义字符序列：
	* ‘\n’==10,是一个仅包含一个字符的字符串常量
	* ‘\0’ 表示值为0的字符，也就是null。通常用于替代0，以强调某些表达式的字符属性

所有的转义字符如下：
![转义字符](image\转义字符.jpg)


## 符号常量

#define 名字 替换文本

* 由**预处理器**解释
* 用于赋予幻数有意义的名字，注意末尾并没有分号；这些并不是变量，而是常量，不需要声明

* 一个好的宏（大小写转换）常常能够大大降低运算的时间，减少函数的调用次数。

## 字符串常量

* 双引号括起来的0个或者多个字符组成的字符序列。`"I am a string"
* 双引号不是字符串的组成部分。`"hello," " world" == "hello, world"

```printf("%s \n", "dfsd" "你好");```

* 字符串常量就是字符数组，内部使用‘\0’作为结尾标志，因此字符串物理存储单元比引号内的字符多1。‘\0’ASCII码为0，
* 因此，“a”与‘a’区别就很明显了。后者是一个整数，前者是字符+‘\0’。
![String](image\String.jpg)

<string.h>中定义了多种字符串操作函数

## 枚举常量

enum 常量名 {Bell = '\a', tab = '\t'} ，是一个常量整型值的列表，定义了枚举名和对应的值。

* 相对于#define来说，枚举值可以自动类推
* 枚举提供变量类型检查

```c
enum boolean { NO, YES };				//默认下，第一个值为0，第二个为1，以此类推
enum months { JAN = 1, FEB, MAR, APR,
MAY, JUN,JUL, AUG, SEP, OCT, NOV, DEC };//C编译器会自动类推加1
```

## 常量表达式

仅仅包含常量的表达式，在编译时求解，不在运行时求值

```c
#define MAXLINE 1000
char line[MAXLINE+1];
#define LEAP 1 /* in leap years */
int days[31+28+LEAP+31+30+31+30+31+31+30+31+30+31];
```

# 3. 变量


## 3.1 变量名

> 内部名，仅在定义该标识符的文件内使用的标识符，至少前31个字符是有效的，变量名区分大小写。
>
> 外部名，在  ***链接***  中涉及的在文件间调用的函数名，外部/全局变量等标识符，仅保证前6个字符的唯一性，不区分大小写
>
> 变量名不能用关键字


## 3.2 作用域

* C语言属于块状域。**作用域一般为声明所在的{}内部**
* 函数中的变量，在函数调用时存在，执行完毕后消失。两次调用，变量是不保留前次调用的值。因此也叫*自动变量*（static变量特殊）
* 所有函数外的变量，叫*外部/全局变量*。只要extern声明后就可以在函数内部调用。
  * 如果*全局变量*在同一源文件的该函数之前定义，那么extern可以省略

```c
    #define MAXLINE 1000  
    char line[MAXLINE], longest[MAXLINE]
    void main(void)
       {
           int i;
           extern char line[], longest[];
           i = 0;
           while ((longest[i] = line[i]) != '\0')
               ++i;
            return 0;
       }
```

* 如果程序有多个文件，某个变量在file1中定义，在file2中必须extern声明之后才能使用。人们喜欢将他们放到头文件中。类似于<stdio.h>
  
* 使用太多外部变量虽然可以简化函数的参数表，但是会大大的降低函数的通用性，应为他把变量名直接写入了函数中。

## 3.3 指针变量

### 声明与定义

```c
int *pr;					//定义pr指向的类型为int
double *dp，atof(char *);	//定义函数
void *pr;
```

###  初始化

注意，指针必须初始化为变量内存地址，才能进行使用。也可以初始化为NULL，NULL值在<stddef.h>中定义，为0.

```c
int a,*pr;
pr = &a;
```

### 有效运算操作

* 数组名称也就是数字第一个元素的指针，计算a[i]时，C语言是先转化为*(a+i)，再求值的。所以指针p可以直接用p[2]表示\*(p+2)。也可以使用p[-1]。需要注意：数组名是常量，指针是变量
* 同类型指针之间的赋值运算
* 指针和整数之间的加减法运算。**注意这里的得到的地址，和指针类型有关，如果指针为int，那么指针+1相当于地址+4，因为，int占4个字节**
* 指向同一数组元素的两个指针之间的减法或者比较运算
* 指针与NULL的比较和赋值运算

***除了以上，其余都不合法***



### Constant 指针

根据constant的位置不同，可以有以下四种情况：
**const char\* const msg_0;**
**const char\* msg_1;**
**char\* const msg_2;**
**char \*msg_3;**

* msg_0是一个constant指针指向一个const字符串。这个声明编译器会给出一个警告，因为msg_0的指向没有被初始化，而且之后的语句也无法对mg_0进行赋值，如``const char const *msg_0 = "hello";``会编译成功，但``*msg_0 = 'j';``或者``msg_0 = "good-bye"; ``将会产生错误

* msg_1既可以指向一个const字符串，也可以指向一个可变的字符串，但是不能修改它所指向的字符串的内容。

* 编译msg_2这条语句，会出现和编译msg_0一样的错误。因为指针是一个常量，所以它应该首先被赋值。如果刚开始已经赋值，那么它可以对指向的字符串内容进行修改，这段代码里，msg_2指向buf[0],并且永远指向这个地址，不会改变；如：

```c
  char buf[ 10 ];
  char * const msg_2 = buf;
```

* 对于msg_3，就没太多可以说的。你可以改变指针，也可以改变指针指向的内容

```c
char *msg = "hello";
*msg = 'j';
```

char *msg;
msg = "hello";
msg = "good-bye";

编译器会对这段代码给出 ***两段警示*** ，说”deprecated conversion from string constant to 'char *'"，你没有能力修改字符串的内容。即，不能进行`` \* msg = 'j';``操作


const char  *msg;
msg = "hello";
msg = "good-bye";

这段代码可以成功编译，并且将msg指向的值如愿改变，但如果**你将指针指向的地址进行赋值**：***msg = 'j';*****将会产生一个错误，不能修改一个字符串常量**


const char  *msg;
**char   buf[ 10 ];  		 //注意不能使用char \*buf；**，
sprintf( buf, "%03d/n", 7 );
msg = buf;

所以const其实在这里只是限制了msg指向的地址的值(buf)不变，但是地址的值(buf)也是一个地址，它的值是可以变化的



指针易错点

```c
   //代码功能： 插数某个数到排序完成的数组中，保持排序
	int x = 100;										//x 为需要插入的数
    int repeat, ri;
    int  n=10,a[10]= {5,6,8,20,50,68,92,120,580,980};	//数组a，从小到大排列 ， n为数组的大小 
	
	
    for(int i= 0; i < n; i++) {
    	
    	if(a[i]>=x){
    
    		/*for(int j= n; j>=i; j--){
    			
        		a[j+1]=a[j];	//移动数组,此处的代码会修改n的值，指针作的怪，a[11] 存的就是n的值 
        		printf("n = %d \n", n);	
    		} 
    		*/
            //正确的代码。本代码有缺陷，需要注意不能无限制的扩大数组，需要申请足够的地址空间
    		for(int j= n-1 ; j>=i; j--){
    			
        		a[j+1]=a[j];	//移动数组 
        		printf("n = %d \n", n);	
    		}
    		a[i]=x;
    		break;
    	}
    	else a[n]=x;
    }
```

### 函数指针

类似于数组名，函数名也是函数的地址，不需要用取地址运算符&。

```c
 void qsort(void *lineptr[], int left, int right,
              int (*comp)(void *, void *));
// comp为函数的指针，该函数具有两个void *类型的参数，返回值为int类型。comp指向的是 *comp，函数地址，

/*调用函数方法*/
(*comp)(i, j)
```


# 4. 运算符

![运算符优先级和结合性](image\运算符优先级和结合性.jpg)

结合性： 当一个运算对象两侧的运算符优先级别相同时，按照结合性来确定算法的运算顺序

编译器： 尽可能将表达式从左至右将若干个字符组成运算符

```c
a*b+++b;	//实际执行的是：(a*(b++))+b
```

***注意C语言中没有平方，只有函数pow(10.0,2)***



## 基本运算符

一元运算符

* !(逻辑运算，将非零的数转化为0，0转化为1), ~(按位求反),
* \*（指针间接访问运算符） ,作用于地址时，访问地址指向的对象
* & 获取变量/对象的地址，只能作用于内存中的对象，不能作用于表达式，常量，register类型变量。
* (type) 类型强制转换
* ++n  自增1，在行代码计算中使用增加1后的值。比如
```c
int a = 2;
b = ++a;
printf("a = %d,b = %d",a,b)
a = 3,b = 3
```
* n++   自增1，在本行代码计算中使用增加1前的值.譬如：


```c
int a,b,c,d;
 	a = 5;b = 5;c = 5;d = 5;
 	printf("%d",++a = b+c*d);
//先计算两端值，a自增1，变成6，右边值为30，然后赋值给a，a就变成了30，最后输出 30
```
* ->和. 为结构体成员访问运算符

编译时一元运算符

* 使用方法：sizeof（类型名）/sizeof 对象，可以是变量，数组和结构，类型可以是**基本类型**，也可以是**派生类型**（**结构类型**或者**指针类型**）
* 不包括字符串的结尾标志符‘\0’。返回值是无符号整型值，类型为size_t，该类型在头文件<stddef.h>中定义。

二元运算符：

* +, -, *, /, %(取模运算，不能用于float，double类型)

赋值运算符

```c
 while ((c = getchar()) !=EOF)  	//赋值表达式具有值 ,有助于编译器产生高效的代码。其类型为左操作数的类型，其值时赋值操作完成后的值
```

* ***赋值表达式具有值 ,其类型为左操作数的类型，其值是赋值操作完成后的值***
* ==   等于关系运算符 先计算等号两边，然后比较大小
* = 赋值运算。先计算等号两边，在将右边的值赋给左边。
* x *= y + 1  等价于 x = x*(y+1)
按位运算

逻辑位运算

* &,|,~,<<,>>,^(按位异或)需要与八进制，十六进制直接量配合进行运算。

逻辑运算

* &&，||的运算结果只能是1或者0

逗号运算符

* 优先级最低的运算符，在for循环中经常使用。结合性按从左到右的顺序求值（***图片错了***）
* ***类似于赋值表达式，表达式右边的操作数的类型和值为其结果的类型和值***

```c
//表达式1，表达式2，再求解表达式2。整个逗号表达式的值是表达式2的值。
int a = 5,c= 6,e,g=50;
printf("%d",++g,a=90,c=9) ;		//输出51
printf("%d",(++g,a=90,c=9)) ;	//输出9
printf("%d",(a=3*5，a*4)) ;		//输出60
x=a=3，6*a						//x为3，原因是逗号运算符是优先级最低运算符
```

* 逗号表达式在多步计算的宏中应用广泛，

三元运算符：？

* expr1 ? expr2 : expr3;
* 首先计算expr1，为真则计算expr2，为假则计算expr3。
* 三元表达式本身也是有**值**的，以计算的值作为该表达式的值

```c
z = (a>b)? a:b;		//z取ab中较大的值
```

# 5. 控制流

```c
// 
if(表达式){
    语句；
}
else if(表达式){    
}
else{ 			//上述条件均不成立
    
}
-----------------------------------------------
//分支排列次序是任意的，某个分支执行后将会继续执行下一个分支，可以用break语句强行退出while，for，do循环
switch (表达式) {				
case 常量表达式: 语句序列
case 常量表达式: 语句序列
default: 语句序列
-------------------------------------------------
while (表达式)
语句
--------------------------------------------------  
for (表达式 1; 表达式 2; 表达式 3)
	语句
//等价于
表达式 1
while (表达式 2){
	语句
    表达式 3
}
//注意当，循环中存在continue时，两者不等价

----------------------------------------------------
do-while 循坏的语法形式如下：
do
	语句
while (表达式);

```

# 6. 函数

* main（）函数是程序的入口，他也可以传递参数进去，return 0表示程序运行正常
* C 语言是以传值的方式将参数值传递给被调用函数的，因此不能直接修改主函数中的值。

## 声明 

int power(int base, int n) 或者  int power(int, int);

## 定义 
return 返回值

```c
函数定义的一般形式：
返回值类型(默认为int)  函数名（0个或者多个参数声明）{
	声明部分
	语句序列
	return 返回值/表达式 或者无return
}

返回值类型：void，所有数据类型
```

* 函数参数在函数被调用时进行初始化，所以修改这个参数，并不能修改你传入的主函数的变量的值（除了指针）
* 函数参数有助于减少额外的零时变量



## 函数间传递参数的设计方法

返回值：可以作为标志位，判断程序是否正常运行

用指针传递访问参数



## main函数

main函数时特殊的函数，是我们的程序的入口，

```c
main(int argc, char *argv[])	//命令行参数
```

* argc  参数计数值，至少为1.

* argv 参数向量，指向字符串数组的指针。argv[0]为程序名，第一个可选参数为argv[1]。ANSI标准要求argv[argc]必须为空指针

命令` echo hello,  world`，argv[0]为echo，argv[1]为`hello,`，argv[2]为`world`

![命令行参数](image\命令行参数.jpg)