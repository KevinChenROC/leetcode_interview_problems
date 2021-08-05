//[Ref]
//  1. https://www.geeksforgeeks.org/avl-tree-set-1-insertion/

// ==================Righ and Left rotations=============================

/*
     y                               x
    / \     Right Rotation          /  \
   x   T3   - - - - - - - >        T1   y 
  / \       < - - - - - - -            / \
 T1  T2     Left Rotation            T2  T3

*/

// ==========================Steps to follow for insertion==========================
/*

Let the newly inserted node be w
1) Perform standard BST insert for w.

2) Starting from w, travel up and find the first unbalanced node. Let z be the first unbalanced node, y be the child of z that comes on the path from w to z and x be the grandchild of z that comes on the path from w to z.

3) Re-balance the tree by performing appropriate rotations on the subtree rooted with z. 

There can be 4 possible cases:

a) y is left child of z and x is left child of y (Left Left Case)
b) y is left child of z and x is right child of y (Left Right Case)
c) y is right child of z and x is right child of y (Right Right Case)
d) y is right child of z and x is left child of y (Right Left Case)

======Left left case=========
T1, T2, T3 and T4 are subtrees.
         z                                      y 
        / \                                   /   \
       y   T4      Right Rotate (z)          x      z
      / \          - - - - - - - - ->      /  \    /  \ 
     x   T3                               T1  T2  T3  T4
    / \
  T1   T2

*/

#include <iostream>
#include <algorithm>
using namespace std;

class Node
{
public:
    int key;
    int height;
    Node *left;
    Node *right;
    Node(int key) : key(key), left(nullptr), right(nullptr), height(1) {}
};

int height(Node *N)
{
    if (N == nullptr)
        return 0;
    return N->height;
}

int getBalance(Node *N)
{
    if (N == nullptr)
        return 0;
    return height(N->left) - height(N->right);
}

Node *rightRotate(Node *y)
{
    Node *x = y->left;
    Node *T2 = x->right;

    // Perform rotation
    x->right = y;
    y->left = T2;

    // Update heights
    y->height = max(height(y->left),
                    height(y->right)) +
                1;
    x->height = max(height(x->left),
                    height(x->right)) +
                1;

    // Return new root
    return x;
}

Node *leftRotate(Node *x)
{
    Node *y = x->right;
    Node *T2 = y->left;

    // Perform rotation
    y->left = x;
    x->right = T2;

    // Update heights
    y->height = max(height(y->left),
                    height(y->right)) +
                1;
    x->height = max(height(x->left),
                    height(x->right)) +
                1;

    // Return new root
    return y;
}

Node *insert(Node *node, int key)
{
    /* 1. Perform the normal BST insertion */
    if (node == nullptr)
        return (new Node(key));

    if (key < node->key)
        node->left = insert(node->left, key);
    else if (key > node->key)
        node->right = insert(node->right, key);
    else // Equal keys are not allowed in BST
        return node;

    /* 2. Update height of this ancestor node */
    node->height = 1 + max(height(node->left),
                           height(node->right));

    /* 3. Get the balance factor of this ancestor
		node to check whether this node became
		unbalanced */

    int balance = getBalance(node);

    // If this node becomes unbalanced, then
    // there are 4 cases

    // Left Left Case
    if (balance > 1 && key < node->left->key)
        return rightRotate(node);

    // Right Right Case
    if (balance < -1 && key > node->right->key)
        return leftRotate(node);

    // Left Right Case
    if (balance > 1 && key > node->left->key)
    {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    // Right Left Case
    if (balance < -1 && key < node->right->key)
    {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    /* return the (unchanged) node pointer */
    return node;
}

/* Given a non-empty binary search tree,
return the node with minimum key value
found in that tree. Note that the entire
tree does not need to be searched. */
Node *minValueNode(Node *node)
{
    Node *current = node;

    /* loop down to find the leftmost leaf */
    while (current->left != nullptr)
        current = current->left;

    return current;
}

Node *deleteNode(Node *root, int key)
{

    // STEP 1: PERFORM STANDARD BST DELETE
    if (root == nullptr)
        return root;

    // If the key to be deleted is smaller
    // than the root's key, then it lies
    // in left subtree
    if (key < root->key)
        root->left = deleteNode(root->left, key);

    // If the key to be deleted is greater
    // than the root's key, then it lies
    // in right subtree
    else if (key > root->key)
        root->right = deleteNode(root->right, key);

    // if key is same as root's key, then
    // This is the node to be deleted
    else
    {
        // node with only one child or no child
        if ((root->left == nullptr) ||
            (root->right == nullptr))
        {
            Node *temp = root->left ? root->left : root->right;

            // No child case
            if (temp == nullptr)
            {
                temp = root;
                root = nullptr;
            }
            else               // One child case
                *root = *temp; // Copy the contents of
                               // the non-empty child
            delete temp;
        }
        else
        {
            // node with two children: Get the inorder
            // successor (smallest in the right subtree)
            Node *temp = minValueNode(root->right);

            // Copy the inorder successor's
            // data to this node
            root->key = temp->key;

            // Delete the inorder successor
            root->right = deleteNode(root->right,
                                     temp->key);
        }
    }

    // If the tree had only one node
    // then return
    if (root == nullptr)
        return root;

    // STEP 2: UPDATE HEIGHT OF THE CURRENT NODE
    root->height = 1 + max(height(root->left),
                           height(root->right));

    // STEP 3: GET THE BALANCE FACTOR OF
    // THIS NODE (to check whether this
    // node became unbalanced)
    int balance = getBalance(root);

    // If this node becomes unbalanced,
    // then there are 4 cases

    // Left Left Case
    if (balance > 1 &&
        getBalance(root->left) >= 0)
        return rightRotate(root);

    // Left Right Case
    if (balance > 1 &&
        getBalance(root->left) < 0)
    {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }

    // Right Right Case
    if (balance < -1 &&
        getBalance(root->right) <= 0)
        return leftRotate(root);

    // Right Left Case
    if (balance < -1 &&
        getBalance(root->right) > 0)
    {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }

    return root;
}

void preOrder(Node *root)
{
    if (root != nullptr)
    {
        cout << root->key << " ";
        preOrder(root->left);
        preOrder(root->right);
    }
}

int main()
{
    Node *root = nullptr;
    /* Constructing tree given in
    the above figure */
    root = insert(root, 9);
    root = insert(root, 5);
    root = insert(root, 10);
    root = insert(root, 0);
    root = insert(root, 6);
    root = insert(root, 11);
    root = insert(root, -1);
    root = insert(root, 1);
    root = insert(root, 2);

    /* The constructed AVL Tree would be
            9
           / \
          1  10
         / \  \
        0  5  11
        / / \
      -1 2   6
    
    */

    cout << "Preorder traversal of the "
            "constructed AVL tree is \n";
    preOrder(root);

    root = deleteNode(root, 10);

    /* The AVL Tree after deletion of 10
            1
           / \
          0   9
         /   / \
       -1   5   11
           / \
          2   6
    */

    cout << "\nPreorder traversal after"
         << " deletion of 10 \n";
    preOrder(root);

    return 0;
}