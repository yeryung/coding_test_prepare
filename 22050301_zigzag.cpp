#include <iostream>
#include <string>
using namespace std;
int T, K, n, m;
string S;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> T;
    while (T > 0) {
        T--;
        cin >> S;
        cin >> K;
        n = S.length();
        m = 2 * K;
        for (int i = 0; i < K; i++) {
            for (int j = 0; j < n; j++) {
                if ((j * m) + i >= n) {
                    break;
                }
                cout << S[i + (j * m)];

                if ((j * m) + m - i - 1 >= n) {
                    break;
                }
                cout << S[(j * m) + m - i - 1];
            }
        }
        cout << '\n';
    }
    return 0;
}
