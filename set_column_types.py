def set_column_types(rows, types_dict, by_number=True):
    
    header = rows[0]
    res_rows = [header]
    columns = []
    for index in range(len(rows[0])):
        column = []
        for row in rows:
            column.append(row[index])
        columns.append(column)
    if by_number is True:
        dict = {index: el[1:] for index, el in enumerate(columns)}
    else:
        dict = {el[0]: el[1:] for el in columns}
    try:
        for key, value in types_dict.items():
            for index, el in enumerate(dct[key]):
                if el == 'True':
                    dict[key][index] = True
                elif el == 'False':
                    dict[key][index] = False
                else:
                    try:
                        dict[key][index] = int(dict[key][index])
                    except ValueError:
                        try:
                            dict[key][index] = float(dict[key][index])
                        except ValueError:
                            pass
                dict[key][index] = str(value(dict[key][index]))
    except KeyError:
        print('В таблице нет столбца с таким названием/индексом')
        return
    except ValueError:
        print('Ошибка! Нельзя конвертировать значение в указанный тип данных')
        return
    for index in range(len(columns[0]) - 1):
        row = []
        for value in dict.values():
            row.append(value[index])
        res_rows.append(row)
    return res_rows