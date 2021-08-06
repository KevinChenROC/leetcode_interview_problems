// Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

// The first node is considered odd, and the second node is even, and so on.

/*
Requirements
    1. Note that the relative order inside both the even and odd groups should remain as it was in the input.

    2. You must solve the problem in O(1) extra space complexity and O(n) time complexity.
*/

#include <iostream>

using namespace std;
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
    ListNode *oddEvenList(ListNode *head)
    {
        //edge cases
        if (head == nullptr || head->next == nullptr)
            return head;

        ListNode *oddHead = head, *evenHead = head->next;
        ListNode *oddNode = oddHead, *evenNode = evenHead;
        unsigned int idx = 3; //current idx of the node, from 1 to n
        head = head->next->next;
        while (head != nullptr)
        {
            cout << "head->val: " << head->val << endl;
            if (idx % 2 == 1)
            {
                //odd
                oddNode->next = head;
                oddNode = head;
            }
            else
            {
                //even
                evenNode->next = head;
                evenNode = head;
            }
            head = head->next;
            idx++;
        }
        evenNode->next = nullptr;
        oddNode->next = evenHead;
        return oddHead;
    }
};

ListNode *append(ListNode *head, int val)
{
    if (head == nullptr)
    {
        return (new ListNode(val));
    }

    ListNode *curNode = head;
    while (curNode->next)
        curNode = curNode->next;

    curNode->next = new ListNode(val);

    return head;
}

void printAllNodes(const ListNode *head)
{
    while (head)
    {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}

int main(int argc, char const *argv[])
{
    ListNode *head = append(nullptr, 1);
    head = append(head, 2);
    head = append(head, 3);
    head = append(head, 4);
    head = append(head, 5);

    Solution sol;
    head = sol.oddEvenList(head);
    printAllNodes(head);

    return 0;
}
