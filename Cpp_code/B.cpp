#include <iostream>
#include <string>
using namespace std;

int start, finish, length;
string prefix, sub;

int max_power_prefix(string line) {
    length = (int) line.size();

    // cout << "Here " <<line.substr(0, 1) << "  " << line.substr(1, 2) << endl;
    for (int i = 1; i < length; i++) {
        prefix = line.substr(0, i);
        cout << prefix << endl;
        start = i;
        finish = 2 * i - 1;
        cout << start << " " << finish << endl;

        // sub = line.substr(start, finish);
        while (finish < length) {
            
            cout << "LOOP " <<start << " " << finish << endl;
            sub = line.substr(start, finish);
            int sub_len = (int) sub.size();
            if (sub_len != i) {
                sub = line.substr(start, finish - 1);
            }

            cout << " SUB = " << sub << endl;
            if (prefix != sub) break;
            start += i;
            finish += i;
        }
        cout << start << " " << finish << endl;
        sub = line.substr(start, finish);
        if (finish == length - 1 && prefix == sub)
            return length / i;
    }
    return 1;
}


int main() {
    string test;
    while (getline(cin, test)) {
        cout << max_power_prefix(test) << endl;
    }
    return 0;
}