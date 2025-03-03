from typing import Optional, List

from pandas.core.computation.common import result_type_many


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Insertion:
    def insert_into_BST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insert_into_BST(root.right, val)
        else:
            root.left = self.insert_into_BST(root.left, val)
        return root


class RecursiveSolution(Insertion):
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def _preorder(root: Optional[TreeNode]) -> List[int]:
            if not root:
                return
            arr.append(root.val)
            _preorder(root.left)
            _preorder(root.right)
            return arr

        return _preorder(root)


class IterativeSolution(Insertion):
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes_stack = [root]
        result = []
        while nodes_stack:
            current_node = nodes_stack.pop()
            if current_node:
                result.append(current_node.val)
                if current_node.right:
                    nodes_stack.append(current_node.right)
                if current_node.left:
                    nodes_stack.append(current_node.left)

        return result


if __name__ == '__main__':
    bst = IterativeSolution()
    root = TreeNode(7)
    bst.insert_into_BST(root, 4)
    bst.insert_into_BST(root, 8)
    bst.insert_into_BST(root, 2)
    bst.insert_into_BST(root, 5)
    print(bst.preorderTraversal(root))
