#include "../global_libraries.cpp"
#include "queue"
#include <numeric>

class Row {
  public:
    int row;
    int strength;
    Row(int row, int strength) {
      this->row = row;
      this->strength = strength;
    }
  
    bool operator>(Row r2) const {
    if (this->strength == r2.strength) {
      return this->row > r2.row;
    }
    return this->strength > r2.strength;
    }

};


class Solution {

  public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
      vector<Row> rows;
    
      priority_queue<Row, vector<Row>, greater<Row>> pq;
      int m = mat.size();
      int n = mat[0].size();
        for (int i=0; i<m; i++) {
          vector<int> row = mat[i];
            int row_strength = std::accumulate(row.begin(), row.end(), 0);
            pq.push(Row(i, row_strength));
        }

        vector<int> output;
        for (int i=0; i<min(k, m); i++) {
          Row top = pq.top();
          pq.pop();
          output.push_back(top.row);
        }
        return output;
    }
};

int main() {
  vector<vector<int>> mat = {
    {1,1,0,0,0},
    {1,1,1,1,0},
    {1,0,0,0,0},
    {1,1,0,0,0},
    {1,1,1,1,1}
  };

  vector<int> rows = Solution().kWeakestRows(mat, 5);
  for (int row_num : rows) {
    cout << row_num << " " << endl;
  }
  return 0;

}