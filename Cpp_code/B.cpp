# include <bits/stdc++.h>
using namespace std;
string str;
int max_power(string str) {
    int i, l, r, res = 1;
    int n = (int) str.length();
    vector<int> z(n, 0);
    for (i = 1, l = 0, r = 0; i < n; i++) {
        if (i <= r) z[i] = min(r - i + 1, z[i - l]);
        while (i + z[i] < n && str[z[i]] == str[i + z[i]]) z[i]++;
        if (i + z[i] - 1 > r) l = i, r = i + z[i] - 1;
        if (i + z[i] == n && n % i == 0) {
            if (n / i > res) res = (int) n / i;
        }
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    while(getline(cin, str)) {
        cout << max_power(str) << "\n";
    }
    return 0;
}