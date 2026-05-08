# Monitoring a Specific Container with docker stats
# Start a container with your application and use the docker stats command
# to monitor its performance. You need to collect information about CPU
# and memory usage peaks over several minutes of testing.
#
# Requirements:
# • A container containing the application must be started using Docker.
#   Make sure that the application inside the container runs successfully.
# • The script must use the docker stats command to monitor container performance,
#   specifically CPU and memory usage.
# • It is necessary to collect information about CPU and memory usage peaks
#   of the container. This data must be obtained during several minutes
#   of performance testing.
# • The script must analyze container performance, detect the moments
#   of the highest CPU and memory load, and record these values
#   for further use.
#
# ## 🇺🇦 Ukrainian version:
#
# Моніторинг конкретного контейнера за допомогою docker stats
# Запустіть контейнер з вашим додатком і використовуйте команду docker stats,
# щоб слідкувати за його продуктивністю.
# Вам потрібно зібрати інформацію про піки використання CPU та пам'яті
# за кілька хвилин тестування.
#
# Вимоги:
# • Необхідно запустити контейнер, у якому знаходиться додаток, використовуючи Docker.
#   Переконайтеся, що додаток всередині контейнера успішно виконується.
# • Скрипт повинен використовувати команду docker stats для моніторингу продуктивності контейнера,
#   зокрема, щодо використання CPU та пам'яті.
# • Необхідно зібрати інформацію про піки використання CPU та пам'яті контейнера.
#   Ці дані мають бути отримані протягом кількох хвилин тестування продуктивності.
# • Скрипт повинен здійснювати аналіз продуктивності контейнера,
#   виявляючи моменти найбільшого навантаження на CPU та пам'ять,
#   і фіксувати ці значення для подальшого використання.

# Starting the application in a container
docker build -t performance-test .
docker run -d --name performance-test-container performance-test

# Monitoring container performance
for i in {1..60}; do
    docker stats --no-stream --format "{{.CPUPerc}} {{.MemUsage}}" performance-test-container
    sleep 5
done | tee performance.log

# Selecting peak values from the logs
echo "Analyzing data..."
grep -Eo '([0-9]+\.[0-9]+)%' performance.log | sort -nr | head -1 | awk '{print "Peak CPU load: "$1}'
grep -Eo '([0-9]+\.[0-9]+MiB)' performance.log | sort -nr | head -1 | awk '{print "Peak memory usage: "$1}'

# Stopping the container after testing
docker stop performance-test-container
docker rm performance-test-container
