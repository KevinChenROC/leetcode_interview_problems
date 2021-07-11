// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *head_L1 = l1;

        int carry = 0;
        while (l1 != nullptr && l2 != nullptr)
        {
            //update nodes
            int sum = carry + l1->val + l2->val;
            l1->val = sum % 10;
            carry = int(sum / 10);

            //create dummy node if neccesary
            if (l1->next != nullptr || l2->next != nullptr)
            {
                if (l1->next == nullptr)
                    l1->next = new ListNode(0);
                else if (l2->next == nullptr)
                    l2->next = new ListNode(0);
            }
            else if (l1->next == nullptr && l2->next == nullptr && carry > 0)
            {
                l1->next = new ListNode(carry);
            }

            l1 = l1->next;
            l2 = l2->next;
        }

        return head_L1; //because we update l1 in-place
    }
};