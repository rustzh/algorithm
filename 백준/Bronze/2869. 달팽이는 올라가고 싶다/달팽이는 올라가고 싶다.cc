#include <iostream>
using namespace std;

int main() {
	int A, B, V;
	cin >> A >> B >> V;;

	int cnt = (V - A) / (A - B);

	if ((V - A) % (A - B) == 0) {
		cnt += 1;
	}
	else {
		cnt += 2;
	}

	cout << cnt;
}