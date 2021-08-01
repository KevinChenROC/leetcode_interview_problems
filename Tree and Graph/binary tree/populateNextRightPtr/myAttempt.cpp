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

        queue<Node *> q;
        q.push(root);

        Node *curNode = nullptr;
        int curNumOfNodes = 1, nextNumOfNodes = 0;
        while (!q.empty())
        {
            curNode = q.front();
            q.pop();
            curNumOfNodes--;

            //add to q the left and right child nodes if any
            if (curNode->left != nullptr)
            {
                nextNumOfNodes++;
                q.push(curNode->left);
            }
            if (curNode->right != nullptr)
            {
                nextNumOfNodes++;
                q.push(curNode->right);
            }

            if (curNumOfNodes > 0)
                curNode->next = q.front();
            else
            {
                curNumOfNodes = nextNumOfNodes;
                nextNumOfNodes = 0;
            }
        }
        return root;
    }
};