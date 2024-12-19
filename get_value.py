def get_value(rows, column=0):
    # Проверка типа и диапазона параметра column:
    if type(column) == int and column < 1:
        raise Exception('Столбца с таким номером не существует')
    # Проверка длины списка rows:
    if len(rows) != 2:
        raise Exception('Ошибка, в таблице не одна строка!')
    # Создание словаря для хранения значений:
    dict = {}
    # Цикл для обработки данных:
    for index, el in enumerate(rows[1]):
        if type(column) != int:
            index = rows[0][index]
        else:
            index += 1
        # Преобразование значений в соответствующие типы:
        if el == 'True':
            dict[index] = True
        elif el == 'False':
            dict[index] = False
        else:
            try:
                dict[index] = int(el)
            except ValueError:
                try:
                    dict[index] = float(el)
                except ValueError:
                    dict[index] = el
    try:
        return dict[column]
    except KeyError:
        print('Столбца с таким названием не существует')
        return