# include <iostream>
using namespace std;

int main() {
    int n, i, j, k, l, helper;
    cin >> n;

    int prefix[n];
    int z[n];

    for (int damn = 0; damn < n; damn++) {
        z[damn] = 0;
    }

    for (int damn = 0; damn < n; damn++) {
        cin >> prefix[damn];
    }

    while (i < n) {
        if(prefix[i]) {
            z[i - prefix[i] + 1] = prefix[i];
        }
        i++;
    }
    z[0] = n;
    for (int fuck = 0; fuck < n; fuck++) {
        cout << z[fuck] << " ";
    }
    if (z[1]) {
        j = 1;
        while (j < z[1]) {
            z[j + 1] = z[1] - j;
            j++;
        }
    }

    for (int fuck = 0; fuck < n; fuck++) {
        cout << z[fuck] << " ";
    }

    k = z[1] + 1;
    while (k < n - 1) {
        helper = k;
        if (z[k] && !z[k + 1]) {
            l = 1;
            while (l < z[k] && z[k + l] <= z[l]) {
                if (z[l] < z[k] - l) z[k + l] = z[l];
                else z[k + l] = z[k] - l;
                helper = k + l;
                l++;
            }
        }
        if (!(helper - k)) k++;
        else k = helper;
    }

    for (int fuck = 0; fuck < n; fuck++) {
        cout << z[fuck] << " ";
    }
}