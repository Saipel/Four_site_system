import numpy as np

from ham_and_array import *


def double_array(array = None):
    a = np.random.rand(6, 6)
    print(a)
    bind = 0
    for i in range(0, len(a[0])):
        for j in range(bind + 1, len(a[0])):
            print(a[i][j])
        print("\n")
        bind += 1

# функция проверяет заполненость всех узлов одноэлектронными состояниями
def all_sites_is_full(array: list) -> bool:
    check_value = True
    increm = 0

    for sites in range(4):
        if array[sites] != '0' and array[sites] != '2':
            increm += 1

    if increm == 4:
        check_value = False

    return check_value

# функция проверяет заполненость соседних  узлов одноэлектронными состояниями
def neighbor_sites_is_full(array: list, first_site: int, sec_site: int) -> bool:

    check_value = True
    increm = 0

    for sites in range(first_site, sec_site + 1):
        if array[sites] != '0' and array[sites] != '2':
            increm += 1

    if increm == 2:
        check_value = False

    return check_value


def auto_complete_ham(basis: list, array_index: int):
    """
    # %======================================================================================================
    # функция должна автоматически заполнять матрицы гамильтонианов
    # Возможные связи узлов {
    # 1 и 2 (1d\sigma 2c\sigma); 1 и 4
    # 2 и 1; 2 и 3
    # 3 и 2; 3 и 4
    # 4 и 3; 4 и 1
    # } \sigma = u,d
    # Возможная запись 1dd и 2cd.
    # После эта схема разбивается командой list на массив элементов.
    # Первый элемент массива указывает узел, второй - действие с электроном, третий - спин электрона
    # %======================================================================================================
    # Заполнение матриц гамильтониана происходит в двух циклах. Заполняться будет только верхняя половина матрицы.
    # работа с базисом.
    # После применения функции в каждый элемент массива разбивается на подмассив из четырех элементов.
    # %======================================================================================================
    # Постановка условия для определения состояний между которыми есть перескок:
        если первый элемент массива равен второму или четвертому; второй равен первому или третьему;
        третий равен второму или четвертому; четвертый равен третьему или первому. (необходимо сравнивать связку элементов...)
        Если перескок произошел с первого узла на второй (при одном электроне), то сранивается первый узел со вторым и наоборот в одной итерации\
        basis_index_line = 0 #переменная отвечает за перемещение по горизонтальным эдементам
        basis_index_column = 0 #переменная отвечает за перемещение по вертикальным элементам
    # %======================================================================================================
    # Необходимо учесть заполненность узлов в состоянии. Есть функция, которая считает количество не
    # нулевых узлов (необходимо учитывать 2х электронные состояния на узлах.)
    """

    """
        # Неприятная конструкция. basis[номер рассматриваемого случая - количество частиц в системе минус - 1]
        #                               [номер состояния базиса, для каждого массива уникален, отсчет начинается с 1го элемента]
        #                               [номер узла, задаетсяв диапазоне от 0 до 3х. В цикле range(0,4), чтобы затрагивался последний элемент] 
    """

    bias_column = 0
    for basis_index_line in range(len(basis[array_index])):
        for basis_index_column in range(bias_column + 1, int(len(basis[array_index]))):

            # Сравниваем первый и второй узел
            if all_sites_is_full(basis[array_index][basis_index_line]) or all_sites_is_full(
                    basis[array_index][basis_index_column]):
                # Отвечает за переходы из стостояний 2+0 в d+u(u+d)
                if (((((basis[array_index][basis_index_line][0] == 'u' and basis[array_index][basis_index_line][1] == 'd')
                       or (basis[array_index][basis_index_line][0] == 'd' and basis[array_index][basis_index_line][1] == 'u'))
                      and ((basis[array_index][basis_index_column][0] == '2' and basis[array_index][basis_index_column][1] == '0'
                        or basis[array_index][basis_index_column][0] == '0' and basis[array_index][basis_index_column][1] == '2')))
                     and (basis[array_index][basis_index_line][2] == basis[array_index][basis_index_column][2]
                          and basis[array_index][basis_index_line][3] == basis[array_index][basis_index_column][3]))
                        or
                        ((((basis[array_index][basis_index_column][0] == 'u' and basis[array_index][basis_index_column][1] == 'd')
                           or (basis[array_index][basis_index_column][0] == 'd' and basis[array_index][basis_index_column][1] == 'u'))
                          and ((basis[array_index][basis_index_line][0] == 2 and basis[array_index][basis_index_line][1] == '0'
                             or basis[array_index][basis_index_line][0] == '0' and basis[array_index][basis_index_line][1] == '2'))
                          and (basis[array_index][basis_index_line][2] == basis[array_index][basis_index_column][2]
                               and basis[array_index][basis_index_line][3] == basis[array_index][basis_index_column][3])))
                ):
                    print("it is work! (2+0)")
                    print(basis[array_index][basis_index_line])
                    print(basis[array_index][basis_index_column])

                # Отвечает за перескоки u+0 в 0+u
                if (((basis[array_index][basis_index_line][0] == basis[array_index][basis_index_column][1]
                      and basis[array_index][basis_index_line][1] == basis[array_index][basis_index_column][0])
                     and not ((basis[array_index][basis_index_line][0] == '2' and basis[array_index][basis_index_line][1] == '0')
                              or (basis[array_index][basis_index_line][0] == '0' and basis[array_index][basis_index_line][1] == '2')))
                        and (basis[array_index][basis_index_line][2] == basis[array_index][basis_index_column][2]
                             and basis[array_index][basis_index_line][3] == basis[array_index][basis_index_column][3])
                        and neighbor_sites_is_full(basis[array_index][basis_index_line], 0, 1)
                    ):
                    print("It is work! (solo translate)")
                    print(basis[array_index][basis_index_line])
                    print(basis[array_index][basis_index_column])

        bias_column += 1


one_part_array = ['u000', '0u00', '00u0', '000u', 'd000', '0d00', '00d0', '000d']

two_part_array = ['ud00', 'du00', 'uu00', 'dd00', 'u0d0', 'd0u0', 'u0u0', 'd0d0', 'u00d', 'd00u', 'u00u',
                                 'd00d', '0ud0', '0du0', '0uu0', '0dd0', '0u0d', '0d0u', '0u0u', \
                                 '0d0d', '00ud', '00du', '00uu', '00dd', '2000', '0200', '0020', '0002']

three_part_array = ['uuu0', 'uud0', 'udu0', 'udd0', 'duu0', 'dud0', 'ddu0', 'ddd0', 'uu0u', 'uu0d', 'ud0u','ud0d', \
                    'du0u', 'du0d', 'dd0u', 'dd0d', 'u0uu', 'u0ud', 'u0du', 'u0dd', 'd0uu', 'd0ud', 'd0du',
                    'd0dd', '0uuu', '0uud', \
                    '0udu', '0udd', '0duu', '0dud', '0ddu', '0ddd', 'u200', 'd200', '2u00', '2d00', 'u020',
                    'd020', '20u0', '20d0', \
                    'u002', 'd002', '200u', '200d', '0u20', '0d20', '02u0', '02d0', '0u02', '0d02', '020u',
                    '020d', '00u2', '00d2', '002u', '002d']

four_part_array = ['uuuu', 'uuud', 'uudu', 'uudd', 'uduu', 'udud', 'uddu', 'uddd', 'duuu', 'duud', 'dudu',
                                 'dudd', 'dduu', 'ddud', 'dddu', \
                                 'dddd', '2uu0', '2ud0', '2du0', '2dd0', 'u2u0', 'u2d0', 'd2u0', 'd2d0', 'uu20', 'ud20',
                                 'du20', 'dd20', '2u0u', '2u0d', \
                                 '2d0u', '2d0d', 'u20u', 'u20d', 'd20u', 'd20d', 'uu02', 'ud02', 'du02', 'dd02', '20uu',
                                 '20ud', '20du', '20dd', 'u02u', \
                                 'u02d', 'd02u', 'd02d', 'u0u2', 'u0d2', 'd0u2', 'd0d2', '02uu', '02ud', '02du', '02dd',
                                 '0u2u', '0u2d', '0d2u', '0d2d', \
                                 '0uu2', '0ud2', '0du2', '0dd2', '2200', '2020', '2002', '0220', '0202', '0022']

five_part_array = ['2uuu', '2uud', '2udu', '2udd', '2duu', '2dud', '2ddu', '2ddd', 'u2uu', 'u2ud', 'u2du',
                                 'u2dd', 'd2uu', 'd2ud', 'd2du', 'd2dd', 'uu2u', 'uu2d', 'ud2u', 'ud2d', 'du2u', 'du2d',
                                 'dd2u', 'dd2d', \
                                 'uuu2', 'uud2', 'udu2', 'udd2', 'duu2', 'dud2', 'ddu2', 'ddd2', '22u0', '22d0', '2u20',
                                 '2d20', 'u220', 'd220', '220u', '220d', '2u02', '2d02', 'u202', 'd202', '202u', '202d',
                                 '20u2', '20d2', \
                                 'u022', 'd022', '0u22', '0d22', '02u2', '02d2', '022u', '022d']

six_part_array = ['22uu', '22ud', '22du', '22dd', '2u2u', '2u2d', '2d2u', '2d2d', 'u22u', 'u22d', 'd22u',
                                 'd22d', 'u2u2', 'u2d2', \
                                 'd2u2', 'd2d2', 'uu22', 'ud22', 'du22', 'dd22', '2uu2', '2ud2', '2du2', '2dd2', '2220',
                                 '2202', '2022', '0222']

seven_part_array = ['222u', '22u2', '2u22', 'u222', '222d', '22d2', '2d22', 'd222']

full_bas_array = []

full_bas_array.append(one_part_array)#0
full_bas_array.append(two_part_array)#1
full_bas_array.append(three_part_array)#2
full_bas_array.append(four_part_array)#3
full_bas_array.append(five_part_array)#4
full_bas_array.append(six_part_array)#5
full_bas_array.append(seven_part_array)#6

auto_complete_ham(full_bas_array, 3)

#double_array()