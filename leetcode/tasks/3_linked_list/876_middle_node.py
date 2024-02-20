from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node_custom(head: Optional[ListNode]) -> Optional[ListNode]:
    n = 0
    next_node = head
    result = head
    while next_node.next:
        next_node = next_node.next
        n += 1
    n = n / 2
    while n > 0 and result.next:
        result = result.next
        n -= 1
    return result


def middle_node_solution(head: Optional[ListNode]) -> Optional[ListNode]:
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


if __name__ == '__main__':
    n0 = ListNode(6)
    n1 = ListNode(5)
    n2 = ListNode(4, n1)
    n3 = ListNode(3, n2)
    n4 = ListNode(2, n3)
    n5 = ListNode(1, n4)
    head = n5
    print(middle_node_solution(head).val)
