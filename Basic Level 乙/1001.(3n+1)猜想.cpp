//<iostream>    
//该文件定义了 cin、cout、cerr 和 clog 对象，分别对应于标准输入流、标准输出流、非缓冲标准错误流和缓冲标准错误流。

//命名空间
using namespace std;    //表示默认的命名空间为std，不然cin就要写成 std::cin 
namespace::code;         // code 可以是变量或函数
namespace first_space{
   void func(){
      cout << "Inside first_space" << endl;
   }                    //定义一个命名空间


//endl、cout、cin、cerr、clog 定义在std命名空间中

//endl回车符，是语句中的末尾字符，
//cin 标准输入流
//cerr 错误流
//cout 标准输出流
//clog 标准日志流 但是 clog 对象是缓冲的。这意味着每个流插入到 clog 都会先存储在缓冲在，直到缓冲填满或者缓冲区刷新时才会输出。


#include<iostream>
using namespace std;
int main()
{
    int n,i=0,j;
    cin>>n;
    if(n==1) {cout<<i<<endl;return 0;}
   do{
        if(n%2==0)
           n=n/2;
        else
            n=(3*n+1)/2;
        i++;
    }while(n!=1);
 cout<<i<<endl;
 return 0;
}