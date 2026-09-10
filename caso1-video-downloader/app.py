from flask import Flask, render_template, request, send_file
import yt_dlp
import os
import glob

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download", methods=["POST"])
def download():

    url = request.form.get("url")

    if not url:
        return "Debe ingresar una URL"

    ydl_opts = {

        # Guardamos usando el ID para encontrar fácilmente
        # el archivo después de la descarga
        "outtmpl": os.path.join(
            DOWNLOAD_FOLDER,
            "%(id)s.%(ext)s"
        ),

        "noplaylist": True,

        # yt-dlp selecciona automáticamente
        # el mejor formato disponible
        "merge_output_format": "mp4",

        # Runtime necesario para YouTube
        "js_runtimes": {
            "deno": {}
        },
    }

    try:

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            info = ydl.extract_info(
                url,
                download=True
            )

            video_id = info.get("id")

            titulo = info.get(
                "title",
                "video"
            )

        # Buscar el archivo generado
        archivos = glob.glob(
            os.path.join(
                DOWNLOAD_FOLDER,
                f"{video_id}.*"
            )
        )

        # Quitar archivos temporales
        archivos = [
            archivo
            for archivo in archivos
            if not archivo.endswith(
                (".part", ".ytdl")
            )
        ]

        if not archivos:
            return (
                "El video se descargó, "
                "pero no se encontró el archivo final."
            )

        # Tomar el archivo más reciente
        archivo_final = max(
            archivos,
            key=os.path.getmtime
        )

        # Obtener extensión final
        extension = os.path.splitext(
            archivo_final
        )[1]

        # Enviar al navegador con el título original
        return send_file(
            archivo_final,
            as_attachment=True,
            download_name=f"{titulo}{extension}"
        )

    except Exception as e:

        return (
            f"Error al descargar el video: {str(e)}"
        )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )