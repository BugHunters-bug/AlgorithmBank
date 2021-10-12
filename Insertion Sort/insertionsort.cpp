#include<iostream>
using namespace std;

int main()
{
    int  n;
    cin>>n;
    cout<<'\n';
    int *a=new int[n];
    for(int i=0;i<=n-1;i++){
        cin>>a[i];
    }
    

    for(int i=1;i<=n-1;i++){
        int j=i-1;
        int temp =a[i];
        while(j>=0&&a[j]>temp){
            a[j+1]=a[j];
            j--;
        }
        a[j+1]=temp;

    }

    for(int i=0;i<=n-1;i++){
        cout<< a[i];
    }
    return 0;
}