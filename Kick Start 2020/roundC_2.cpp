#include<bits/stdc++.h>
using namespace std;

bool perfectsquare(int x){
	double y=sqrt(x);
	return((y-floor(y))==0);
}

int main(){
	int t,n;
	cin>>t;
	for(int k=1;k<t+1;k++){
		cin>>n;
		int arr[n];
		for(int i=0;i<n;i++){
			cin>>arr[i];
		}
		int count=0,s=0;
		for(int i=0;i<n;i++){
			s=0;
			for(int j=i;j<n;j++){
				s+=arr[j];
//				cout<<s<<" ";
				if(perfectsquare(s)){
					count+=1;
				}
			}
		}
		cout<<"Case #"<<k<<": "<<count<<endl;
	}

	return 0;
}
