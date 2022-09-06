#include "../global_libraries.cpp"

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
        
        int sum = 0;
        int i = 0;
        while(i < s.length()) {
            if (find(special.begin(), special.end(), s.substr(i, 2)) != special.end()) {
                sum -= mapping.at(s[i]);
                sum += mapping.at(s[i+1]);
                i += 2;
            }
            else {
                sum += mapping.at(s[i]);
                i += 1;
            }
        }
        return sum;
    }
};

int main() {
    int num = Solution().romanToInt("LVIII");
    cout << num << endl;
    return 0;
}