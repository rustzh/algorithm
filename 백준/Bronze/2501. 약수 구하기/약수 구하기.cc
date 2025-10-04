#include <iostream>
using namespace std;

int a[10001];
int cnt = 0;

int main()
{

	int n, k; cin >> n >> k;

	for (int i = 1;i <= n;i++) {
		if (n % i == 0)
			a[i] = 1;
	}

	for (int i = 1;i <= n;i++) {
		if (a[i] == 1)
			cnt++;

		if (cnt == k) {
			cout << i;
			break;
		}
	}

	if (cnt < k)
		cout << "0";

	return 0;
}