FROM php:8.4-fpm-bookworm

# Installer Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    git \
    zip \
    unzip \
    nano \
    zlib1g-dev \
    libpng-dev \
    libonig-dev \
    bash \
    curl \
    libxml2-dev \
    libzip-dev \
    librdkafka-dev \
    g++ \
    make \
    autoconf \
    linux-headers \
    icu-devtools \
    supervisor \
 && rm -rf /var/lib/apt/lists/*

# Installer les extensions PHP
RUN docker-php-ext-install mysqli gd mbstring curl xml zip opcache intl sockets

# Installer les extensions PECL
RUN pecl install xdebug apcu \
 && docker-php-ext-enable apcu xdebug

# Exposer le port FPM
EXPOSE 9000

# Définir le dossier de travail
WORKDIR /var/www