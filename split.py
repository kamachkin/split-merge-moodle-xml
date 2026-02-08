
import xml.etree.ElementTree as ET

input_file = "questions.xml"
num_files = 25
output_files = [f"questions_part{i+1}.xml" for i in range(num_files)]

# Парсим исходный XML
tree = ET.parse(input_file)
root = tree.getroot()

# Находим все вопросы
questions = [q for q in root.findall("question")]

# Считаем, сколько вопросов в каждой части
total = len(questions)
chunk_size = total // num_files
remainder = total % num_files

start = 0
for i in range(num_files):
    end = start + chunk_size + (1 if i < remainder else 0)
    part_questions = questions[start:end]

    quiz = ET.Element("quiz")
    for q in part_questions:
        quiz.append(q)

    tree_part = ET.ElementTree(quiz)
    tree_part.write(output_files[i], encoding="utf-8", xml_declaration=True)
    start = end

print("Файлы успешно созданы:", output_files)