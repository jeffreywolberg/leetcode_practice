#include "../global_libraries.cpp"

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
   public:
    ListNode* makeLinkedList(int num) {
        vector<int> digits;
        int digit;
        int i = 0;
        string num_str = to_string(num);
        ListNode* head = new ListNode();
        ListNode* curNode = head;
        while (i < num_str.length()) {
            digit = (num / (int)pow(10, i++)) % 10;
            // smallest in front, largest in back
            curNode->val = digit;
            curNode->next = new ListNode();
            curNode = curNode->next;
        }

        curNode = head;
        while(curNode->next != nullptr) {
          curNode = curNode->next;
        }
        return head;
    }

    int getNumFromLinkedList(ListNode* l1) {
        int sum = 0;
        int i = 0;
        while (l1->next != nullptr) {
            sum += l1->val * (int)pow(10, i++);
            l1 = l1->next;
        }
        return sum;
    }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum1 = getNumFromLinkedList(l1);
        int sum2 = getNumFromLinkedList(l2);
        return makeLinkedList(sum1 + sum2);
    }
};

int main() {
    Solution sol = Solution();
    ListNode* n1 = sol.makeLinkedList(345);
    
    ListNode* n2 = sol.makeLinkedList(9805);
    ListNode* sum = sol.addTwoNumbers(n1, n2);
    cout << sol.getNumFromLinkedList(sum) << endl;
    return 0;
}