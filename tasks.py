def task_1(values):
    match values:
        case 1: print(f'{values} компьютер')
        case 2 | 3 | 4: print(f'{values} компьютера')
        case 5 | 6 | 7 | 8 | 9 | 0: print(f'{values} компьютеров')


def task_1_1(values):
    if values % 10 in [2, 3, 4]:
        print(f'{values} компьютера')
    elif values % 10 == 1:
        print(f'{values} компьютер')
    else:
        print(f'{values} компьютеров')


def task_2(value_list):
    pass


def task_3(value_list):
    result = []
    for i in value_list:
        if i % 2 == 0 or i % 3 == 0:
            continue
        elif i // 1 == i and i // i == 1:
            result.append(i)
        else:
            pass
    return result


def task_4(value):
    for i in range(1, (value + 1)):
        for j in range(1, (value + 1)):
            print("%4d" % (i * j), end="")
        print()

