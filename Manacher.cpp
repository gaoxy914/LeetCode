#include <iostream>
#include <string>
#include <vector>

using namespace std;

string manacher(string str) {
    string str_trans = "#";
    for (char c : str) {
        str_trans += c;
        str_trans += '#';
    }

    int n = str_trans.length();
    vector<int> p(n, 0);

    int maxRight = 0, center = 0;
    int maxLen = 1, start = 0;

    for (int i = 0; i < n; ++i) {
        if (i < maxRight) {
            int mirror = 2*center - i;
            p[i] = min(maxRight - i, p[mirror]);
        }
        int left = i - (1 + p[i]), right = i + (1 + p[i]);
        while (left >= 0 && right < n && str_trans[left] == str_trans[right]) {
            p[i]++;
            left--;
            right++;
        }

        if (i + p[i] > maxRight) {
            maxRight = i + p[i];
            center = i;
        }

        if (p[i] > maxLen) {
            maxLen = p[i];
            start = (i - maxLen) / 2;
        }
    }
    return str.substr(start, maxLen);
}

int main(int argc, char *argv[])
{
    string a = "abab";
    cout << manacher(a) << endl;
    return 0;
}
