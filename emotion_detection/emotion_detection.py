import cv2
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
from deepface import DeepFace

clf = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cam = cv2.VideoCapture(0)

while True:
    _,frame = cam.read()
    gray_cam = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(gray_cam,scaleFactor=1.2,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
    res = DeepFace.analyze(frame, actions=("emotion",),enforce_detection=False)
    dominant=(res[0]["dominant_emotion"])


    for (x,y,w,h) in faces:
        cv2.putText(frame,text=dominant, org=(x,y), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(255,255,0))
        cv2.rectangle(frame,(x,y), (x+w, y+h), (255,255,0),2)

    cv2.imshow("",frame)
    if cv2.waitKey(20) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()