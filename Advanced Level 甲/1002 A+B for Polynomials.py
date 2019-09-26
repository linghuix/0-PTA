#!/usr/bin/python3.6
# -*- coding: UTF-8 -*- 

"""
This time, you are supposed to find A+B where A and B are two polynomials.
Input Specification:

Each input file contains one test case. Each case occupies 2 lines, and each line contains the information of a polynomial:

K N​1​​ a​N​1​​​​ N​2​​ a​N​2​​​​ ... N​K​​ a​N​K​​​​

where K is the number of nonzero terms in the polynomial, N​i​​ and a​N​i​​​​ (i=1,2,⋯,K) are the exponents and coefficients, respectively. It is given that 1≤K≤10，0≤N​K​​<⋯<N​2​​<N​1​​≤1000.
Output Specification:

For each test case you should output the sum of A and B in one line, with the same format as the input. Notice that there must be NO extra space at the end of each line. Please be accurate to 1 decimal place.
Sample Input:

2 1 2.4 0 3.2
2 2 1.5 1 0.5

Sample Output:

3 2 1.5 1 2.9 0 3.2


"""

def main():

    result = dict()

    # string1 = input()
    # string2 = input()

    string1 = '3 5 3.5 3 2.5 1 -0.5' #input()
    string2 = '2 2 1.5 1 0.5' #input()

    string1 = [float(i) for i in string1.split(' ')]
    string2 = [float(i) for i in string2.split(' ')]

    for string in (string1,string2):
        i = string[0]
        del string[0]
        # print(string)
        
        for index in range(int(i)):
            # print(index)
            result[string[2*index]] = string[2*index+1]+result.get(string[2*index], 0)
            
            # 考虑相加为0的情况
            if result[string[2*index]]==0:
                del result[string[2*index]]

    print(len(result), end='')

    for i in sorted(result.keys(), reverse=True):
        # if result[i]==0:
            # continue
        print(" {} {}".format(int(i), round(result[i], 1)), end='')

if __name__ == '__main__':
    main()
    
