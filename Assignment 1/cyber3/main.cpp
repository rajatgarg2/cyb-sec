#include <iostream>

using namespace std;

int main()
{
    int a,b,i,j,flag;
    cout<<"Enter the range : ";
    cin>>a>>b;
    cout<<"Prime no.s between "<<a<<" and "<<b<<" are :";
    for(i=a;i<=b;i++)
    {
        if(i==1 || i==0)
        continue;
        flag=1;
        for(j=2;j<i/2;j++)
        {
            if(i%j==0)
            {
            flag=0;
            break;
            }
        }
        if(flag==1)
        cout<<endl<<i;
    }
    return 0;
}
