#include "../global_libraries.cpp"

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    bool isPalindrome(ListNode* head) {
      ListNode* curNode = head;
      int i = 0;
      while (curNode->next != nullptr) {
        // cout << curNode->val << endl;
        curNode = curNode->next;
        i += 1;
      }
      int length = i+1;

      vector<int> stack;
      i = 0;
      curNode = head;
      while (i < int(length / 2)) {
        stack.push_back(curNode->val);
        curNode = curNode->next;
        i += 1;
      }

      if (length % 2 == 1) {
        i += 1;
        curNode = curNode->next;
      }

      // cout << "Length of stack: " << stack.size() << " " << endl;

      while (stack.size() > 0) {
        int popped_char = stack.back();
        stack.pop_back();
        // cout << "Popped char: " << popped_char << ", curNode val: " << curNode->val << endl;
        if (popped_char != (char) curNode->val) {
          return false;
        }
        curNode = curNode->next;
      }
      return true;



      return 0;
    }
};

int main() {
  
  vector<int> s = {1, 2, 1, 3, 2, 1};

  ListNode *head =  new ListNode(s[0]);
  ListNode* curNode = head;
  int i=1;
  while (i<s.size()) {
    curNode->next = new ListNode(s[i]);
    curNode = curNode->next;
    i+=1;
  }
  
  bool isPalindrome = Solution().isPalindrome(head);
  cout << "is palindrome? " << isPalindrome << endl;
  return 0;  
}