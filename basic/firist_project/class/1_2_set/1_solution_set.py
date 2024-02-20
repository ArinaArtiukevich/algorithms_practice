set_size = 10
custom_set = [[] for _ in range(set_size)]


def add_element(num: int):
    if not find_element(num):
        custom_set[num % set_size].append(num)


def find_element(num: int):
    hash_num = num % set_size
    for value in custom_set[hash_num]:
        if num == value:
            return True
    return False


def delete_element(num: int):
    current_list = custom_set[num % set_size]
    for i in range(len(current_list)):
        if current_list[i] == num:
            current_list[i] = current_list[len(current_list) - 1]
            current_list.pop()
