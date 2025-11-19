### Test downloading audio with Yt-Dlp
- Enter in Yt-Dlp container `docker exec -it yt-dlp bash`
- Download audio by running `yt-dlp -f bestaudio -o "/media/test.%(ext)s" "https://www.youtube.com/watch?v=dQw4w9WgXcQ"`