import cv2

from src.video.video_reader import VideoReader
from src.detection.vehicle_detector import VehicleDetector

CONFIDENCE_THRESHOLD = 0.5
BOX_COLOR = (0, 255, 0)
FONT = cv2.FONT_HERSHEY_SIMPLEX

def main():

    # Video okuyucuyu oluştur
    reader = VideoReader("videos/anpr-demo-video.mp4")

    # Araç tespit modelini oluştur
    detector = VehicleDetector("models/yolo11s.pt")

    # Video bitene kadar devam et
    while True:

        frame = reader.read()

        # Video bittiyse çık
        if frame is None:
            break

        # Araçları tespit et
        detections = detector.detect(frame)
        

        for detection in detections:
            bbox = detection["bbox"] # burada detection["bbox"] ile tespit edilen aracın konumunu alıyoruz
            class_name = detection["class_name"] # burada detection["class_name"] ile tespit edilen aracın sınıf ismini alıyoruz
            confidence = detection["confidence"] # burada detection["confidence"] ile tespit edilen aracın güven skorunu alıyoruz

            if confidence < CONFIDENCE_THRESHOLD:  # güven skoru CONFIDENCE_THRESHOLD'ten düşükse atla
                continue

            x1, y1, x2, y2 = bbox

            # Tespit edilen araçları çerçevele
            cv2.rectangle(frame, (x1, y1), (x2, y2), BOX_COLOR, 2) # çizgi çekme

            cv2.putText(frame,f"{class_name} ({confidence:.2f})",(x1, y1-10),FONT,0.5,BOX_COLOR,2) # yazdırma
            
        # Şimdilik terminale yazdır
        # print(detections)

        # Videoyu göster
        cv2.imshow("ANPR", frame)

        # q ile çık
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    reader.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()