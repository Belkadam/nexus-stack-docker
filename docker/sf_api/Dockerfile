FROM php:8.4-fpm

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN apk add git zip unzip nano zlib-dev libpng-dev oniguruma-dev bash curl-dev libxml2-dev libzip-dev librdkafka-dev g++ make autoconf linux-headers icu-dev supervisor

RUN docker-php-ext-install mysqli gd mbstring curl xml zip opcache intl sockets pdo pdo_mysql

RUN pecl install xdebug apcu

RUN docker-php-ext-enable apcu

EXPOSE 9000

WORKDIR /var/www
