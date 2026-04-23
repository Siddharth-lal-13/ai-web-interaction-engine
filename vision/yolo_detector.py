# vision/yolo_detector.py

from ultralytics import YOLO
import cv2
from typing import List, Dict


class YoloDetector:
    def __init__(self, model_path: str = "models/yolov8n.pt"):
        """
        Initialize YOLOv8 model
        """
        self.model = YOLO(model_path)

    def detect(self, image_path: str) -> List[Dict]:
        """
        Run object detection on image

        Returns:
            List of detections with bounding boxes and labels
        """
        results = self.model(image_path)

        detections = []

        for result in results:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                label = self.model.names[cls_id]
                coords = box.xyxy[0].tolist()

                detections.append({
                    "label": label,
                    "confidence": float(box.conf[0]),
                    "bbox": coords
                })

        return detections

    def draw_detections(self, image_path: str, output_path: str):
        """
        Save image with bounding boxes
        """
        img = cv2.imread(image_path)
        results = self.model(image_path)

        annotated = results[0].plot()
        cv2.imwrite(output_path, annotated)