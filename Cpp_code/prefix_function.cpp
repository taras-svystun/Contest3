#include <iostream>
#include <cstring>
using namespace std;

int P[10];

void MaxBorderArray(char *s) {
    int i, j, len = strlen(s);
    P[0] = 0;
    for (i = 1; i < len; i++)
    {
        j = P[i - 1];
        while ((j > 0) && (s[i] != s[j]))
            j = P[j - 1];
        if (s[i] == s[j])
            j++;
        P[i] = j;
    }
}

int main() {
    string a = "";
}