#include <iostream>
#include <string>

using namespace std;

int KMP(string s, string p) {
    int* next = new int[p.length()];
    next[0] = 0;
    int i = 1, now = 0;
    while (i < p.length()) {
        if (p[now] == p[i])
            next[i++] = ++now;
        else {
            if (now == 0) next[i++] = 0;
            else now = next[now - 1];
        }
    }
    /* for (int i = 0; i < p.length(); ++i)
        cout << next[i] << " ";
    cout << endl; */

    i = 0; int j = 0;
    while (i < s.length() && j < p.length()) {
        if (s[i] == p[j]) {
            ++i; ++j;
        } else {
            j = j == 0 ? 0 : next[j - 1];
        }
    }
    if (j == p.length()) return i - j;
    return -1;
}

int main(int argc, char *argv[])
{
    string s = "ababaabaabac";
    string p = "abaabac";
    cout << KMP(s, p) << endl;
    return 0;
}
