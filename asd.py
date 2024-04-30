import csv
import requests

# Отправляем GET запрос на сервер
response = requests.get('https://bilimge.kz/admins/api/teacher/?school=aa27')

# Проверяем успешность запроса
if response.status_code == 200:
    teachers_data = response.json()  # Получаем данные в формате JSON

    # Читаем CSV файл
    with open('school_teachers_support.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)  # Преобразуем в список

    # Проходим по каждой строке CSV файла и обновляем первое поле
    for row in rows:
        first_field_csv = row[0]  # Получаем первое поле CSV строки
        for teacher in teachers_data:
            if first_field_csv == str(teacher['id']):  # Сравниваем с id из JSON
                row[0] = str(teacher['id'])  # Изменяем первое поле на id из JSON
                break

    # Перезаписываем обновленные данные в CSV файл
    with open('school_teachers_support.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

else:
    print("Ошибка при получении данных:", response.status_code)
