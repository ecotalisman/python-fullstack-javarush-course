# Using the Google Cloud Vision API

# Write a program that uses the Google Cloud Vision API
# to analyze an image and recognize objects.

### 🇺🇦 Ukrainian version:

# Google Cloud Vision API

# Напишіть програму, яка використовує Google Cloud Vision API
# для аналізу зображення та розпізнавання об'єктів.

# Write your code here
from google.cloud import vision
import io

client = vision.ImageAnnotatorClient()

file_name = "path/to/your/image.jpg"
with io.open(file_name, "rb") as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response = client.object_localization(image=image)
objects = response.localized_object_annotations

for object_ in objects:
    print(f"Object name: {object_.name}")
    print(f"Confidence: {object_.score}")
