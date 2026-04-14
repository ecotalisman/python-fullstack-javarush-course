# Forwarding a Range of Ports
# Run a container based on the someimage image, forwarding the range of container ports
# from 6000 to 7000 to host machine ports from 8000 to 9000.
#
# Requirements:
# • The container must be started based on the someimage image.
# • The range of container ports from 6000 to 7000 must be forwarded to host machine ports from 8000 to 9000.
# • The container must be started in detached mode.
#
# ## 🇺🇦 Ukrainian version:
#
# Перенаправлення діапазону портів
# Запустіть контейнер на основі образу someimage, перенаправивши діапазон портів з 6000 по 7000 контейнера на порти з 8000 по 9000 хост-машини.
#
# Вимоги:
# • Контейнер має бути запущено на основі образу someimage.
# • Діапазон портів з 6000 по 7000 контейнера має бути перенаправлено на порти з 8000 по 9000 хост-машини.
# • Контейнер має бути запущено в фоновому режимі (detached mode).

# Run a container based on the someimage image, forwarding the range of container ports
# from 6000 to 7000 to host machine ports from 8000 to 9000
docker run -d -p 8000-9000:6000-7000 someimage