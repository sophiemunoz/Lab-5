import os
import re


# TAREA 1

print("=== TAREA 1 ===")

with open(r"C:\Users\chavi\OneDrive\Escritorio\Visual Studio\Lab_5\task1-en.txt", encoding="utf-8") as f:
    text1 = f.read()

# 1. Palabras que terminan en "e"
words_ending_e = re.findall(r"\b\w*e\b", text1)
print("Palabras que terminan en 'e':")
print(words_ending_e)

# 2. Números entre paréntesis
numbers_in_parentheses = re.findall(r"\(\d+\)", text1)
print("\nNúmeros entre paréntesis:")
print(numbers_in_parentheses)


# TAREA 2

print("\n=== TAREA 2 ===")

with open(r"C:\Users\chavi\OneDrive\Escritorio\Visual Studio\Lab_5\task2.html", encoding="utf-8") as f:
    html = f.read()

# regex para capturar width y height por imagen
image_pattern = r'<img[^>]*>'
images = re.findall(image_pattern, html)

image_sizes = []

for img_tag in images:
    width_match = re.search(r'width\s*=\s*"(\d+)"', img_tag)
    height_match = re.search(r'height\s*=\s*"(\d+)"', img_tag)
    width = width_match.group(1) if width_match else "N/A"
    height = height_match.group(1) if height_match else "N/A"
    image_sizes.append((width, height))

print("Dimensiones de imágenes (width, height):")
for w, h in image_sizes:
    print(w, h)


# TAREA 3

print("\n=== TAREA 3 ===")

BASE_PATH = r"C:\Users\chavi\OneDrive\Escritorio\Visual Studio\Lab_5"

with open(f"{BASE_PATH}/task3.txt", encoding="utf-8") as f:
    text3 = f.read()

# Expresiones regulares
id_re = r"\b\d+\b"
surname_re = r"\b[А-ЯЁA-Z][а-яёa-zA-ZáéíóúÁÉÍÓÚ]+\b"
email_re = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
date_re = r"\b\d{4}-\d{2}-\d{2}\b|\b\d{2}[./-]\d{2}[./-]\d{2,4}\b"


web_re = r"\b(?:https?://|www\.)[a-zA-Z0-9-]+\.(?:com|ru|org|net|info|edu)\b"

ids = re.findall(id_re, text3)
surnames = re.findall(surname_re, text3)
emails = re.findall(email_re, text3)
dates = re.findall(date_re, text3)
websites = re.findall(web_re, text3)

print("Cantidad de elementos encontrados:")
print("IDs:", len(ids))
print("Apellidos:", len(surnames))
print("Emails:", len(emails))
print("Fechas:", len(dates))
print("Webs:", len(websites))

# Crear lista de registros y ordenar por ID numérico
records = []
min_len = min(len(ids), len(surnames), len(emails), len(dates), len(websites))
for i in range(min_len):
    records.append((int(ids[i]), surnames[i],
                   emails[i], dates[i], websites[i]))

records_sorted = sorted(records, key=lambda x: x[0])

# Guardar CSV
csv_path = f"{BASE_PATH}/result.csv"
with open(csv_path, "w", encoding="utf-8") as f:
    f.write("ID,Apellido,Email,Fecha,Web\n")
    for rec in records_sorted:
        f.write(f"{rec[0]},{rec[1]},{rec[2]},{rec[3]},{rec[4]}\n")

print("CSV guardado correctamente en:", csv_path)


# TAREA ADICIONAL

print("\n=== TAREA ADICIONAL ===")

with open(r"C:\Users\chavi\OneDrive\Escritorio\Visual Studio\Lab_5\task_add.txt", encoding="utf-8") as f:
    text_add = f.read()

extra_dates = re.findall(r"\s\d{2}[./-]\d{2}[./-]\d{2,4}", text_add)
extra_emails = re.findall(
    r"\s[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text_add)


extra_webs = re.findall(
    r"\b(?:https?://|www\.)[a-zA-Z0-9-]+\.(?:com|ru|org|net|info|edu)\b",
    text_add
)

print("Fechas encontradas:", extra_dates)
print("Emails encontrados:", extra_emails)
print("Webs encontradas:", extra_webs)
print("\nTOTAL encontrados:", len(extra_dates) +
      len(extra_emails) + len(extra_webs))
