#include <iostream>

using namespace std;

int a[31];
int b[31];
int rice[31];
int a_value, b_value;

int main()
{
	int D, K; cin >> D >> K;

	a[1] = 1;
	a[2] = 0;

	b[1] = 0;
	b[2] = 1;

	for (int i = 3; i <= D; i++)
	{
		a[i] = a[i - 2] + a[i - 1];
		b[i] = b[i - 2] + b[i - 1];
	}

	for (int i = 1;i < 50000;i++) {
		if (((K - (a[D] * i)) % b[D]) == 0) {
			a_value = i;
			b_value = (K - (a[D] * i)) / b[D];
			break;
		}

	}

	cout << a_value << "\n" << b_value;

	return 0;
}
