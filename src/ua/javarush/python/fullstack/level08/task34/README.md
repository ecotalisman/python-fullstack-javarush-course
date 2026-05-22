<!--
Documenting API Endpoints

Add a section to the README.md file that describes the main API endpoints
of your application.
The endpoints for managing users and tasks must be included,
as well as the methods used to work with them.

Requirements:

1. The README.md section must include a description of the main API endpoints
   related to user management.
   This description must include information about the available HTTP methods,
   endpoint URLs, and the expected request and response data.
2. The README.md section must include a description of the main API endpoints
   related to task management.
   Information about the supported HTTP methods, endpoint URLs,
   and the data structure for requests and responses must be provided.
3. The README.md file must include information about the methods used
   to work with each API endpoint, such as GET, POST, PUT, and DELETE.
   The description must include an example of using each method,
   specifying the required parameters and data format.

🇺🇦 Ukrainian version:

Документування API ендпоінтів

Додайте в файл README.md розділ, що описує основні API ендпоінти
вашого застосунку.
Повинні бути включені ендпоінти для управління користувачами
та завданнями, а також методи для роботи з ними.

Вимоги:

1. У розділі README.md має бути додано опис основних API ендпоінтів,
   пов’язаних з управлінням користувачами.
   Цей опис повинен включати інформацію про доступні методи HTTP,
   URL ендпоінтів та очікувані дані запиту і відповіді.
2. У розділі README.md має бути додано опис основних API ендпоінтів,
   пов’язаних з управлінням завданнями.
   Має бути надана інформація про підтримувані методи HTTP,
   URL ендпоінтів та структуру даних для запитів і відповідей.
3. README.md має включати інформацію про методи роботи
   з кожним API ендпоінтом, такі як GET, POST, PUT, DELETE.
   Опис повинен включати приклад використання кожного методу
   з зазначенням необхідних параметрів та формату даних.
-->

# API Endpoints

The Task Management App exposes a REST API on the backend service
(`http://localhost:5000`). All request and response bodies use **JSON**.
Endpoints marked with 🔒 require an authentication token in the
`Authorization: Bearer <token>` header, obtained after login.

## User Management

### POST /register

Registers a new user.

**Request body:**

```json
{
  "username": "john",
  "password": "secret123"
}
```

**Response (201 Created):**

```json
{
  "message": "User registered successfully",
  "user_id": 1
}
```

**Example:**

```bash
curl -X POST http://localhost:5000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "password": "secret123"}'
```

### POST /login

Authenticates a user and returns an access token.

**Request body:**

```json
{
  "username": "john",
  "password": "secret123"
}
```

**Response (200 OK):**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR..."
}
```

**Example:**

```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "password": "secret123"}'
```

## Task Management

### 🔒 GET /tasks

Returns a list of all tasks belonging to the authenticated user.

**Response (200 OK):**

```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, bread, eggs",
    "status": "pending",
    "owner_id": 1
  }
]
```

**Example:**

```bash
curl -X GET http://localhost:5000/tasks \
  -H "Authorization: Bearer <token>"
```

### 🔒 POST /tasks

Creates a new task for the authenticated user.

**Request body:**

```json
{
  "title": "Buy groceries",
  "description": "Milk, bread, eggs",
  "status": "pending"
}
```

**Response (201 Created):**

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, bread, eggs",
  "status": "pending",
  "owner_id": 1
}
```

**Example:**

```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"title": "Buy groceries", "description": "Milk, bread, eggs", "status": "pending"}'
```

### 🔒 GET /tasks/:id

Returns details of a specific task by its ID.

**Response (200 OK):**

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, bread, eggs",
  "status": "pending",
  "owner_id": 1
}
```

**Example:**

```bash
curl -X GET http://localhost:5000/tasks/1 \
  -H "Authorization: Bearer <token>"
```

### 🔒 PUT /tasks/:id

Updates an existing task. Send only the fields you want to change.

**Request body:**

```json
{
  "title": "Buy groceries and fruits",
  "status": "in_progress"
}
```

**Response (200 OK):**

```json
{
  "id": 1,
  "title": "Buy groceries and fruits",
  "description": "Milk, bread, eggs",
  "status": "in_progress",
  "owner_id": 1
}
```

**Example:**

```bash
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"title": "Buy groceries and fruits", "status": "in_progress"}'
```

### 🔒 DELETE /tasks/:id

Deletes a task by its ID.

**Response (200 OK):**

```json
{
  "message": "Task deleted successfully"
}
```

**Example:**

```bash
curl -X DELETE http://localhost:5000/tasks/1 \
  -H "Authorization: Bearer <token>"
```

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK — request succeeded |
| 201 | Created — new resource created |
| 400 | Bad Request — invalid input data |
| 401 | Unauthorized — token missing or invalid |
| 404 | Not Found — resource does not exist |
| 409 | Conflict — duplicate resource (e.g. username) |

---

# 🇺🇦 Українська версія

# API ендпоінти

Бекенд Task Management App надає REST API на сервісі
`http://localhost:5000`. Усі тіла запитів і відповідей використовують
формат **JSON**. Ендпоінти, позначені 🔒, вимагають токен автентифікації
у заголовку `Authorization: Bearer <token>`, отриманий після логіну.

## Управління користувачами

### POST /register

Реєстрація нового користувача.

**Тіло запиту:**

```json
{
  "username": "john",
  "password": "secret123"
}
```

**Відповідь (201 Created):**

```json
{
  "message": "User registered successfully",
  "user_id": 1
}
```

**Приклад:**

```bash
curl -X POST http://localhost:5000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "password": "secret123"}'
```

### POST /login

Авторизація користувача, повертає токен доступу.

**Тіло запиту:**

```json
{
  "username": "john",
  "password": "secret123"
}
```

**Відповідь (200 OK):**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR..."
}
```

**Приклад:**

```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "password": "secret123"}'
```

## Управління завданнями

### 🔒 GET /tasks

Повертає список усіх завдань авторизованого користувача.

**Відповідь (200 OK):**

```json
[
  {
    "id": 1,
    "title": "Купити продукти",
    "description": "Молоко, хліб, яйця",
    "status": "pending",
    "owner_id": 1
  }
]
```

**Приклад:**

```bash
curl -X GET http://localhost:5000/tasks \
  -H "Authorization: Bearer <token>"
```

### 🔒 POST /tasks

Створює нове завдання для авторизованого користувача.

**Тіло запиту:**

```json
{
  "title": "Купити продукти",
  "description": "Молоко, хліб, яйця",
  "status": "pending"
}
```

**Відповідь (201 Created):**

```json
{
  "id": 1,
  "title": "Купити продукти",
  "description": "Молоко, хліб, яйця",
  "status": "pending",
  "owner_id": 1
}
```

**Приклад:**

```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"title": "Купити продукти", "description": "Молоко, хліб, яйця", "status": "pending"}'
```

### 🔒 GET /tasks/:id

Повертає деталі конкретного завдання за його ID.

**Відповідь (200 OK):**

```json
{
  "id": 1,
  "title": "Купити продукти",
  "description": "Молоко, хліб, яйця",
  "status": "pending",
  "owner_id": 1
}
```

**Приклад:**

```bash
curl -X GET http://localhost:5000/tasks/1 \
  -H "Authorization: Bearer <token>"
```

### 🔒 PUT /tasks/:id

Оновлює існуюче завдання. Надсилайте лише ті поля, які треба змінити.

**Тіло запиту:**

```json
{
  "title": "Купити продукти і фрукти",
  "status": "in_progress"
}
```

**Відповідь (200 OK):**

```json
{
  "id": 1,
  "title": "Купити продукти і фрукти",
  "description": "Молоко, хліб, яйця",
  "status": "in_progress",
  "owner_id": 1
}
```

**Приклад:**

```bash
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"title": "Купити продукти і фрукти", "status": "in_progress"}'
```

### 🔒 DELETE /tasks/:id

Видаляє завдання за його ID.

**Відповідь (200 OK):**

```json
{
  "message": "Task deleted successfully"
}
```

**Приклад:**

```bash
curl -X DELETE http://localhost:5000/tasks/1 \
  -H "Authorization: Bearer <token>"
```

## HTTP коди відповідей

| Код | Значення |
|-----|----------|
| 200 | OK — запит успішний |
| 201 | Created — створено новий ресурс |
| 400 | Bad Request — неправильні вхідні дані |
| 401 | Unauthorized — токен відсутній або недійсний |
| 404 | Not Found — ресурс не знайдено |
| 409 | Conflict — дублюючий ресурс (напр. username) |