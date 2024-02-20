class StaticArray:
    def __init__(self):
        self.A = []
        self.size = 0

    # O[1]
    def __len__(self):
        return self.size

    # O[N]
    def copy(self, X):
        self.A = [item for item in X]
        self.size = len(self.A)

    # O[N]
    def _copy_forward(self, A, i, n, j):
        for index in range(n):
            A[i + index] = self.A[j + index]
        return A

    # O[N]
    def insert_at(self, item, i):
        A = [None for i in range(len(self.A) + 1)]
        self._copy_forward(A, 0, i, 0)
        A[i] = item
        self._copy_forward(A, i + 1, len(self.A) - i, i)
        self.copy(A)

    # O[N]
    def delete_at(self, i):
        A = [None for i in range(len(self.A) - 1)]
        self._copy_forward(A, 0, i, 0)
        self._copy_forward(A, i, len(self.A) - i - 1, i + 1)
        self.copy(A)

    # O[N]
    def insert_first(self, item):
        self.insert_at(item, 0)

    # O[N]
    def delete_first(self):
        self.delete_at(0)

    # O[N]
    def insert_last(self, item):
        self.insert_at(item, len(self.A))

    # O[N]
    def delete_last(self):
        self.delete_at(len(self.A))

    # O[1]
    def get_at(self, i):
        return self.A[i]

    # O[1]
    def set_at(self, item, i):
        self.A[i] = item


if __name__ == '__main__':
    sa = StaticArray()
    sa.copy([1, 3, 4, 5, 6])
    sa.insert_at(2, 1)
    sa.delete_at(0)
    print(sa.A)
