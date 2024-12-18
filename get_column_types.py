def get_column_types(rows, by_number=True):
    """
    Получение словаря вида столбец:тип_значений. Тип значения: int, float, bool, str (по умолчанию для всех столбцов).

    Args:
        rows(list): внутреннее представление
        by_number(bool): Если True, то ключи в словарях - индекс столбцов, иначе - их строковые представления

    Returns:
        dict: словарь вида столбец: тип_значений.
    Raises:
        None
    """
    dict = {}
    columns = []
    for index in range(len(rows[0])):
        column = []
        for row in rows:
            column.append(row[index])
        columns.append(column)

    for index, column in enumerate(columns):
        if by_number is False:
            index = column[0]
        if column[1] == 'True' or column[1] == 'False':
            dict[index] = bool
            continue
        try:
            crutch = int(column[1])
            dict[index] = int
        except ValueError:
            try:
                crutch = float(column[1])
                dict[index] = float
            except ValueError:
                dict[index] = str
    return dict