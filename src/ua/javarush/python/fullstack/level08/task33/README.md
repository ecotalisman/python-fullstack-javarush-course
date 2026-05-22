<!--
Creating a Basic README

Write a README.md file for a multi-container task management application.
Include a project description, its components such as frontend, backend,
and database, and instructions for installing and running the application
using Docker Compose.

Requirements:

1. The README.md file must contain a clear and concise project description
   that explains its main features and purpose.
2. The README.md file must include a section describing the key components
   of the multi-container application, such as the frontend, backend,
   and database, with a brief explanation of their role in the application.
3. The README.md file must contain step-by-step installation instructions,
   including all required prerequisites and commands.
4. The README.md file must contain clear steps for running the application
   using Docker Compose, including commands and any necessary explanation
   of the Docker Compose configuration file.

🇺🇦 Ukrainian version:

Створення базового README

Напишіть файл README.md для багатоконтейнерного застосунку
з управління завданнями.
Включіть опис проєкту, його компоненти, такі як фронтенд,
бекенд і база даних, а також інструкцію з установки та запуску
застосунку з використанням Docker Compose.

Вимоги:

1. Файл README.md повинен містити чіткий і стислий опис проєкту,
   що пояснює його основні функції й призначення.
2. Файл README.md має включати розділ із описом ключових компонентів
   багатоконтейнерного застосунку, таких як фронтенд, бекенд і база даних,
   з коротким поясненням їхньої ролі в застосунку.
3. Файл README.md повинен містити покрокову інструкцію з установки
   застосунку, включаючи всі необхідні попередні умови та команди.
4. Файл README.md повинен містити чіткі кроки для запуску застосунку
   за допомогою Docker Compose, включаючи команди та будь-яке необхідне
   пояснення конфігурації файлу Docker Compose.
-->

# Task Management App

A multi-container task management application that lets users create, edit,
delete, and assign tasks. The system is built as a classic three-tier web
application and runs entirely in Docker containers, making it easy to launch
on any machine with a single command.

## Main Components

- **Frontend** — a ReactJS application that provides the user interface
  for working with tasks. Runs on port `3000`.
- **Backend** — a Python (Flask) application that exposes a REST API,
  handles business logic, and communicates with the database. Runs on
  port `5000`.
- **Database** — a PostgreSQL database that stores users and tasks.
  Runs on port `5432`.

The services communicate over an internal Docker network: the frontend
sends HTTP requests to the backend, and the backend talks to the database
using SQLAlchemy.

## Requirements

Before installing the project, make sure the following tools are
installed on your machine:

- **Docker** — [installation guide](https://docs.docker.com/get-docker/)
- **Docker Compose** — [installation guide](https://docs.docker.com/compose/install/)
- **Git** — to clone the repository

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/ecotalisman/task_management_app.git
   ```

2. Move into the project folder:

   ```bash
   cd task_management_app
   ```

The folder contains a `docker-compose.yml` file that describes all three
services (frontend, backend, database), their network, and persistent
storage for the database.

## Running the Application with Docker Compose

1. Build the images and start all containers in one command:

   ```bash
   docker compose up --build
   ```

   The `--build` flag tells Docker Compose to rebuild the images from
   the `Dockerfile` of each service before starting. On subsequent
   launches you can simply run `docker compose up`.

2. Once all services have started, open the application in your browser:

   - **Frontend (UI):** `http://localhost:3000`
   - **Backend (API):** `http://localhost:5000`

3. To stop the application:

   ```bash
   docker compose down
   ```

   This stops and removes the containers but keeps the database volume,
   so your data is preserved for the next launch.

---

# 🇺🇦 Українська версія

# Task Management App

Багатоконтейнерний застосунок для управління завданнями, який дозволяє
користувачам створювати, редагувати, видаляти завдання та призначати
їх іншим користувачам. Систему побудовано як класичний триярусний
веб-застосунок, що повністю працює у Docker-контейнерах і запускається
однією командою.

## Основні компоненти

- **Frontend** — ReactJS-застосунок, що забезпечує інтерфейс
  користувача для роботи з завданнями. Працює на порту `3000`.
- **Backend** — застосунок на Python (Flask), який надає REST API,
  обробляє бізнес-логіку та взаємодіє з базою даних. Працює на
  порту `5000`.
- **Database** — база даних PostgreSQL для зберігання користувачів
  і завдань. Працює на порту `5432`.

Сервіси спілкуються через внутрішню Docker-мережу: фронтенд надсилає
HTTP-запити до бекенду, а бекенд звертається до бази даних через
SQLAlchemy.

## Вимоги

Перед встановленням проєкту переконайтеся, що на вашій машині
встановлено:

- **Docker** — [інструкція зі встановлення](https://docs.docker.com/get-docker/)
- **Docker Compose** — [інструкція зі встановлення](https://docs.docker.com/compose/install/)
- **Git** — для клонування репозиторію

## Встановлення

1. Клонуйте репозиторій на свій комп'ютер:

   ```bash
   git clone https://github.com/ecotalisman/task_management_app.git
   ```

2. Перейдіть у папку проєкту:

   ```bash
   cd task_management_app
   ```

У папці лежить файл `docker-compose.yml`, який описує всі три сервіси
(frontend, backend, database), їхню мережу та постійне сховище для
бази даних.

## Запуск застосунку через Docker Compose

1. Зберіть образи та запустіть усі контейнери однією командою:

   ```bash
   docker compose up --build
   ```

   Прапор `--build` каже Docker Compose перебудувати образи з
   `Dockerfile` кожного сервісу перед запуском. При наступних
   запусках достатньо `docker compose up`.

2. Після запуску відкрийте застосунок у браузері:

   - **Frontend (інтерфейс):** `http://localhost:3000`
   - **Backend (API):** `http://localhost:5000`

3. Щоб зупинити застосунок:

   ```bash
   docker compose down
   ```

   Ця команда зупиняє та видаляє контейнери, але зберігає том з даними
   бази, тому ваша інформація залишиться для наступного запуску.