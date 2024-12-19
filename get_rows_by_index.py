import copy

def get_rows_by_index(rows, values, copy_table=False):
   
    if copy_table is False:
        table = copy.deepcopy(rows)
        rows.clear()
    else:
        table = rows
    # Инициализация списка результатов:
    result = [table[0]]
    table = table[1:]
    values = [val for val in values]
    # Преобразование элементов в числовые типы:
    for index1, row in enumerate(table):
        for index2, el in enumerate(table):
            try:
                table[indx1][index2] = int(table[index1][index2])
            except ValueError:
                try:
                    table[index1][index2] = float(table[index1][index2])
                except ValueError:
                    pass
    for row in table:
        if row[0] in values:
            result.append([str(el) for el in row])
    if copy_table:
        return result
    else:
        for row in result:
            rows.append(row)
        return rows