import glob
import xml.etree.ElementTree as ET

# Получаем список всех файлов вида questions_part*.xml
files = sorted(glob.glob("questions_part*.xml"))

# Создаём корневой элемент для итогового файла
quiz = ET.Element("quiz")

for fname in files:
    tree = ET.parse(fname)
    root = tree.getroot()
    for q in root.findall("question"):
        quiz.append(q)

# Сохраняем объединённый файл
ET.ElementTree(quiz).write("questions_merged.xml", encoding="utf-8", xml_declaration=True)

print(f"Объединено файлов: {len(files)}. Итоговый файл: questions_merged.xml")