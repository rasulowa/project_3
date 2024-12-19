import csv
import pickle

def load_table(file_type, file_name):
    # Обработка исключений
    try:
        # Условия для чтения файла
        if file_type == 'csv':
            with open(file_name, newline='') as file:
                file_csv = csv.reader(file, delimiter=';')
                rows = [_ for _ in file_csv]
        elif file_type == 'pickle':
            with open(file_name, 'rb') as file:
                rows = pickle.load(file)
        else:
            # Обработка ошибок
            raise Exception('Неправильно введен тип файла')
    except FileNotFoundError:
        print('Неправильно указан адрес файла или файл не существует')
        return
    except PermissionError:
        print('Необходимо указать путь к файлу')
        return
    else:
        return rows