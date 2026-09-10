# 🎬 Descargador de Videos con Flask y Docker

Aplicación web desarrollada en **Python con Flask**, que permite descargar videos mediante una URL utilizando `yt-dlp`.

Este proyecto corresponde al **Caso 1 de la Práctica Calificada 1** del curso **Desarrollo de Soluciones en la Nube**, aplicando Docker para la contenerización y ejecución de la aplicación.

---

## 📌 Descripción del proyecto

El sistema permite ingresar la URL de un video desde una interfaz web. La aplicación procesa el enlace utilizando `yt-dlp` y posteriormente permite descargar el archivo obtenido.

El proyecto contempla la descarga de contenido desde plataformas compatibles como:

- YouTube
- Instagram
- TikTok
- Facebook
- LinkedIn

> La disponibilidad de la descarga depende de las restricciones de cada plataforma. La aplicación debe utilizarse únicamente con contenido que el usuario tenga autorización para descargar.

---

## 🎯 Objetivo

Desarrollar una aplicación web para la descarga de videos y posteriormente contenerizarla utilizando Docker.

Como parte de la práctica se implementaron tres configuraciones:

- `Dockerfile`
- `Dockerfile.optimizado`
- `Dockerfile.multistage`

Esto permite aplicar diferentes técnicas de construcción y optimización de imágenes Docker.

---

## ⚙️ Tecnologías utilizadas

- Python 3.11
- Flask
- yt-dlp
- FFmpeg
- Deno
- HTML
- CSS
- Docker
- Git
- GitHub

---

## 📁 Estructura del proyecto

```text
caso1-video-downloader/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Dockerfile.optimizado
├── Dockerfile.multistage
├── .dockerignore
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
└── downloads/
```

---

# 🚀 Instalación y ejecución local

## 1. Clonar el repositorio

```bash
git clone URL-DE-TU-REPOSITORIO
```

Luego ingresar a la carpeta del proyecto:

```bash
cd caso1-video-downloader
```

---

## 2. Instalar las dependencias

Ejecutar:

```bash
pip install -r requirements.txt
```

---

## 3. Ejecutar la aplicación

```bash
python app.py
```

Una vez iniciado Flask, abrir en el navegador:

```text
http://localhost:5000
```

---

# 💻 Uso de la aplicación

Para utilizar el sistema:

1. Abrir la aplicación desde el navegador.
2. Copiar la URL del video que se desea descargar.
3. Pegar la URL en el campo correspondiente.
4. Presionar el botón de descarga.
5. Esperar mientras la aplicación procesa el video.
6. El archivo obtenido será enviado al navegador para su descarga.

---

# 🐳 Dockerización

El proyecto cuenta con tres archivos Docker para evaluar diferentes formas de construcción de la aplicación.

## 1. Dockerfile estándar

Construir la imagen:

```bash
docker build -t downloader:v1.0 .
```

Ejecutar el contenedor:

```bash
docker run -d -p 5000:5000 --name downloader-app downloader:v1.0
```

Luego acceder desde:

```text
http://localhost:5000
```

---

## 2. Dockerfile optimizado

Construir la imagen optimizada:

```bash
docker build -f Dockerfile.optimizado -t downloader:optimizado .
```

Esta versión incorpora mejoras orientadas a reducir archivos innecesarios y mejorar la ejecución del contenedor.

---

## 3. Dockerfile multistage

Construir la imagen:

```bash
docker build -f Dockerfile.multistage -t downloader:multistage .
```

Esta versión utiliza una construcción por etapas para separar la instalación de dependencias del entorno final de ejecución.

---

# 🔍 Verificación de imágenes Docker

Para visualizar las imágenes creadas:

```bash
docker images downloader
```

Se pueden observar las tres versiones:

```text
downloader:v1.0
downloader:optimizado
downloader:multistage
```

---

# 📦 Verificación del contenedor

Para comprobar que el contenedor se encuentra en ejecución:

```bash
docker ps
```

Para visualizar los registros de la aplicación:

```bash
docker logs downloader-app
```

Para detener el contenedor:

```bash
docker stop downloader-app
```

---

# 🎥 Video demostrativo

Se realizó **un video demostrativo correspondiente al Caso 1: Descargador de Videos**, donde se muestra el funcionamiento de la aplicación.

En el video se puede observar el ingreso de una URL, el procesamiento del contenido y la descarga del video mediante la aplicación desarrollada.

▶️ **[Ver video demostrativo](PON-AQUI-EL-ENLACE-DEL-VIDEO)**

> El enlace permite acceder a la evidencia audiovisual del funcionamiento del proyecto.

---

# 📊 Evidencias

Durante el desarrollo se verificó:

- La construcción de la imagen Docker.
- La creación y ejecución del contenedor.
- El acceso a la aplicación desde el navegador.
- El funcionamiento de la interfaz web.
- El procesamiento de URLs mediante `yt-dlp`.
- La descarga del archivo resultante.
- La creación de las versiones estándar, optimizada y multistage.

---

# 📝 Conclusiones

- Se desarrolló una aplicación web funcional utilizando Python, Flask y `yt-dlp` para realizar la descarga de videos mediante una URL.

- Docker permitió contenerizar la aplicación y sus dependencias, facilitando su ejecución en un entorno controlado.

- Se implementaron tres configuraciones de Docker: estándar, optimizada y multistage, permitiendo aplicar diferentes estrategias de construcción de imágenes.

- El uso de `.dockerignore` y `.gitignore` permitió excluir archivos innecesarios, archivos temporales y videos descargados del repositorio.

- La práctica permitió aplicar conocimientos de desarrollo web, gestión de dependencias, Docker, construcción de imágenes y ejecución de contenedores.

---
## 👩‍💻 Autor

**Yojhan Huannca Yucra**  


**Curso:** Desarrollo de Soluciones en la Nube

