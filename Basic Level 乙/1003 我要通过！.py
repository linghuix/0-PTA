import re

"""
“答案正确”是自动判题系统给出的最令人欢喜的回复。本题属于 PAT 的“答案正确”大派送 —— 只要读入的字符串满足下列条件，系统就输出“答案正确”，否则输出“答案错误”。

得到“答案正确”的条件是：

    字符串中必须仅有 P、 A、 T这三种字符，不可以包含其它字符；
    任意形如 xPATx 的字符串都可以获得“答案正确”，其中 x 或者是空字符串，或者是仅由字母 A 组成的字符串；
    如果 aPbTc 是正确的，那么 aPbATca 也是正确的，其中 a、 b、 c 均或者是空字符串，或者是仅由字母 A 组成的字符串。

现在就请你为 PAT 写一个自动裁判程序，判定哪些字符串是可以获得“答案正确”的。
输入格式：

每个测试输入包含 1 个测试用例。第 1 行给出一个正整数 n (<10)，是需要检测的字符串个数。接下来每个字符串占一行，字符串长度不超过 100，且不包含空格。
输出格式：

每个字符串的检测结果占一行，如果该字符串可以获得“答案正确”，则输出 YES，否则输出 NO。
输入样例：

8
PAT
PAAT
AAPATAA
AAPAATAAAA
xPATx
PT
Whatever
APAAATAA

输出样例：

YES
YES
YES
YES
NO
NO
NO
NO


"""
def check(str):
    i_p = 0
    i_t = 0
    for i in list(str):
        if i != 'A' and i != 'P' and i != 'T':
            print('NO')
            return 0
        if i=='P':
            i_p +=1
        
        if i=='T':
            i_t +=1
    
    if i_p != 1 or i_t != 1:
        print('NO')
        return 0
    return 1
        

def token(str):
    pattern = re.compile(r"(A*)P(A*)T(A*)")
    match = pattern.match(str)
    
    if match:
        t = match.groups()
        if t[1]=='':
            return 0
        return t
    return 0

def xPATx(token):
    
    if token[0]==token[2] and token[1] is 'A':
        return 'YES'
    else:
        if token[1] == 'A':
            return 'NO'
        new_token = (token[0],token[1][0:-1],token[2][0:-len(token[0])])
        # print(new_token)
        string = xPATx(new_token)
        return string

def main():

    # string = 'xPATx'
    number = int(input())
    for i in range(number):
        string = input()
        # if check(string):  不需要check因为正则表达式中已经包含了check的内容
        t = token(string)
        if t:
            # print(t)
            print(xPATx(t))
        else:
            print('NO')
    
    
    
if __name__ == '__main__':
    main()
