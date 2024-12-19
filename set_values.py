def set_values(self, values, column=0):
    try:
        # Определение индекса столбца:
        col_index = column if isinstance(column, int) else self.header.index(column)
        # Проверка длины значений:
        if len(values) != len(self.data):
            raise ValueError("Длина значений не соответствует количеству строк.")
        # Цикл по значениям:
        for i, value in enumerate(values):
            # Установка значения:
            self.data[i][col_index] = value
    except Exception as e:
        # Возбуждение исключения:
        raise Exception(f"Ошибка в set_values: {e}")