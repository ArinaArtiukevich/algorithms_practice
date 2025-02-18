# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current_node = root
        parent_node = None
        while current_node:
            parent_node = current_node
            if current_node.val < val:
                current_node = current_node.right
            elif current_node.val > val:
                current_node = current_node.left
        if not parent_node:
            return TreeNode(val)
        if parent_node.val < val:
            parent_node.right = TreeNode(val)
        elif parent_node.val > val:
            parent_node.left = TreeNode(val)
        return root

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self._is_balanced_subtrees(root, [True, 0])[0]

    def _is_balanced_subtrees(self, root: Optional[TreeNode], result) -> [bool, int]:
        if not root:
            return [True, 0]
        result_right = self._is_balanced_subtrees(root.right, result)
        is_balanced_right, depth_right = result_right
        result_left = self._is_balanced_subtrees(root.left, result)
        is_balanced_left, depth_left = result_left
        return [is_balanced_right and is_balanced_left and abs(depth_right - depth_left) <= 1, max(depth_left, depth_right) + 1]


if __name__ == '__main__':
    bst = Solution()
    root = TreeNode(7)
    bst.insertIntoBST(root, 4)
    bst.insertIntoBST(root, 8)
    bst.insertIntoBST(root, 2)
    bst.insertIntoBST(root, 5)
    bst.insertIntoBST(root, 1)
    print(bst.isBalanced(root))
