# Using the official Python image as the base image
FROM python

# Setting the working directory inside the container
WORKDIR /app

# Copying the dependencies file into the container
COPY requirements.txt ./

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying the application code into the container
COPY . .

# Specifying the default command to run the container
CMD ["python", "app.py"]