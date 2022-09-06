#include "../global_libraries.cpp"

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
      map<char, int> magazineMap;
      vector<char> mapKeys;
      for (char c : magazine) {
        if (find(mapKeys.begin(), mapKeys.end(), c) != mapKeys.end()) {
          magazineMap[c] += 1;
        }
        else {
          mapKeys.push_back(c);
          magazineMap.insert(pair<char, int>(c, 1));
        }
      }
      
      for (char c: ransomNote) {
        vector<char>::iterator pos;
        if ((pos = find(mapKeys.begin(), mapKeys.end(), c)) != mapKeys.end()) {
          magazineMap[c] -= 1;
          if (magazineMap[c] == 0) {
            mapKeys.erase(pos);
          }
        }
        else {
          return false;
        }
      }

      return true;
    }
};

int main() {
  string note = "abcdddd";
  string magazine = "ddbdca";
  bool canConstruct = Solution().canConstruct(note, magazine);
  cout << "Can construct: " << canConstruct << endl;
}