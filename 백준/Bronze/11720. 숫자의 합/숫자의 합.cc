#include <iostream>
#include <string>

using namespace std;

int main() {
	int n;
	string str;

	cin >> n >> str;

	int ans = 0;
	for (int i=0; i<n; i++){
		ans += (str[i] - '0'); // ASCII 값을 이용한 식
	}

	cout << ans;
}