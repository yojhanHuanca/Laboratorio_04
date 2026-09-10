FROM python:3.11-slim

WORKDIR /app

# Instalar FFmpeg y herramientas necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    unzip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Instalar Deno para que yt-dlp funcione correctamente con YouTube
ARG DENO_VERSION=2.9.6

RUN curl -fsSL \
    "https://github.com/denoland/deno/releases/download/v${DENO_VERSION}/deno-x86_64-unknown-linux-gnu.zip" \
    -o /tmp/deno.zip \
    && unzip /tmp/deno.zip -d /usr/local/bin \
    && rm /tmp/deno.zip \
    && chmod +x /usr/local/bin/deno

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicación
COPY app.py .

# Copiar interfaz
COPY templates ./templates

# Crear carpeta para las descargas
RUN mkdir -p /app/downloads

# Puerto utilizado por Flask
EXPOSE 5000

# Ejecutar aplicación
CMD ["python", "app.py"]