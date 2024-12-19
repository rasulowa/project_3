def print_table(rows):
    #  Инициализация переменных
    res_str = ''
    len_set = set()
    #  Сбор длин строк
    for row in rows:
        for el in row:
            len_set.add(len(el))
    #  Выравнивание строк
    try:
        for row in rows:
            for index in range(len(row)):
                while len(row[index]) != max(len_set):
                    row[index] += ' '
    # Обработка пустого ввода
    except ValueError:
        print('Вы подали на вход пустой файл')
        return
    # Формирование конечной строки
    for row in rows:
        for el in row:
            res_str += el + ' '
        res_str += '\n'
    print(res_str)