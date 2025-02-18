# Definition for a binary tree node.
from asyncio import current_task
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insert_into_BST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]):
        ...



if __name__ == '__main__':
    bst = RecursionSolution()

    root_1 = TreeNode(1)
    bst.insert_into_BST(root_1, 3)
    bst.insert_into_BST(root_1, 2)
    bst.insert_into_BST(root_1, 5)

    root_2 = TreeNode(2)
    bst.insert_into_BST(root_2, 1)
    bst.insert_into_BST(root_2, 3)
    bst.insert_into_BST(root_2, 4)
    bst.insert_into_BST(root_2, 7)


    print(bst.mergeTrees(root_1, root_2))
