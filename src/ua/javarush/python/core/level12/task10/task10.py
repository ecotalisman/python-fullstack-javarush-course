# Writing Binary Data

# Write a program that reads the image input_image.jpg
# and writes it to another file output_image.jpg.

### 🇺🇦 Ukrainian version:

# Запис бінарних даних

# Напишіть програму, яка читає зображення input_image.jpg і записує його в інший файл output_image.jpg.

# Write your code here
with open('input_image.jpg', 'rb') as infile:
    image_data = infile.read()

with open('output_image.jpg', 'wb') as outfile:
    outfile.write(image_data)