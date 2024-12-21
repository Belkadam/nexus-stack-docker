FROM ubuntu:latest
LABEL authors="adam"

ENTRYPOINT ["top", "-b"]