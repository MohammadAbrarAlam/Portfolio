import cv2
import threading

def start_camera():
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        cv2.imshow("Abrar Vision AI", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

def run_camera():
    threading.Thread(target=start_camera, daemon=True).start()