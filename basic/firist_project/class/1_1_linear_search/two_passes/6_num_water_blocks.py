# яндекс, тренировки по алгоритмам 2, лекция 2, 35:00
# сколько блоков воды осталось в низинах

# вода ограничивается бортиками справа и слева => не выливается
# для каждого блока такие проверки будут слишком долгими


# р! итоговую форму после того как вода нальется => остров станет ступенчатым (без перепадов все низьменности)
# найдем самую высокую точку острова, до этой вершины ступеньки на подъем, вод асливается слева от вершины
# после => вправо

# идем слева, запоминаем текущую макс высоту столбика
# либо след макс, либо текущий макс, либо заполняем текущий макс - высота текущего столбика
#
# ищем глобальный макс
# правая часть
# левая  часть
# учитываем неск глобальных макс(между макс тоже заполняем, алгоритм сработает, но нужна проверка)

def get_num_water_blocks_custom(h: list[int]) -> int:
    if len(h) == 0:
        result = None
    else:
        result = 0
        global_max_i = 0
        for i in range(1, len(h)):
            if h[global_max_i] < h[i]:
                global_max_i = i
        local_max_h = h[0]
        for i in range(1, global_max_i):
            if local_max_h > h[i]:
                result += local_max_h - h[i]
            elif local_max_h < h[i]:
                local_max_h = h[i]
        reversed_range = list(range(global_max_i, len(h)))[::-1]
        local_max_h = h[reversed_range[0]]
        for i in reversed_range:
            if local_max_h > h[i]:
                result += local_max_h - h[i]
            elif local_max_h < h[i]:
                local_max_h = h[i]
    return result


def get_num_water_blocks_class(h: list[int]) -> int:
    global_max_i = 0
    result = 0
    for i in range(1, len(h)):
        if h[global_max_i] < h[i]:
            global_max_i = i
    local_max_h = 0
    for i in range(global_max_i):
        if local_max_h < h[i]:
            local_max_h = h[i]
        result += local_max_h - h[i]
    local_max_h = 0
    for i in range(len(h) - 1, global_max_i, -1):
        if local_max_h < h[i]:
            local_max_h = h[i]
        result += local_max_h - h[i]

    return result


if __name__ == "__main__":
    print(get_num_water_blocks_class([3, 1, 5, 3, 5, 1, 1, 3, 10]))
    print(list(range(10, 2, -1)))