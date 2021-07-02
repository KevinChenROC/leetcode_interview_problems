# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # edge case
        if not root:
            return []

        # use queue
        queue = []
        level_groups = [[root.val]]
        queue.append(root)

        while queue:
            group = []
            next_queue = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    group.append(node.left.val)
                    next_queue.append(node.left)
                if node.right:
                    group.append(node.right.val)
                    next_queue.append(node.right)

            if group:
                level_groups.append(group)
            queue = next_queue

        return level_groups
