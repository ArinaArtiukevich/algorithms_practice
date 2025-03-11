from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class IterativeSolution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l, r = head, head
        stack_nodes = []
        while r:
            stack_nodes.append(r)
            r = r.next

        for _ in range(len(stack_nodes) // 2 + 1):
            insert_node = stack_nodes.pop()
            insert_node.next = l.next
            l.next = insert_node
            l = insert_node.next
        l.next = None


class RecursiveSolution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return head




if __name__ == '__main__':
    # l = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))

    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
    print(IterativeSolution().reorderList(l))
