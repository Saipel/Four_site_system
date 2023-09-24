def auto_complete_ham(basis):
    """
    # %======================================================================================================
    # функция должна автоматически заполнять матрицы гамильтонианов
    # Возможные связи узлов {
    # 1 и 2 (1d\sigma 2c\sigma); 1 и 4
    # 2 и 1; 2 и 3
    # 3 и 2; 3 и 4
    # 4 и 3; 4 и 1
    # } \sigma = u,d.
    # Возможная запись 1dd и 2cd.
    # После эта схема разбивается командой list на массив элементов.
    # Первый элемент массива указывает узел, второй - действие с электроном, третий - спин электрона
    # %======================================================================================================
    # Заполнение матриц гамильтониана происходит в двух циклах. Заполняться будет только верхняя половина матрицы.
    # работа с базисом. Разбиваем в массив list (функция cep_bas_array).
    # После применения функции в каждый элемент массива разбивается на подмассив из четырех элементов.
    # %======================================================================================================
    # Постановка условия для определения состояний между которыми есть перескок:
        если первый элемент массива равен второму или четвертому; второй равен первому или третьему;
        третий равен второму или четвертому; четвертый равен третьему или первому. (необходимо сравнивать связку элементов...)
        Если перескок произошел с первого узла на второй (при одном электроне), то сранивается первый узел со вторым и наоборот в одной итерации\
        basis_index_line = 0 #переменная отвечает за перемещение по горизонтальным эдементам
        basis_index_column = 0 #переменная отвечает за перемещение по вертикальным элементам
    """

    """
        # Неприятная конструкция. basis[номер рассматриваемого случая - количество частиц в системе минус - 1]
        #                               [номер состояния базиса, для каждого массива уникален, отсчет начинается с 1го элемента]
        #                               [номер узла, задаетсяв диапазоне от 0 до 3х. В цикле range(0,4), чтобы затрагивался последний элемент] 
    """

    bias_column = 0
    for basis_index_line in range(len(basis[0])):
        for basis_index_column in range(bias_column + 1, int(len(basis[0]))):
            print("basis_index_line=", basis_index_line)
            print("basis_index_column=", basis_index_column)
            # Сравниваем первый и второй узел
            if (basis[0][basis_index_line][0] == basis[0][basis_index_column][1] and basis[0][basis_index_line][1] == basis[0][basis_index_column][0]
            and basis[0][basis_index_line][2] == basis[0][basis_index_column][2] and basis[0][basis_index_line][3] == basis[0][basis_index_column][3]
                    and ((basis[0][basis_index_line][0] != 0 and basis[0][basis_index_line][1] != 0)
                    or (basis[0][basis_index_line][0] != 2 and basis[0][basis_index_line][1] != 2))):
                print("1 and 2")
                print("line", basis[0][basis_index_line])
                print("column", basis[0][basis_index_column], "\n")


            # Сравниваем первый и четвертый узел
            if ((basis[0][basis_index_line][0] == basis[0][basis_index_column][3] and basis[0][basis_index_line][3] == basis[0][basis_index_column][0]
                    and basis[0][basis_index_line][2] == basis[0][basis_index_column][2] and basis[0][basis_index_line][1] == basis[0][basis_index_column][1])\
                    and ((basis[0][basis_index_line][0] != 0 and basis[0][basis_index_line][3] != 0)
                    or (basis[0][basis_index_line][0] != 2 and basis[0][basis_index_line][3] != 2))):
                print("1 and 4")
                print("line", basis[0][basis_index_line])
                print("column", basis[0][basis_index_column], "\n")


            # Сравниваем второй и третий узел
            if (basis[0][basis_index_line][1] == basis[0][basis_index_column][2] and basis[0][basis_index_line][2] == basis[0][basis_index_column][1]
                    and basis[0][basis_index_line][0] == basis[0][basis_index_column][0] and basis[0][basis_index_line][3] == basis[0][basis_index_column][3]
                    and ((basis[0][basis_index_line][1] != 0 and basis[0][basis_index_line][2] != 0)
                    or (basis[0][basis_index_line][1] != 2 and basis[0][basis_index_line][2] != 2))):
                print("2 and 3")
                print("line", basis[0][basis_index_line])
                print("column", basis[0][basis_index_column], "\n")

            # Сравниваем третий и четвертый узел
            if (basis[0][basis_index_line][2] == basis[0][basis_index_column][3] and basis[0][basis_index_line][3] == basis[0][basis_index_column][2]
                    and basis[0][basis_index_line][0] == basis[0][basis_index_column][0] and basis[0][basis_index_line][1] == basis[0][basis_index_column][1]
                    and ((basis[0][basis_index_line][2] != 0 and basis[0][basis_index_line][2] != 0)
                    or (basis[0][basis_index_line][3] != 2 and basis[0][basis_index_line][3] != 2))):
                print("3 and 4")
                print("line", basis[0][basis_index_line])
                print("column", basis[0][basis_index_column], "\n")

        bias_column += 1


    pass