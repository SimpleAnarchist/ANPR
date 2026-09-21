import cv2


class VideoReader:
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)

        if not self.cap.isOpened():
            raise Exception("Video açılamadı")

        # metadata hazırla
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = float(self.cap.get(cv2.CAP_PROP_FPS))
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def get_metadata(self):
        return {
            "width": self.width,
            "height": self.height,
            "fps": self.fps,
            "total_frames": self.total_frames
        }

    def read(self):
        ret, frame = self.cap.read()

        if not ret:
            return None

        return frame

    def release(self):
        self.cap.release()