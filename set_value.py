def set_value(self, value, column=0):
    # Проверка на количество строк
    try:
        if len(self.data) != 1:
            raise ValueError("Таблица содержит более одной строки.")
        # Определение индекса колонки
        col_index = column if isinstance(column, int) else self.header.index(column)
        # Установка значения
        self.data[0][col_index] = value
    # Обработка ошибок
    except Exception as e:
        raise Exception(f"Ошибка в set_value: {e}")