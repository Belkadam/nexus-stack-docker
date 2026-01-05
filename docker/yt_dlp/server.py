from fastapi import FastAPI
from fastapi.responses import JSONResponse
import subprocess
import uuid
import os

app = FastAPI()

MEDIA_DIR = "/media"

@app.get("/download")
def download(videoId: str):
    file_id = str(uuid.uuid4())
    output_template = f"{MEDIA_DIR}/{file_id}.%(ext)s"

    cmd = [
        "yt-dlp",
        "--cookies", "/app/cookies.txt",
        "-f", "ba/b",
        "-o", output_template,
        f"https://www.youtube.com/watch?v={videoId}"
    ]

    try:
        subprocess.run(cmd, check=True)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

    # Get the file
    files = [f for f in os.listdir(MEDIA_DIR) if f.startswith(file_id)]
    if not files:
        return JSONResponse(status_code=500, content={"error": "file_not_found"})

    filename = files[0]

    return {
        "status": "ok",
        "file": filename,
        "path": f"/media/{filename}"
    }