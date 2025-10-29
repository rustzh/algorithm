#include <bits/stdc++.h>
using namespace std;

int main()
{
   ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);   

   int s_h, s_m;
   cin >> s_h >> s_m;

   int c_h, c_m;

   c_m = s_m - 45;
   if (c_m < 0){
   		c_m = c_m + 60;
    	s_h = s_h - 1;
	}

	c_h = s_h; 
	if (c_h < 0)
		c_h = c_h + 24;
	
	cout << c_h << " " << c_m;

   return 0;
}