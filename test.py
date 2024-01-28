import time
import multiprocessing
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor

import cv2

model = YOLO("y8best.pt")

def test():
    while True:
        print(model.predict(source=f"{multiprocessing.current_process().name}.mp4", show=True))


if __name__ == '__main__':
    multiprocessing.freeze_support()
    multiprocessing.Process(target=test, name="1").start()
    multiprocessing.Process(target=test, name="2").start()