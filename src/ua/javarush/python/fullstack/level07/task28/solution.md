## Tabular Display of Requests

Create a table in Kibana that displays all URLs that were requested and their count. Use the **Data Table** visualization and configure the URL display as columns.

### Steps:

1. Go to **Dashboard** -> **Create new dashboard**.
2. Click **Create new** -> **Data Table**.
3. Select the `logstash-*` index.
4. In the **Buckets** section, add **Split rows** -> **Terms**, and select the `url.keyword` field.
5. Configure the column labels and click **Update**.
6. Save the table and add it to the Dashboard.

### Requirements:

1. The `logstash-*` index must be selected to display the information in the table.
2. **Split rows** must be added using **Terms**, and the `url.keyword` field must be selected to display URLs.
3. The **Data Table** visualization must be used to display requests in tabular form.
4. Column labels must be configured so that URLs are displayed as separate columns.
5. After creating and configuring the table, it must be saved and added to the Dashboard.

## 🇺🇦 Ukrainian version:

## Табличне відображення запитів

Створіть таблицю в Kibana, яка відображає всі URL, до яких були запити, та їх кількість. Використовуйте представлення **Data Table** і налаштуйте відображення URL у вигляді колонок.

### Кроки:

1. Перейдіть у розділ **Dashboard** -> **Create new dashboard**.
2. Натисніть **Create new** -> **Data Table**.
3. Виберіть індекс `logstash-*`.
4. У розділі **Buckets** додайте **Split rows** -> **Terms**, виберіть поле `url.keyword`.
5. Налаштуйте мітки колонок і натисніть **Update**.
6. Збережіть таблицю та додайте її на Dashboard.

### Вимоги:

1. Потрібно вибрати індекс `logstash-*` для відображення інформації в таблиці.
2. Необхідно додати **Split rows** з використанням **Terms** і вибрати поле `url.keyword` для відображення URL.
3. Обов’язково використовувати представлення **Data Table** для відображення запитів у табличній формі.
4. Потрібно налаштувати мітки колонок, щоб URL відображалися у вигляді окремих колонок.
5. Після створення та налаштування таблиці, потрібно зберегти її та додати на Dashboard.