import os
from datetime import datetime

import cv2
import torch
from flask import Flask

app = Flask(__name__)

video_capture = cv2.VideoCapture('rtsp://rtsp-server:8554/videostream')
model = torch.hub.load("ultralytics/yolov5", "yolov5s")

output_directory = os.getenv('OUTPUT_DIR')

def get_inference(img):
    result = model(img)
    return result.pandas().xyxy[0]

def draw_bboxes(img, bboxes):
    for _, bbox in bboxes.iterrows():
        x1, y1, x2, y2 = int(bbox['xmin']), int(bbox['ymin']), int(bbox['xmax']), int(bbox['ymax'])
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return img

def write_inference(img):
    timestamp_str = datetime.now().strftime("%M%S")
    output_filename = f'image-{timestamp_str}.jpg'
    output_path = os.path.join('images', output_filename)
    cv2.imwrite(output_path, img) 
    return os.path.join(output_directory, output_filename)


@app.route('/get_frame')
def get_frame():
    for _ in range(10):
        success, frame = video_capture.read()
    
    if success:

        bboxes = get_inference(frame)
        drawn_img = draw_bboxes(frame, bboxes)
        img_path = write_inference(drawn_img)

        return img_path
        
    else:
        return "Error", 500 

if __name__ == "__main__":
    app.run(host='0.0.0.0')
