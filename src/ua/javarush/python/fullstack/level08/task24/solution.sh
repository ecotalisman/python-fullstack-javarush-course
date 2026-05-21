# Obtaining an SSL Certificate from Let's Encrypt
#
# Configure a secure HTTPS connection using an SSL certificate
# obtained with Let's Encrypt.
# Implement redirection of HTTP requests to HTTPS.
#
# Requirements:
#
# 1. Install and configure a Let's Encrypt client, such as Certbot,
#    to automatically obtain an SSL certificate.
# 2. Use the Let's Encrypt client to obtain a valid SSL certificate
#    for your domain name.
# 3. Configure the web server to use the obtained SSL certificate
#    for a secure HTTPS connection.
# 4. Configure the web server so that all HTTP requests
#    are automatically redirected to HTTPS.
#
# 🇺🇦 Ukrainian version:
#
# Отримання SSL сертифіката з Let's Encrypt
#
# Налаштуйте захищене з'єднання HTTPS з використанням SSL-сертифіката,
# отриманого за допомогою Let's Encrypt.
# Реалізуйте перенаправлення HTTP-запитів на HTTPS.
#
# Вимоги:
#
# 1. Встановіть і налаштуйте клієнт Let's Encrypt, наприклад Certbot,
#    для автоматичного отримання SSL-сертифіката.
# 2. Використовуйте клієнт Let's Encrypt для отримання чинного SSL-сертифіката
#    для вашого доменного імені.
# 3. Налаштуйте вебсервер на використання отриманого SSL-сертифіката
#    для захищеного з'єднання через HTTPS.
# 4. Налаштуйте вебсервер так, щоб усі HTTP-запити
#    автоматично перенаправлялися на HTTPS.

# Build the Docker image:
docker build -t nginx-ssl .

# Run the Docker container:
docker run -p 80:80 -p 443:443 --name nginx-ssl nginx-ssl

# Inside the container, run the script to obtain the SSL certificate:
docker exec -it nginx-ssl /bin/bash \
  certbot certonly --nginx -d example.com -d www.example.com \
  --non-interactive --agree-tos -m your-email@example.com