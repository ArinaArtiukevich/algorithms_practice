# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insert_into_BST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insert_into_BST(root.right, val)
        else:
            root.left = self.insert_into_BST(root.left, val)
        return root

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def _postorder(root: Optional[TreeNode]):
            if not root:
                return
            _postorder(root.left)
            _postorder(root.right)
            result.append(root.val)

        _postorder(root)
        return result


if __name__ == '__main__':
    bst = Solution()
    root = TreeNode(7)
    bst.insert_into_BST(root, 4)
    bst.insert_into_BST(root, 8)
    bst.insert_into_BST(root, 2)
    bst.insert_into_BST(root, 5)
    print(bst.postorderTraversal(root))
