# Encrypting Data in Transit
# Run a container with Nginx and configure it to use an encrypted TLS connection.
# To do this, use the cert.pem certificate and the key.pem key,
# which must be mounted into the container.
#
# Requirements:
# • The container must use the Nginx image to run the web server.
# • Nginx must be configured to use TLS for an encrypted connection when transmitting data.
# • The cert.pem certificate and the key.pem key must be mounted into the Nginx container
#   for use in the TLS configuration.
#
# ## 🇺🇦 Ukrainian version:
#
# Шифрування даних при передачі
# Запустіть контейнер з Nginx та налаштуйте його на використання зашифрованого з'єднання TLS.
# Для цього використовуйте сертифікат cert.pem та ключ key.pem,
# які повинні бути змонтовані в контейнер.
#
# Вимоги:
# • Контейнер має використовувати образ Nginx для запуску веб-сервера.
# • Nginx повинен бути налаштований на використання TLS для зашифрованого з'єднання при передачі даних.
# • Сертифікат cert.pem та ключ key.pem повинні бути змонтовані в контейнер з Nginx
#   для використання в налаштуваннях TLS.

# Run a container with Nginx, mounting the certificates and keys for using TLS
docker run -d -p 443:443 --name tls_container \
 -v $(pwd )/cert.pem:/etc/nginx/cert.pem \
 -v $(pwd)/key.pem:/etc/nginx/key.pem \
 -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf \
 nginx