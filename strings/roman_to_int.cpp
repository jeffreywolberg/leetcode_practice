#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        // convert to chars
        vector<char> v(s.begin(), s.end());
        vector<string> special = {"CM", "CD", "XL", "XC", "IV", "IX"};
        map<char, int> mapping = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        
        vector<int> positions;
        int sum = 0;
        int i = 0;
        for (string &sp : special) {
            size_t pos;
            // sp = "TMP";
            // cout << sp << " " << special[i] << endl;

            if ((pos = s.find(sp)) != string::npos) {
                cout << pos << " " << sp << " " << s << endl;
                positions.push_back(pos);
            }
            i++;
        }
        i = 0;
        for (char &c : s) {
            if (positions.size() > 0) {
                if (i == positions[0]) {
                    i += 1;
                    sum -= mapping.at(c);
                    cout << c << " " << mapping.at(c) << " " << sum << endl;
                    continue;
                }
                else if (i-1 == positions[0]) {
                    i += 1;
                    positions.erase(positions.begin());
                    sum += mapping.at(c);
                    cout << c << " " << mapping.at(c) << " " << sum << endl;
                    continue;
                }
            }
            sum += mapping.at(c);
            cout << c << " " << mapping.at(c) << " " << sum << endl;
            i += 1;
        }
        return sum;
    }
};

int main() {
    Solution sol = Solution();
    int num = sol.romanToInt("MCMXCIV");
    cout << num << endl;
    return 0;
}