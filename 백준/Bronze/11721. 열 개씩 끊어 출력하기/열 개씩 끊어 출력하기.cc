#include <iostream>

using namespace std;

int main() {
	char str[11];

	for (int i = 0; i < 10; i++) {
		cin.get(str, 11);

		if (!cin.gcount())
			break;
		
		cout << str << endl;
	}
}