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

class RecursionSolution(Solution):
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def _inorder(root):
            if not root:
                return
            _inorder(root.left)
            res.append(root.val)
            _inorder(root.right)
        _inorder(root)
        return res[k - 1]


class IterativeSolution(Solution):
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr_node = root
        stack = []
        while stack or curr_node:
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            curr_node = stack.pop()
            k -= 1
            if k == 0:
                return curr_node.val
            curr_node = curr_node.right
        return -1






if __name__ == '__main__':
    bst = IterativeSolution()
    root = TreeNode(7)
    bst.insertIntoBST(root, 4)
    bst.insertIntoBST(root, 8)
    bst.insertIntoBST(root, 2)
    bst.insertIntoBST(root, 5)
    bst.insertIntoBST(root, 1)
    print(bst.kthSmallest(root, 2))
