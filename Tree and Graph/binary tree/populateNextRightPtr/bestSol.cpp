// Definition for a Node.
class Node
{
public:
    int val;
    Node *left;
    Node *right;
    Node *next;

    Node() : val(0), left(nullptr), right(nullptr), next(nullptr) {}

    Node(int _val) : val(_val), left(nullptr), right(nullptr), next(nullptr) {}

    Node(int _val, Node *_left, Node *_right, Node *_next)
        : val(_val), left(_left), right(_right), next(_next) {}
};

#include <queue>

using namespace std;

class Solution
{
public:
    Node *connect(Node *root)
    {
        if (root == nullptr)
            return root;
        Node *pre = root;
        Node *cur = nullptr;

        //assume a complete binary tree, where each level has no empty leaves.
        while (pre->left)
        {
            cur = pre;
            while (cur)
            {
                cur->left->next = cur->right;
                if (cur->next)
                    cur->right->next = cur->next->left;
                cur = cur->next;
            }
            pre = pre->left;
        }

        return root;
    }
};