# Tahaluf Al Emarat MLOps Task

## What the repo does
This solution streams a video on loop to a RTSP server, when a GET request reaches the server then a frame is taken from the streamed video and passed to a YOLOv5 model for object detection inference. The resulting image (original frame with bounding boxes drawn on it) is then saved to a directory on the host machine and its path is returned in the original request response.

## What the repo contains
This solution is built using 3 Docker containers, all controlled and managed by Docker Compose.

- rtsp-server: docker container for the RTSP server, necessary for RTSP streaming.
- ffmpeg-streamer: docker container that is responsible for streaming the surveillance video to rtsp-server (dependant on rtsp-server).
- flask-app: docker container for the flask app that is responsible for receiving the GET requests, loading the YOLOv5 model, performing inference and returning the path of the written image (dependant on ffmpeg-streamer).

## How to use the repo
- `cd` into the root directory of the project
- Run `docker compose build`
- Run `docker compose up`
- When flask server is up and running, send a request by running `python3 main.py` in the command line.
- The response is the path in the host machine where the inference image is saved.