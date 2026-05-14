## Optimizing Prometheus Performance

Your Prometheus server is experiencing high load, which causes the system to slow down. Optimize metric collection and improve Prometheus performance.

### Steps:

1. Check the `scrape_interval` parameter in the Prometheus configuration and increase the metric collection interval to reduce the load.
2. Split metric sources across several Prometheus instances to distribute the load.
3. Make sure that the Prometheus server has enough resources, such as CPU and memory, or add them if necessary.

### Requirements:

1. The script must include checking the `scrape_interval` parameter in the Prometheus configuration file and provide the ability to increase the metric collection interval to reduce system load.
2. Metric sources must be distributed across multiple Prometheus instances to ensure balanced load distribution.
3. It must be possible to check the current resources of the Prometheus server, such as CPU and memory, and add additional resources if necessary to maintain stable system operation.

## 🇺🇦 Ukrainian version:

## Оптимізація продуктивності Prometheus

Ваш сервер Prometheus стикається з високим навантаженням, що спричиняє уповільнення роботи системи. Оптимізуйте збір метрик і покращіть продуктивність Prometheus.

### Кроки:

1. Перевірте параметр `scrape_interval` у конфігурації Prometheus і збільшіть інтервал збору метрик для зменшення навантаження.
2. Розділіть джерела метрик на декілька інстансів Prometheus для розподілу навантаження.
3. Переконайтеся, що сервер Prometheus має достатньо ресурсів, таких як CPU і пам'ять, або додайте їх за потреби.

### Вимоги:

1. Скрипт має передбачати перевірку параметра `scrape_interval` у конфігураційному файлі Prometheus і можливість збільшення інтервалу збору метрик для зниження системного навантаження.
2. Необхідно забезпечити розподіл джерел метрик між кількома інстансами Prometheus для рівномірного розподілу навантаження.
3. Має бути можливість перевірки поточних ресурсів сервера Prometheus, таких як CPU і пам'ять, і додавання додаткових ресурсів у разі потреби для підтримання стабільної роботи системи.
