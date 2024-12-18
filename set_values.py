def set_values(rows, values, column=0):
    """
    Задание списка значений values для столбца таблицы.

    Args:
        rows: внутреннее представление
        values: список значений для столбца таблицы
        column(int, str): либо номер столбца, либо его строковое представление

    Returns:
       list: внутреннее представление
    Raises:
        Exception('Cтолбца с таким номером не существует')
    """
    header = rows[0]
    dict = {}
    types_dict = {}
    if type(column) == int:
        if column < 1:
            raise Exception('Cтолбца с таким номером не существует')
    columns = []
    res_rows = []
    for index in range(len(rows[0])):
        col = []
        for row in rows:
            col.append(row[index])
        columns.append(col)
    for index, col in enumerate(columns):
        if type(column) != int:
            index = col[0]
        else:
            index += 1
        dict[index] = col[1:]

    for key, value in dict.items():
        el = value[0]
        if el == 'True' or el == 'False':
            types_dict[key] = bool
        else:
            try:
                crutch = int(el)
                types_dict[key] = int
            except ValueError:
                try:
                    crutch = float(el)
                    types_dict[key] = float
                except ValueError:
                    types_dict[key] = str
    try:
        if len(dict[column]) != len(values):
            print('Кол-во значений в задаваемом столбце не соответcтвует размеру таблицы')
            return
    except KeyError:
        print('Столбца с таким индексом/названием не существует')
        return
    else:
        typ = types_dict[column]
        try:
            values = [str(typ(el)) for el in values]
        except ValueError:
            print('Вы ввели данные, которые нельзя типизировать')
            return
        for index in range(len(values)):
            if values[index] is True:
                values[index] = 'True'
            elif values[index] is False:
                values[index] = 'False'
        dict[column] = values
    res_columns = [value for value in dict.values()]
    for index in range(len(res_columns[0])):
        row = []
        for col in res_columns:
            row.append(col[index])
        res_rows.append(row)
    return [header] + res_rows