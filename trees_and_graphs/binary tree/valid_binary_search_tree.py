# Test cases
# [2,1,3]
# [0]
# [2,2,2]
# [5,4,6,null,null,3,7]
# [0 ,-1 ,3 ,null, null, null, 6, 2 ,8  ]


class Solution(object):
    def isValid(self, root):
        """
        :rtype: (int, int, bool)
        """
        l_max = l_min = r_max = r_min = max_node = min_node = root.val
        r_validity = l_validity = validity = True

        # if we reach a single node
        if (not root.left) and (not root.right):
            return (min_node, max_node, True)

        if root.right:
            r_min, r_max, r_validity = self.isValid(root.right)
            # print("root.val = " + str(root.val))
            # print("root.right.val = " + str(root.right.val))
            # print("r_min = " + str(r_min))

            if root.val >= root.right.val or root.val >= r_min:
                validity = False

        if root.left:
            l_min, l_max, l_validity = self.isValid(root.left)

            if root.val <= root.left.val or root.val <= l_max:
                validity = False

        return (
            min(l_min, r_min, min_node),
            max(l_max, r_max, max_node),
            validity and l_validity and r_validity,
        )

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        _, _, validity = self.isValid(root)
        return validity
