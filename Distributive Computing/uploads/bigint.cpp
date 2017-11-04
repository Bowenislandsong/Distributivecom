// Copyright 2017 Dishant Pandya dishantp@bu.edu

#include <vector>
#include <string>
using namespace std;

typedef string BigInt;
BigInt multiply_int(const BigInt &a,const BigInt &b){
	int Alen=a.size();
	int Blen=b.size();
	int size=Alen+Blen;
	if(a.size()==0||b.size()==0){
		return "0";
	}
	//vector<int> e(a.size(),0);
	//vector<int> f(b.size(),0);
	vector<int> mul(size,0);
	int n1=0;
	int n2=0;
	for(int i=a.size()-1;i>=0;i--){
		int carry=0;
		int e=a[i]-'0';
		n2=0;
		for(int j=b.size()-1;j>=0;j--){
			int f=b[j]-'0';
			int sum= e*f+mul[n1+n2]+carry;
			carry=sum/10;
			mul[n1+n2]=sum%10;
			n2++;
		}
		if(carry>0)
			mul[n1+n2]+=carry;
		n1++;
		}
		int i=mul.size()-1;
		while(i>=0 && mul[i]==0)
			i--;
		if(i==-1)
			return "0";
		string s=" ";
		while(i>=0)
			s+=to_string(mul[i--]);

		return s;
	}	