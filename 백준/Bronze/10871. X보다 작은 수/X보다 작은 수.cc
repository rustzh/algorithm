#include <bits/stdc++.h>
using namespace std;

#define max 10000

int main()
{
   ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);   

   int n, x;
   cin >> n >> x;
   int A[max];

   for (int i=0; i<n; i++){
   		int a;
   		cin >> a;
   		A[i] = a;
	}

	for (int i=0; i<n; i++)
	{
		if (A[i]<x)
   			cout << A[i] <<" ";
	}

   return 0;
}