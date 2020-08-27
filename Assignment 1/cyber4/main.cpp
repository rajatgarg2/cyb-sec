#include <iostream>
#include <string>
using namespace std;

int main()
{
    string str,str1;
    cout<<"Input String - ";
    getline(cin,str);
    int l=str.length();
    for(int i=0;i<l;i++)
    {
        int val=int(str[i]);
        str1+=char(val+5);
    }
    cout<<endl<<"Encrypted String - "<<str1;
    return 0;
}
