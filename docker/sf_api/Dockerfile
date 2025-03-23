FROM php:8.4-fpm

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git zip unzip nano zlib1g-dev libpng-dev libonig-dev bash libcurl4-openssl-dev \
    libxml2-dev libzip-dev librdkafka-dev g++ make autoconf libicu-dev supervisor \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install required PHP extensions
RUN docker-php-ext-install mysqli gd mbstring curl xml zip opcache intl sockets pdo pdo_mysql

# Install and enable PECL extensions
RUN pecl install xdebug apcu && docker-php-ext-enable apcu

# Expose the PHP-FPM port
EXPOSE 9000

# Set the working directory
WORKDIR /var/www
