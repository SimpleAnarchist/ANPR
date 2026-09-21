import cv2
import time

cap = cv2.VideoCapture("videos/guzel_olan.mp4")
ptime = 0
if not cap.isOpened():
    print("Error: Video açılamadı.")
    exit()

genislik = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
yukseklik = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps2 = round(cap.get(cv2.CAP_PROP_FPS),2)
toplam_kare = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(f"Video boyutu: {genislik}x{yukseklik}")
print(f"Video FPS: {fps2}")
print(f"Toplam Kare: {toplam_kare}")
print(f"Çözünürlük: {genislik}x{yukseklik}")


while True:
    ret, frame = cap.read()

    # ret False ise video bitti veya okunamadı okunup okunamadığına bakıyor
    if not ret:
        print("Video bitti veya okunamadı.")
        break

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Video", frame)

    # q basıldığında çıkış
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()