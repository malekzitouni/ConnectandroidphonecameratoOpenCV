import cv2
import numpy as np
import requests

url = "https://192.168.2.149:8080/shot.jpg"
output_file = 'web.avi'  # Change the file extension to '.avi'
fps = 20
frame_width = 1200
frame_height = 480
frame_size = (frame_width, frame_height)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Use MJPG codec
video_writer = cv2.VideoWriter(output_file, fourcc, fps, frame_size)

while True:
    try:
        response = requests.get(url, verify=False)
        img_arr = np.array(bytearray(response.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        img = cv2.resize(img, (500, 500))
        cv2.imshow("Android_cam", img)
        video_writer.write(img)

        # Press Esc key to exit
        if cv2.waitKey(1) == 27:
            break
    except Exception as e:
        print(f"Error: {e}")

video_writer.release()
cv2.destroyAllWindows()

