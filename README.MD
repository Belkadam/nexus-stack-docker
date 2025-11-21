### Activate xdebug on PhpStorm
- Go settings PHP -> servers  and add new server:
  - Name: sf-api
  - Host: 127.0.0.1
  - Port: 8083
  - Activate path maping and map to: /var/www/sf-api
### Test downloading audio with Yt-Dlp
- Enter in Yt-Dlp container `docker exec -it yt-dlp bash`
- Download audio by running `yt-dlp -f bestaudio -o "/media/test.%(ext)s" "https://www.youtube.com/watch?v=dQw4w9WgXcQ"`