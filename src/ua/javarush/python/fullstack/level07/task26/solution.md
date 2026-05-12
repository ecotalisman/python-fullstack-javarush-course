# Creating an Index for Docker Logs
# Configure an index in Kibana to display logs received from Docker containers.
# Use the Logstash pattern "logstash-*".
# Make sure that the logs are displayed in the "Discover" section.
#
# Steps:
#
# 1. Go to Kibana at http://localhost:5601.
#
# 2. Open the "Discover" section in the left menu.
#
# 3. Click "Create index pattern".
#
# 4. Enter "logstash-*" in the "Index pattern name" field.
#
# 5. On the next page, select the "@timestamp" field as the time field.
#
# 6. Go to the "Discover" section and make sure that the logs are displayed.
#
# Requirements:
# • The task must use Kibana to configure an index that will display logs received from Docker containers.
# • To create the index in Kibana, the Logstash pattern "logstash-*" must be used.
# • After configuring the index, the logs must be displayed in the "Discover" section of the Kibana interface.
# • When creating the index, the "@timestamp" field must be selected as the time field.
# • To complete the task, you must go to the Kibana page at http://localhost:5601.
#
# 🇺🇦 Ukrainian version:
#
# Створення індексу для логів Docker
# Налаштуйте індекс у Kibana для відображення логів, отриманих із Docker-контейнерів. Використовуйте логстеш-шаблон "logstash-*". Переконайтеся, що логи відображаються в розділі "Discover".
#
# Кроки:
#
# 1. Перейдіть у Kibana за адресою http://localhost:5601.
#
# 2. Відкрийте розділ "Discover" у лівому меню.
#
# 3. Натисніть "Create index pattern".
#
# 4. Введіть "logstash-*" у поле "Index pattern name".
#
# 5. На наступній сторінці виберіть поле "@timestamp" як часову мітку.
#
# 6. Перейдіть у розділ "Discover" і переконайтеся, що логи відображаються.
#
# Вимоги:
# • Скрипт має використовувати Kibana для налаштування індексу, який буде відображати логи, отримані із Docker-контейнерів.
# • Для створення індексу у Kibana необхідно використовувати логстеш-шаблон "logstash-*".
# • Після налаштування індексу логи повинні відображатися у розділі "Discover" на інтерфейсі Kibana.
# • Під час створення індексу необхідно вибрати поле "@timestamp" як часову мітку.
# • Для виконання завдання необхідно перейти на сторінку Kibana за адресою http://localhost:5601.