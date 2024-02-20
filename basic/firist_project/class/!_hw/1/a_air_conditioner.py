
def start(t_room: int, t_cond: int, state: str) -> int:
    result = 0
    if state == 'freeze':
        result = min(t_room, t_cond)
    elif state == 'heat':
        result = max(t_room, t_cond)
    elif state == 'auto':
        result = t_cond
    return result



if __name__ == '__main__':
    nums = input()
    state = input()
    print(start(int(nums.split(' ')[0]), int(nums.split(' ')[1]), state))