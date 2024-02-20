from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        head = result
        while list1 and list2:
            if list1.val <= list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next
        if list1:
            result.next = list1
        if list2:
            result.next = list2
        return head.next

    def merge_two_lists_recursion(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.merge_two_lists_recursion(list1.next, list2)
            return list1
        list2.next = self.merge_two_lists_recursion(list1, list2.next)
        return list2


if __name__ == '__main__':
    l_1_n_2 = ListNode(7)
    l_1_n_1 = ListNode(5, l_1_n_2)
    l_1_n_0 = ListNode(2, l_1_n_1)

    l_2_n_3 = ListNode(10)
    l_2_n_2 = ListNode(9, l_2_n_3)
    l_2_n_1 = ListNode(4, l_2_n_2)
    l_2_n_0 = ListNode(1, l_2_n_1)

    print(Solution().merge_two_lists(l_1_n_0, l_2_n_0))
