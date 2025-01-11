import os
import wandb
from ultralytics import YOLO
from PIL import Image
import wget


model_predict = YOLO("runs/detect/train3/weights/best.pt")


def perform_detection(image_path, save=True, save_dir='runs/detect/predict'):
    results = model_predict.predict(image_path, save=save, save_dir=save_dir)
    return results


if __name__ == "__main__":
    test_image_path = "/Users/yixuan/Desktop/Unjuanable/Github/yolov11/YOLOv11-Face-Mask-Detection/duolaAmeng.jpeg"
    perform_detection(test_image_path)
