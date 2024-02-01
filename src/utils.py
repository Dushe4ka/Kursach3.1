import json
import re
from datetime import datetime

def load_json():
    """
    Открытие файла operations.json
    """
    with open('operations.json', 'r', encoding="UTF-8") as f:
        json_operations = json.load(f)
    return json_operations.load(f)

def json_EXECUTED_operations(values):
    """
    Функция возвращает список выполненных операций
    """
    return [operation for operation in values if operation['status'] == 'EXECUTED']

def sort_date_operations(operations):
    """
    Функция сортирует список 5 последних операций по дате
    """
    sort_list = sorted(operations, key=lambda operation: operation['date'], reverse=True)
    sort_last_list = sort_list[0:5]
    return sort_last_list

