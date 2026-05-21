FROM nginx:latest

# Install Certbot to obtain SSL certificates
RUN apt-get update && \
    apt-get install -y certbot python3-certbot-nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the source Nginx configuration files
COPY ./default.conf /etc/nginx/conf.d/

# Specify the container entry point
CMD ["nginx", "-g", "daemon off;"]