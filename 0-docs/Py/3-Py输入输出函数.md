# 输入输出




## 1. 标准输入输出

#### 1.1  print

>  参数表：(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
>
> ```python
> file:  a file-like object (stream); defaults to the current sys.stdout.
> sep:   string inserted between values, default a space.
> end:   string appended after the last value, default a newline.
> flush: whether to forcibly flush the stream.
> ```






#### 1.2  int getchar(void);



#### 1.3 char *gets(char *s)


#### 1.4 puts



## 2. 格式化

#### 2.1  int printf(char *format, arg1, arg2, ...);	格式化输出


#### 2.2  int sprintf(char *string, char *format, arg1, arg2, ...);


#### 2.3  int scanf(char  \*format, ...)


## 3. 文件访问



#### 3.1 int putc(int c, FILE \*fp) 




#### 3.2 int getc(FILE \*fp)



#### 3.3 int fscanf(FILE \*fp, char \*format, ...) 



#### 3.4int fprintf(FILE \*fp, char \*format, ...) 



#### 3.5 char \*fgets(char \*line, int maxline, FILE \*fp) 


#### 3.6 int fputs(char \*line, FILE \*fp) 输出不需要包含换行符的字符串到文件



#### 小技巧


## 自定义有用的函数

