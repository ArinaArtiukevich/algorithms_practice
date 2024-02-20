class DynamicArray:
    def __init__(self):
        self.A = []
        self.size = 0
        self.r = 2
        self.upper: int
        self.lower: int
        self._compute_boundaries()
        self._resize(0)

    # O[n]
    def _copy_forward(self, i, n, A, j):
        for ind in range(n):
            A[i + ind] = self.A[j + ind]

    # O[n]
    def _copy_backward(self, i, n, A, j):
        for ind in range(n):
            A[i - ind] = self.A[j - ind]

    def _compute_boundaries(self):
        self.lower = len(self.A) // self.r
        self.upper = len(self.A)

    # O[n]
    def _resize(self, n):
        if self.lower < n < self.upper:
            return
        n = max(n, 1)
        A = [None for _ in range(n * self.r)]
        self._copy_forward(0, self.size, A, 0)
        self.A = A
        self._compute_boundaries()

    # O[1]a
    def insert_last(self, x):
        self._resize(self.size + 1)
        self.A[self.size] = x
        self.size += 1

    # O[n]
    def copy(self, X):
        for x in X:
            self.insert_last(x)

    # O[1]a
    def delete_last(self):
        self.A[self.size - 1] = None
        self.size -= 1
        self._resize(self.size)

    # custom
    # def insert_at(self, x, i):
    #     if i == self.size:
    #         self.insert_last(x)
    #         return
    #     self._resize(self.size + 1)
    #     A = [None for _ in range(len(self.A))]
    #     self._copy_forward(0, i, A, 0)
    #     A[i] = x
    #     self._copy_forward(i + 1, self.size - i, A, i)
    #     self.A = A
    #     self.size += 1

    # O[n]
    def insert_at(self, x, i):
        self.insert_last(None)
        self._copy_backward(self.size, self.size - i + 1, self.A, self.size - 1)
        self.A[i] = x
        self.size += 1

    # O[n]
    def delete_at(self, i):
        self._copy_forward(i, self.size - i - 1, self.A, i + 1)
        self.delete_last()

    # O[n]
    def insert_first(self, x):
        self.insert_at(x, 0)

    # O[n]
    def delete_first(self):
        self.delete_at(0)


if __name__ == '__main__':
    sa = DynamicArray()
    sa.copy([1])
    sa.insert_last(2)
    sa.insert_last(3)
    sa.insert_last(4)
    # sa.delete_last()
    # sa.delete_last()
    # sa.delete_last()

    sa.insert_at(5, 4)
    sa.insert_at(6, 5)
    #
    sa.insert_at(6, 2)
    sa.insert_at(6, 1)
    sa.delete_at(1)
    sa.delete_at(2)

    sa.delete_at(7)

    print(sa.A)
