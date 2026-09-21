import re

from ultralytics import YOLO
import cv2

class VehicleDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, frame):
        # predict görevi şu görüntüyü analiz et tarzı
        results = self.model.predict(
            source=frame, # modele frame gönderiyoruz
            verbose=False # her frame için bilgi vermesin diye false
            )

        detection = []

        for result in results:
            if result.boxes is None:
                continue

            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist() # konumları dönüştürme düzgüne
                confidence = float(box.conf[0]) # eminlik oranı
                class_id = int(box.cls[0]) # class id çektik
                class_name = self.model.names[class_id] # o id hangi isme karşılık geliyor onu aldık
                
                detection.append({
                    "bbox": [int(x1), int(y1), int(x2), int(y2)],
                    "confidence": confidence,
                    "class_id": class_id,
                    "class_name": class_name
                })

        return detection