#include <iostream>
#include <string>
using namespace std;

int main()
{
    string str;
   cout<<"Enter a string : ";
   getline(cin,str);
   int len=str.length()-1;
   int i=0;
   while(len>i)
   {
       if(str[i++]!=str[len--])
       {
           cout<<endl<<str<<" is not palindrome.";
           return 0;
       }
   }
   cout<<endl<<str<<" is palindrome";
   return 0;
}
