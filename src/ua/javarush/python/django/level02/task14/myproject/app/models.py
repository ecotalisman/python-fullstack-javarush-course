# Working with Media Files
#
# 1. Configure the `MEDIA_URL` and `MEDIA_ROOT` parameters in `settings.py` so that file uploads are saved to the `media` directory in the project root.
#
# 2. Create a `UserDocument` model with a `file` field of type `FileField`, which will store uploaded documents in the `documents` folder.
#
# 3. Create an admin interface for uploading files.
#
# 4. Configure the display of uploaded media files in an HTML template.
#
# Requirements:
#
# 1. In the `settings.py` file, the `MEDIA_URL` parameter must be set to specify the URL prefix for media files, for example `/media/`.
# 2. In the `settings.py` file, the `MEDIA_ROOT` parameter must be defined to specify the path to the `media` directory in the project root for storing media files.
# 3. The `UserDocument` model must contain a `file` field, which is an instance of `FileField`. The `file` field must use the `upload_to='documents'` setting to store uploaded files in the `documents` folder inside the `MEDIA_ROOT` directory.
# 4. The `UserDocument` model must be registered in the `admin.py` file to allow documents to be uploaded through the admin interface.
# 5. The project routing, URLConf, must be configured to provide access to files from the `MEDIA_ROOT` directory through URLs that start with `MEDIA_URL`.
# 6. The HTML template must be configured to display uploaded files using URLs generated through the `file.url` property of the `UserDocument` model object.
#
# 🇺🇦 Ukrainian version:
#
# Робота з медіафайлами
#
# 1. Налаштуйте параметри `MEDIA_URL` та `MEDIA_ROOT` у `settings.py`, щоб завантаження файлів відбувалось у директорію `media` в корені проєкту.
#
# 2. Створіть модель `UserDocument` з полем `file` типу `FileField`, який буде зберігати завантажені документи у папці `documents`.
#
# 3. Створіть в адмінці інтерфейс для завантаження файлів.
#
# 4. Налаштуйте відображення завантажених медіафайлів у HTML-шаблоні.
#
# Вимоги:
#
# 1. У файлі `settings.py` необхідно задати параметр `MEDIA_URL`, що вказує URL-префікс для медіафайлів, наприклад `/media/`.
# 2. У файлі `settings.py` треба визначити параметр `MEDIA_ROOT`, який задає шлях до директорії `media` в корені проєкту для зберігання медіафайлів.
# 3. Модель `UserDocument` повинна містити поле `file`, яке є екземпляром типу `FileField`. Поле `file` повинно використовувати налаштування `upload_to='documents'` для зберігання завантажених файлів у папці `documents` всередині директорії `MEDIA_ROOT`.
# 4. Модель `UserDocument` повинна бути зареєстрована у файлі `admin.py`, щоб забезпечити можливість завантаження документів через інтерфейс адміністратора.
# 5. Повинна бути налаштована маршрутизація проєкту, URLConf, щоб забезпечити доступ до файлів із директорії `MEDIA_ROOT` через адреси, що починаються з `MEDIA_URL`.
# 6. У шаблоні HTML треба налаштувати відображення завантажених файлів, використовуючи URL-адреси, сформовані через властивість `file.url` об'єкта моделі `UserDocument`.

from django.db import models


# Model for storing documents uploaded by users
class UserDocument(models.Model):
    # The file field is for uploading files. Files are stored in the "documents" subfolder inside MEDIA_ROOT
    file = models.FileField(upload_to='documents/')

    # Return the string representation of the document for convenient display in the admin panel
    def __str__(self):
        return self.file.name