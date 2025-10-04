#include <iostream>

using namespace std;

int main()
{
	int n, a, sum;
	int result = 0;

	cin >> n;

	for (int i = n; i > 0; i--)
	{
		a = i;
		sum = a;
		while (a != 0)
		{
			sum += a % 10;
			a /= 10;
		}

		if (sum == n)
		{
			if (i < result || result == 0)
				result = i;
		}
	}

	cout << result;

	return 0;
}
