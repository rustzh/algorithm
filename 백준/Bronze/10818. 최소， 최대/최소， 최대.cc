#include <bits/stdc++.h>
using namespace std;

int main()
{
   ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);   

   int n;
   int min=1000000, max=-1000000;

   cin >> n;

   for (int i = 0 ; i<n; i++){
   	int a;
   	cin >> a;

   	if (a<min)
   		min = a;
   	if (a>max)
   		max = a;
   }

   cout << min << " " << max;

   return 0;
}