#include <bits/stdc++.h>
using namespace std;

int main()
{
   ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);   

   int a, b, c, d, e;
   int result;

   cin >> a >> b >> c >> d >> e;
   result = a*a + b*b + c*c + d*d + e*e;
   result = result % 10;
   
   cout << result;

   return 0;
}