#include <iostream>

using namespace std;

// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
    {
        // len(listA) = m
        // len(listB) = n
        /*
        key observations from examples
            1. The length w of the list starting at the intersection is constant
            2. m + w + n = n + w + m = const
        */

        //edge cases
        if (headA == NULL || headB == NULL)
            return NULL;

        ListNode *a = headA, *b = headB;
        while (a != b)
        {
            a = (a == NULL) ? headB : a->next;
            b = (b == NULL) ? headA : b->next;
        }
        return a;
    }
};
