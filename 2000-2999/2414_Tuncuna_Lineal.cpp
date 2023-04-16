#include "bits/stdc++.h"
using namespace std;
int T,N;
vector<int> v(1e6+5,0);
void tuncuna(){
	int x=1,pos;
	for(int i=1;i<=v.size()-1;i++){
		pos=int(i*(i+1)/2);
		if(pos <= v.size()-1){
		v[pos]=1;}
		else{break;}
	}
}
int main()
{	
	ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
	tuncuna();
	cin>>T;
	for (int i = 0; i < T; i++)
	{
		int con=0;
		cin>>N;
		for(int j=1;j<=N;j++){
			if(v[j]==1){
				con++;
			}
		}
		if(v[N]==1){
			cout<<"Llegas al cuadrado "<<con<<endl;}
			else{
			cout<<"No llegas"<<endl;
		}
		
	}
	return 0;
}