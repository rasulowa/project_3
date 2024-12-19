def get_column_types(rows, by_number=True):
    # Инициализация переменных:
    dict = {}
    columns = []
    # Сбор данных столбцов:
    for index in range(len(rows[0])):
        column = []
        for row in rows:
            column.append(row[index])
        columns.append(column)
    # Определение типов данных для столбцов:
    for index, column in enumerate(columns):
        if by_number is False:
            index = column[0]
        if column[1] == 'True' or column[1] == 'False':
            dict[index] = bool
            continue
        try:
            res = int(column[1])
            dict[index] = int
        except ValueError:
            try:
                res = float(column[1])
                dict[index] = float
            except ValueError:
                dict[index] = str
    return dict