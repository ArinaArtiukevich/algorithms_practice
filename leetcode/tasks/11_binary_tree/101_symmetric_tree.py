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

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self._is_symmetric_subtrees(root.left, root.right)

    def _is_symmetric_subtrees(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if (left and not right) or (not left and right):
            return False
        if not (left and right):
            return True
        if left.val != right.val:
            return False
        return self._is_symmetric_subtrees(left.left, right.right) and self._is_symmetric_subtrees(left.right, right.left)



if __name__ == '__main__':
    bst = Solution()
    root = TreeNode(7)
    bst.insertIntoBST(root, 4)
    bst.insertIntoBST(root, 8)
    bst.insertIntoBST(root, 2)
    bst.insertIntoBST(root, 5)
    print(bst.isSymmetric(root))
