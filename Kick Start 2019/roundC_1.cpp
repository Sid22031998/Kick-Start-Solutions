#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,n,r,c,x,y;
	cin>>t;
	for(int k=1;k<=t;k++){
		cin>>n>>r>>c>>x>>y;
		string s;
		cin>>s;
		x--;
		y--;
		int arr[r][c];
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				arr[i][j]=0;
			}
		}
		arr[x][y]=1;
		for(int i=0;i<n;i++){
			if(s[i]=='E'){
				while(arr[x][y]){
					y++;
				}
			}else if(s[i]=='W'){
				while(arr[x][y]){
					y--;
				}
			}else if(s[i]=='N'){
				while(arr[x][y]){
					x--;
				}
			}else if(s[i]=='S'){
				while(arr[x][y]){
					x++;
				}
			}
			arr[x][y]=1;
		}
		cout<<"Case #"<<k<<": "<<x+1<<" "<<y+1<<endl;
	}
	return 0;
}
