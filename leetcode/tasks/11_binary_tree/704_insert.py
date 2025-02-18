from inspect import stack
from typing import Optional



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root


class IterativeSolution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = []
        current_node = root
        while current_node:
            stack.append(current_node)
            if current_node.val < val:
                current_node = current_node.right
            elif current_node.val > val:
                current_node = current_node.left
        current_node = TreeNode(val)
        while stack:
            parent_node = stack.pop()
            if current_node.val < parent_node.val:
                parent_node.left = current_node
            elif current_node.val > parent_node.val:
                parent_node.right = current_node
            current_node = parent_node
        return current_node


class IterativeSimplifiedSolution:
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



if __name__ == '__main__':
    bst = IterativeSolution()
    root = TreeNode(7)
    bst.insertIntoBST(root, 4)
    bst.insertIntoBST(root, 8)
    bst.insertIntoBST(root, 2)
    bst.insertIntoBST(root, 5)
    print(bst)


