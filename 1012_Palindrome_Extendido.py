#include <iostream>
#include <cstring>
using namespace std;
 
int main()
{
    long long n;cin>>n;long long a;
    for(long long i=0;i<n;i++){
        cin>>a;
        a=(((a*(a-1))/2)+a)-(a-1);
        cout<<a<<endl;
    }
    return 0;
}
