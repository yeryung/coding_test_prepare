#include <iostream>
#include <stack>
using namespace std;
int T, N, Op, x;
stack<int>minStack, maxStack;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> T;
	while (T > 0) {
		T--;
		while (!minStack.empty() || !maxStack.empty()) {
			minStack.pop();
			maxStack.pop();
		}
		cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> Op;
			switch (Op) {
			case 1:
				cin >> x;
				if (minStack.empty() || maxStack.empty()) {
					minStack.push(x);
					maxStack.push(x);
				}
				else {
					minStack.push(min(minStack.top(), x));
					maxStack.push(max(maxStack.top(), x));
				}
				cout << minStack.top() << " " << maxStack.top() << '\n';
				break;
			case 2:
				if (minStack.empty() || maxStack.empty()) {
					continue;
				}
				else {
					minStack.pop();
					maxStack.pop();
					break;
				}
			}
		}
	}
	return 0;
}