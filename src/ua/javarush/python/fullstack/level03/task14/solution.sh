# Building an Image Using a Build Argument
# Create a Dockerfile that uses a build argument APP_VERSION.
# Pass this argument during the image build with the tag 1.0 and set its value to 1.0.
# After the build, the MY_VERSION environment variable must be available inside the container.
#
# Requirements:
# • The Dockerfile must support the use of the APP_VERSION build argument, which will define the application version.
# • When building the image, the APP_VERSION argument with the value 1.0 must be passed, using the 1.0 tag for the image.
# • Inside the Dockerfile, the MY_VERSION environment variable must be set, and its value must be the value passed
# through the build argument.
#
# ## 🇺🇦 Ukrainian version:
#
# Збірка образу із використанням аргументу
# Створіть Dockerfile, в якому буде використовуватися аргумент збірки APP_VERSION.
# Передайте цей аргумент при збірці образу з тегом 1.0 та встановіть його значення як 1.0.
# Після збірки змінна середовища MY_VERSION повинна бути всередині контейнера.
#
# Вимоги:
# • Dockerfile повинен передбачати використання аргументу збірки APP_VERSION, який визначатиме версію застосунку.
# • При збірці образу необхідно передати аргумент APP_VERSION зі значенням 1.0, використовуючи тег 1.0 для образу.
# • Усередині Dockerfile необхідно встановити змінну середовища MY_VERSION, значення якої буде передане значення
# аргументу збірки.

# Building the image with the argument passed and the tag
docker build --build-arg APP_VERSION=1.0 -t myapp:1.0 .

# Running the container:
docker run myapp:1.0