class LinkedListNode:
    # O[1]
    def __init__(self, item):
        self.item = item
        self.next = None

    # O[i]
    def later_node(self, i):
        if i == 0:
            return self
        if self.next is None:
            raise IndexError('Invalid index')
        return self.next.later_node(i - 1)


class LinkedList:
    # O[1]
    def __init__(self):
        self.head = None
        self.size = 0

    # O[1]
    def __len__(self):
        return self.size

    # O[n]
    def __iter__(self):
        current_node = self.head
        while current_node:
            print(current_node.item)
            current_node = current_node.next

    # O[n]
    def copy(self, X):
        for item in reversed(X):
            self.insert_first(item)

    # O[1]
    def insert_first(self, item):
        new_node = LinkedListNode(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    # O[1]
    def delete_first(self):
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node

    # O[i]
    def insert_at(self, item, i):
        if i == 0:
            self.insert_first(item)
            return
        new_node = LinkedListNode(item)
        current_node = self.head.later_node(i - 1)
        new_node.next = current_node.next
        current_node.next = new_node
        self.size += 1

    # O[i]
    def delete_at(self, i):
        if i == 0:
            return self.delete_first()
        prev_node = self.head.later_node(i - 1)
        current_node = prev_node.next
        prev_node.next = current_node.next
        return current_node

    # O[N]
    def insert_last(self, item):
        self.insert_at(item, self.size)

    # O[N]
    def delete_last(self):
        self.delete_at(self.size)

    # O[i]
    def get_at(self, i):
        return self.head.later_node(i)

    # O[i]
    def set_at(self, item, i):
        current_node = self.head.later_node(i)
        current_node.item = item


if __name__ == '__main__':
    sa = LinkedList()
    sa.copy([1, 3, 4, 5, 6])
    sa.insert_at(2, 5)
    sa.get_at(5)
    print(sa.get_at(6).item)
    # sa.delete_at(0)
    # print(sa.__iter__())
