#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

	int n, s;
	cin >> n >> s;


	vector<long long> v(n, 0);

	for (int i = 0; i < n; i++) {
		cin >> v[i];
	}

	long long len = n + 1;
	long long sum = v[0];
	auto left = v.begin();
	auto right = v.begin();
	while (left != v.end()) {
		if (sum >= s) {



			if (len > (right - left) + 1) {
				len = right - left + 1;
			}

			if (len == 1) {
				break;
			}

			sum -= *left;
			left++;
		}
		else {
			right++;
			if (right == v.end()) {
				break;
			}
			sum += *right;
		}
	}
	if (len == n + 1) {
		len = 0;
	}
	cout << len;

	return 0;
}