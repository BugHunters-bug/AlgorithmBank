#include<iostream>
#include<vector>
#include<cmath>
#include<cstring>
#include<climits>
#include<algorithm>
using namespace std;
using LL = long long;
using ULL = unsigned long long;
#define FOR(i,a,b) for(int i = a; i < b; i++)
#define DFOR(i,a,b) for(int i = a; i > b; i--)

void merge(int ar[],int lo,int mid,int hi){
    int p1=lo,p2=mid+1,temp[hi-lo+1],k=0;
    while(p1<=mid && p2<=hi){
        if(ar[p1] < ar[p2]){
            temp[k++] = ar[p1++];
        } 
        else{
            temp[k++] = ar[p2++];
        }
    }
    while(p1<=mid){
        temp[k++] = ar[p1++];
    }
    while(p2<=hi){
        temp[k++] = ar[p2++];
    }
    FOR(i,0,hi-lo+1){
        ar[i+lo] = temp[i];
    }
}

void MS(int ar[],int lo,int hi){
    if(lo==hi){
        return;
    }
    int mid = (lo+hi)/2;
    MS(ar,lo,mid);
    MS(ar,mid+1,hi);
    merge(ar,lo,mid,hi);
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    FOR(i,0,t){
        int n,k;
        cin >> n >> k;
        int a[n];
        FOR(j,0,n){
            cin >> a[j];
        }
        MS(a,0,n-1);
        FOR(j,0,n){
            cout << a[j] << " ";
        }
    }
    return 0;
}