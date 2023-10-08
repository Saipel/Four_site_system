

# функция делает из массива словарь, чтобы удобнее работать с перестановками
def list_to_dict(array: list) -> list:

    dict_array = []

    index = len(array) - 1

    while index >= 0:
        if array[index] != '0':
            if array[index] != '2':
                dict_array.append([index, array[index]])
            else:
                dict_array.append([index, 'd'])
                dict_array.append([index, 'u'])
        index -= 1

    #dict_array = dict(dict_array)
    return dict_array


# Функция определяет знак перед параметром перескока при заполнении матрицы гамильтониана
# Известны узлы между которыми происходит перескок, известны спины и количество электронов на узлах
# В таком случае возможны три варианта:
# 1) Одноэлектронный перескок. Тогда один узел будет пуст, на другом - один электрон
# 2) Одноэлектронный перскок из 2+0 в 1+1. Тогда на месте пустого узла будет электрон, совершивший перескок,
# следовательно берем его спин
# 3) Перескок из 2+1 в 1+2. Тогда спин перескочившего электрона будет противополжным спину одиночного эл-она.
# Метод решения задачи: определяем случай из выше перечисленных, составляем пару ключ и значение для поиска в словаре
# состояния, после чего находим позицию этого элемента (позиция элемента: есть количество перестановок
# оператора уничтожения), после этого элемет удаляется из словаря и находится позиция элемента с совпадающим спином,
# но другим узлом.
def calc_sign_translate(array_of_state: list, sec_array_of_state: list,position_1: int, position_2: int) -> str:

    dict_of_state = list_to_dict(array_of_state)
    sec_dict_of_state = list_to_dict(sec_array_of_state)
    ham_element = '0'

    if (array_of_state[position_1] == '0' or array_of_state[position_2] == '0') \
        and not (array_of_state[position_1] == '2' or array_of_state[position_2] == '2'):
        print("1+0")
        if array_of_state[position_1] == '0':
            print("Only if")
            # Исходя из условий отбора задается состояние оператора уничтожения
            # после чего находится позиция этого элемента в списке (позиция равна количеству перемещений)
            # Потом удаляется этот элемент
            # Потом вычисляется позиция элемента в состоянии в кторое был сделан переход (Работает для всех условий)

            sustein = [position_2, array_of_state[position_2]]
            number_of_trans = dict_of_state.index(sustein)
            print(number_of_trans)
            dict_of_state.remove(sustein)
            sec_sustein = [position_1, sec_array_of_state[position_1]]
            sec_number_of_trans = sec_dict_of_state.index(sec_sustein)
            print(sec_number_of_trans)
        else:
            print("Else")
            sustein = [position_1, array_of_state[position_1]]
            number_of_trans = dict_of_state.index(sustein)
            print(number_of_trans)

    if (array_of_state[position_1] == '2' and array_of_state[position_2] == '0') \
        or (array_of_state[position_1] == '0' and array_of_state[position_2] == '2'):
        print('2+0 is work')
        if array_of_state[position_1] == '0':
            print("Only if")
            sustein = [position_2, array_of_state[position_2]]
            number_of_trans = dict_of_state.index(sustein)
            print(number_of_trans)
        else:
            print("Else")
            sustein = [position_1, array_of_state[position_1]]
            number_of_trans = dict_of_state.index(sustein)
            print(number_of_trans)

    if (array_of_state[position_1] == '2' and (array_of_state[position_2] == 'd' or array_of_state[position_2] == 'u'))\
        or ((array_of_state[position_1] == 'd' or array_of_state[position_1] == 'u') and array_of_state[position_2] =='2'):
        print("2+1 is work")
        if array_of_state[position_1] == '2':
            print("Only if")
            sustein = [position_1, array_of_state[position_2]]
            number_of_trans = dict_of_state.index(sustein)
            print(sustein)
            print(number_of_trans)
        else:
            print("Else")
            sustein = [position_2, array_of_state[position_1]]
            number_of_trans = dict_of_state.index(sustein)
            print(sustein)
            print(number_of_trans)

    return ham_element

array = ['0', 'u', '2', '2']
sec_array = ['u', '0', '2', '2']

some_dict = list_to_dict(array)
print(some_dict)
print(list_to_dict(sec_array))

calc_sign_translate(array, sec_array, 0, 1)
