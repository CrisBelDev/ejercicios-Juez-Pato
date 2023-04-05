#include<bits/stdc++.h>
using namespace std;
int main(){
int enteros;
 cin>>enteros;
 for(int j=1;j<=enteros;j++)
 { int n,i,tr=0;
    cin>>n;
    int vec[n];
    for(i=1; i<=n ; i++){
       cin>>vec[i];
    }
    for(i=1; i<=n; i++){
      if(vec[vec[vec[i]]]==i){
        tr++;
      }
    }
    if(tr){
        cout<<"YES"<<"\n";
    }
    else{
        cout<<"NO"<<"\n";
 }
 }
return 0;
}