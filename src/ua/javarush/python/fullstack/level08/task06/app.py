# Implementing a CRUD API for Tasks
#
# Create an API for managing tasks using CRUD operations with Flask.
# Implement functions for creating, retrieving, updating, and deleting tasks.
#
# Requirements:
#
# 1. The API must include a function for adding a new task,
#    which accepts task data and stores it in the storage.
# 2. The API must include functionality for retrieving a list of all tasks
#    or a single task by its identifier.
# 3. The API must provide the ability to update information about an existing task
#    by passing modified data.
# 4. The API must include a function for deleting a task by its identifier
#    from the storage.
# 5. The application must be developed using the Flask web framework
#    to handle HTTP requests.
#
# 🇺🇦 Ukrainian version:
#
# Реалізація CRUD API для задач
#
# Створіть API для управління задачами (CRUD-операції) за допомогою Flask.
# Реалізуйте функції створення, отримання, оновлення та видалення задач.
#
# Вимоги:
#
# 1. API повинно включати функцію для додавання нової задачі,
#    яка приймає дані про задачу і зберігає їх у сховищі.
# 2. API повинно містити функціональність для отримання списку всіх задач
#    або окремої задачі за ідентифікатором.
# 3. API повинно передбачати можливість оновлення інформації про існуючу задачу
#    шляхом передання змінених даних.
# 4. API повинно включати функцію для видалення задачі за її ідентифікатором
#    із сховища.
# 5. Додаток повинен бути розроблений із використанням веб-фреймворку Flask
#    для обробки HTTP-запитів.

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Storing tasks in memory
tasks = {}
current_id = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global current_id
    if not request.json or 'title' not in request.json:
        abort(400)
    task = {
        'id': current_id,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks[current_id] = task
    current_id += 1
    return jsonify({'task': task}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': list(tasks.values())})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = tasks.get(task_id)
    if task is None:
        abort(404)
    return jsonify({'task': task})

@app.route('/tasks/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = tasks.get(task_id)
    if task is None:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) is not str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    
    return jsonify({'task': task})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = tasks.pop(task_id, None)
    if task is None:
        abort(404)
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)