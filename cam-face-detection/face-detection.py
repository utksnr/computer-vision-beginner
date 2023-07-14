import cv2

fcd=cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

def detect(img):

    face=img.copy()
    rectangle = fcd.detectMultiScale(face,scaleFactor=1.2,minNeighbors=4)

    for(x,y,w,h) in rectangle:
        cv2.rectangle(face,(x,y),(x+w,y+h),(255,255,0),2)
    return face

cam = cv2.VideoCapture(0)

while True:
    ret,frame = cam.read(0)
    frame = detect(frame)

    cv2.imshow("Camera",frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows() 


