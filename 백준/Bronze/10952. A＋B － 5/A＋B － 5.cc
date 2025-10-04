#include <bits/stdc++.h>
using namespace std;

int main()
{
   ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);   

   int a,b;

   while (cin >> a >> b){
   	if (a && b)
   		cout << a+b << "\n";
   	else
   		break;
   }

   return 0;
}