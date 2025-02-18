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


    def _is_valid_left_subtree(self, current_node: Optional[TreeNode], root: Optional[TreeNode]) -> bool:
        if not current_node:
            return True
        if root.val <= current_node.val:
            return False
        return self._is_valid_left_subtree(current_node.right, root) and self._is_valid_left_subtree(current_node.left, root)

    def _is_valid_right_subtree(self, current_node: Optional[TreeNode], root: Optional[TreeNode]) -> bool:
        if not current_node:
            return True
        if root.val >= current_node.val:
            return False
        return self._is_valid_right_subtree(current_node.right, root) and self._is_valid_right_subtree(current_node.left, root)

# O(n^2)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not self._is_valid_right_subtree(root.right, root) or not self._is_valid_left_subtree(root.left, root):
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

# O(n)
    def isValidBSTSolution(self, root: Optional[TreeNode]) -> bool:
        return self._is_valid_solution(root, float('-inf'), float('inf'))

    def _is_valid_solution(self, root: Optional[TreeNode], min_boundary: float, max_boundary: float) -> bool:
        if not root:
            return True
        if not (max_boundary > root.val > min_boundary):
            return False
        return self._is_valid_solution(root.right, root.val, max_boundary) and self._is_valid_solution(root.left, min_boundary, root.val)


if __name__ == '__main__':
    bst = Solution()
    root = TreeNode(7)
    bst.insertIntoBST(root, 4)
    bst.insertIntoBST(root, 8)
    bst.insertIntoBST(root, 2)
    bst.insertIntoBST(root, 5)
    print(bst.isValidBSTSolution(root))
