def custom_hash(num: int) -> int:
    return num % 10


class CustomSet:
    def __init__(self):
        self.custom_set = {}

    def add_element(self, num: int):
        hash_num = custom_hash(num)
        if hash_num in self.custom_set:
            if not self.find_element(num):
                self.custom_set[hash_num].append(num)
        else:
            self.custom_set[hash_num] = [num]

    def find_element(self, num: int) -> bool:
        hash_num = custom_hash(num)
        if (hash_num in self.custom_set) and (num in self.custom_set[hash_num]):
            return True
        return False

    def delete_element(self, num: int) -> bool:
        if self.find_element(num):
            for i, element in enumerate(self.custom_set[custom_hash(num)]):
                if element == num:
                    self.custom_set[custom_hash(num)][i] = self.custom_set[custom_hash(num)][
                        len(self.custom_set[custom_hash(num)]) - 1]
                    self.custom_set[custom_hash(num)].pop(len(self.custom_set[custom_hash(num)]) - 1)
                    return True
        return False


if __name__ == '__main__':
    cs = CustomSet()
    cs.add_element(7)
    cs.add_element(1)
    cs.add_element(17)
    cs.add_element(117)
    cs.add_element(7)
    cs.delete_element(7)

    print(cs.custom_set)
