# My Notes on Running This Demo

This repository was cloned from https://github.com/et-soft/habr-elk
for the JavaRush lecture "Visualizing logs in Kibana" (Level 17, Lecture 7).

## Changes Compared to the Original

### Windows Fix: Filebeat Permissions

A line was added to the `filebeat` section of `docker-compose.yml`:

    command: filebeat -e -strict.perms=false

**Reason:** On Windows, Filebeat refuses to start with the error:

    Exiting: error loading config file: config file ("filebeat.yml")
    can only be writable by the owner but the permissions are "-rwxrwxrwx"

When a file is mounted from a Windows host into a Linux container, the
permissions become `rwxrwxrwx`, which Filebeat considers insecure. The
`-strict.perms=false` parameter disables this safety check. This fix is
**not needed** on Linux/Mac.

## How to Start

    cd habr-elk
    docker compose up -d

Wait ~30 seconds. Verify all containers are in `Up` status:

    docker compose ps

There should be 5 containers: elasticsearch, logstash, kibana, filebeat, golang.

## How to Access Kibana

Open in browser: http://localhost:5601

First time:
1. Click "Explore on my own"
2. Menu (☰) → Discover → Create index pattern
3. Index pattern: `logstash-*`
4. Time field: `@timestamp`
5. Done — you can view logs

## How to Stop

    docker compose down

Containers are removed, images (~3 GB) remain for quick next startup.

## How to Remove Everything, Including Images

    docker compose down --rmi all -v

`--rmi all` removes images (~3 GB of disk), `-v` removes volumes with data.

---

# 🇺🇦 Ukrainian version:

# Мої замітки по запуску цього демо

Цей репозиторій склонований з https://github.com/et-soft/habr-elk
для лекції JavaRush "Візуалізація логів у Kibana" (рівень 17, лекція 7).

## Зміни порівняно з оригіналом

### Виправлення для Windows: Filebeat permissions

У `docker-compose.yml` у секцію `filebeat` додано рядок:

    command: filebeat -e -strict.perms=false

**Причина:** Filebeat на Windows відмовляється стартувати з помилкою:

    Exiting: error loading config file: config file ("filebeat.yml")
    can only be writable by the owner but the permissions are "-rwxrwxrwx"

Коли файл монтується з Windows-хосту в Linux-контейнер, права стають
`rwxrwxrwx`, що Filebeat вважає небезпечним. Параметр `-strict.perms=false`
вимикає цю перевірку. На Linux/Mac цієї правки **не потрібно**.

## Як запустити

    cd habr-elk
    docker compose up -d

Зачекати ~30 секунд. Перевірити, що всі контейнери у статусі `Up`:

    docker compose ps

Має бути 5 контейнерів: elasticsearch, logstash, kibana, filebeat, golang.

## Як зайти в Kibana

Відкрити браузер: http://localhost:5601

Перший раз:
1. "Explore on my own"
2. Меню (☰) → Discover → Create index pattern
3. Index pattern: `logstash-*`
4. Time field: `@timestamp`
5. Готово, можна дивитись логи

## Як зупинити

    docker compose down

Контейнери видаляються, образи (~3 ГБ) залишаються для швидкого
наступного запуску.

## Як прибрати все, включно з образами

    docker compose down --rmi all -v