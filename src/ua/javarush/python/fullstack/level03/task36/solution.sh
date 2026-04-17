# Using a Tag for Image Versioning
# Create a Dockerfile for a simple application, build two images with different versions — yourusername/myapp:1.0 and yourusername/myapp:2.0. Then publish both images to Docker Hub and run containers for each version.
#
# Requirements:
# • The Dockerfile must be developed for a simple application so that it can be used to build images.
# • It is necessary to build two application images with the tags yourusername/myapp:1.0 and yourusername/myapp:2.0 to provide versioning.
# • Both built images, yourusername/myapp:1.0 and yourusername/myapp:2.0, must be published to Docker Hub for public use.
# • Containers must be run separately for each image version — yourusername/myapp:1.0 and yourusername/myapp:2.0 — to verify that they work correctly.
#
# ## 🇺🇦 Ukrainian version:
# Використання тега для версіонування образів
# Створіть Dockerfile для простого додатка, зберіть два образи з різними версіями — yourusername/myapp:1.0 і yourusername/myapp:2.0. Потім опублікуйте обидва образи в Docker Hub і запустіть контейнери для кожної версії.
#
# Вимоги:
# • Dockerfile має бути розроблений для простого додатка, щоб його можна було використовувати для збирання образів.
# • Необхідно зібрати два образи додатка з тегами yourusername/myapp:1.0 і yourusername/myapp:2.0, щоб забезпечити версіонування.
# • Обидва зібрані образи, yourusername/myapp:1.0 і yourusername/myapp:2.0, мають бути опубліковані в Docker Hub для їх загального використання.
# • Контейнери мають бути запущені окремо для кожної версії образу — yourusername/myapp:1.0 і yourusername/myapp:2.0, щоб перевірити їх працездатність.

# Copy app_v1.py to app.py (for building version 1.0).
cp app_v1.py app.py

# Build the version 1.0 image:
docker build -t yourusername/myapp:1.0 .


# Copy app_v2.py to app.py (for building version 2.0).
cp app_v2.py app.py

# Build the version 2.0 image:
docker build -t yourusername/myapp:2.0 .


# Authentication with Docker Hub (this requires entering credentials)
docker login

# Publishing the images to Docker Hub:
docker push yourusername/myapp:1.0
docker push yourusername/myapp:2.0

# Running containers for each version:
docker run --rm yourusername/myapp:1.0
docker run --rm yourusername/myapp:2.0