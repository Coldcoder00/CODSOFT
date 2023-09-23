import cv2

body_cascade = cv2.CascadeClassifier("c:/Users/admin/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Camera not opened.")
    exit()

while True:
    ret, frame = video_capture.read()

    if not ret:
        print("Error: Failed to read frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = body_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("video_feed", frame)

    if cv2.waitKey(10) == ord("s"):
        print("Exiting loop.")
        break

video_capture.release()
cv2.destroyAllWindows()