# Creating Data Models
# Create data models for users and tasks in your application.
# Users must have unique usernames and store password hashes,
# and tasks must be linked to a specific user through a foreign key.
#
# Requirements:
# • The data model for users must ensure username uniqueness so that each user has a unique name in the system.
# • The data model must include a field for storing the password hash, not the password itself, to ensure user data security.
# • The data model for tasks must contain a foreign key that links each task to the specific user who owns that task.
#
# 🇺🇦 Ukrainian version:
#
# Створення моделей даних
# Створіть моделі даних для користувачів і завдань у вашому застосунку. Користувачі повинні мати унікальні імена та зберігати хеші паролів, а завдання повинні бути пов’язані з конкретним користувачем через зовнішній ключ.
#
# Вимоги:
# • Модель даних для користувачів повинна забезпечувати унікальність імен, щоб кожний користувач мав унікальне ім'я в системі.
# • Модель даних повинна включати поле для зберігання хеша пароля, а не самого пароля, для забезпечення безпеки даних користувачів.
# • Модель даних для завдань повинна містити зовнішній ключ, який зв'язує кожне завдання з конкретним користувачем, що володіє цим завданням.

from sqlalchemy.orm import relationship

from .user import User
from .task import Task

User.tasks = relationship("Task", order_by=Task.id, back_populates="user")