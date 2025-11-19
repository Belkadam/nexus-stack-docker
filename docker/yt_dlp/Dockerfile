FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    ffmpeg \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Installer yt-dlp
RUN pip install yt-dlp

# Créer dossier pour stocker les vidéos
RUN mkdir -p /media

WORKDIR /media

CMD ["tail", "-f", "/dev/null"]