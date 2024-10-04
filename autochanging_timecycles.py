import xml.etree.ElementTree as ET

def modify_values(element):
    # Преобразование текста элемента в список значений
    values = element.text.strip().split()
    if values:
        # Замена всех значений на первое значение
        first_value = values[6]
        element.text = ' '.join([first_value] * len(values))

def process_xml(file_path):
    # Парсинг XML-файла
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Проход по всем элементам в файле
    for elem in root.iter():
        if elem.text and elem.text.strip():
            modify_values(elem)

    # Сохранение изменений в файл
    tree.write('modified_' + file_path, encoding='UTF-8', xml_declaration=True)
    print(f"Изменения сохранены в 'modified_{file_path}'")

# Укажите путь к вашему XML-файлу
process_xml('w_extrasunny.xml')
