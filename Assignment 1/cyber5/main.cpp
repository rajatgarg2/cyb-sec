#include <iostream>
#include <string>
#include <ctype.h>

using namespace std;

int main()
{
    char ch;
    string str;
    cout<<"Enter the string : ";
    getline(cin,str);
    for(int i=0;i<str.length();i++)
    {
     if(str[i]>='A'&&str[i]<='Z')
     {
        int val=int(str[i]);
        val=val-64;
        if(i%2==0)
        {
            while(val!=0)
            {
                cout<<"#";
                --val;
            }
        }
        else
        {
            while(val!=0)
            {
                cout<<"$";
                --val;
            }
        }
    }
     if(str[i]>='a'&&str[i]<='z')
     {
        int val=int(str[i]);
        val=val-96;
        if(i%2==0)
        {
            while(val!=0)
            {
                cout<<"#";
                --val;
            }
        }
        else
        {
            while(val!=0)
            {
                cout<<"$";
                --val;
            }
        }
    }
    }
    return 0;
}
