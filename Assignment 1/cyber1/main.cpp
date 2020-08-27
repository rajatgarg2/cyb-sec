#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;
    char ch;
    float r,a,l,b,h,ba;
    do{
    cout<<"1. Area of circle"<<endl;
    cout<<"2. Area of rectangle"<<endl;
    cout<<"3. Area of triangle"<<endl;
    cout<<"Enter your choice : ";
    cin>>n;
    switch(n)
    {
        case 1: cout<<"Enter the radius of the circle : ";
                cin>>r;
                a=3.14*r*r;
                cout<<"Area of circle is : "<<a;
                break;
        case 2: cout<<"Enter the length and breadth of the rectangle : ";
                cin>>l>>b;
                a=l*b;
                cout<<"Area of rectangle is : "<<a;
                break;
        case 3: cout<<"Enter height and base of triangle : ";
                cin>>h>>ba;
                a=(0.5)*h*ba;
                cout<<"Area of triangle is : "<<a;
                break;
        default: cout<<endl<<"Enter a valid choice";
    }
    cout<<endl<<"Do you want to run this program again (y/n) : ";
    cin>>ch;
    }while(ch=='y');
        return 0;
}
