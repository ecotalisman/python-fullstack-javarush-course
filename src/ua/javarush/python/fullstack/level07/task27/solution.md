## Visualizing Logs Using a Histogram

Create a histogram in Kibana that will display the ratio of successful (`statusCode < 400`) and unsuccessful (`statusCode >= 400`) requests. Use the **Vertical Bar** visualization and display the data on a time axis.

### Steps:

1. Go to **Dashboard** -> **Create new dashboard**.
2. Click **Create new** -> **Vertical Bar**.
3. Select the created index `logstash-*`.
4. In the **Buckets** section, click **Add** -> **X-axis**, select **Date Histogram**, and set the `@timestamp` field.
5. Add filters for `statusCode >= 400` for unsuccessful requests and `statusCode < 400` for successful requests.
6. Click **Update** to display the chart and save it to the Dashboard.

### Requirements:

1. The **Vertical Bar** visualization must be selected to visualize the data in Kibana.
2. Display the data on a time axis using **Date Histogram** on the X-axis and the `@timestamp` field.
3. Add filters to display successful requests (`statusCode < 400`) and unsuccessful requests (`statusCode >= 400`).
4. Use the `logstash-*` index to select the data for visualization.
5. After displaying the chart, save it to the Dashboard for further use.

## 🇺🇦 Ukrainian version:

## Візуалізація логів за допомогою гістограми

Створіть гістограму в Kibana, яка відображатиме співвідношення успішних (`statusCode < 400`) і неуспішних (`statusCode >= 400`) запитів. Використовуйте графічне представлення **Vertical Bar** і відобразіть дані за часовою віссю.

### Кроки:

1. Перейдіть до **Dashboard** -> **Create new dashboard**.
2. Натисніть **Create new** -> **Vertical Bar**.
3. Оберіть створений індекс `logstash-*`.
4. У розділі **Buckets** натисніть **Add** -> **X-axis**, оберіть **Date Histogram**, встановіть поле `@timestamp`.
5. Додайте фільтри для `statusCode >= 400` для неуспішних запитів та `statusCode < 400` для успішних.
6. Натисніть **Update**, щоб відобразити графік, і збережіть його на Dashboard.

### Вимоги:

1. Необхідно обрати графічне представлення **Vertical Bar** для візуалізації даних у Kibana.
2. Відобразіть дані за часовою віссю, використовуючи **Date Histogram** на осі X та поле `@timestamp`.
3. Додайте фільтри для відображення успішних запитів (`statusCode < 400`) та неуспішних запитів (`statusCode >= 400`).
4. Використовуйте індекс `logstash-*` для вибірки даних для візуалізації.
5. Після відображення графіка, збережіть його на Dashboard для подальшого використання.