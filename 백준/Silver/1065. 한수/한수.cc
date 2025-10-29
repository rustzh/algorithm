#include <iostream>

using namespace std;

int main()
{
	int n;
	int result = 0;

	cin >> n;

	for (int i = 1; i < n+1; i++) {

		if (i < 100) 
			result++;

		else if (i >= 100 && i < 1000) {
			int temp = i;
			int one_number = temp % 10;
			temp /= 10;
			int ten_number = temp % 10;
			temp /= 10;
			int hundred_number = temp % 10;

			if (hundred_number - ten_number == ten_number - one_number)
				result++;
		}
	}

	cout << result;

	return 0;
}
