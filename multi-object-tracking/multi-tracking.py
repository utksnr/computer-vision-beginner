import cv2

obj_trackers = {'csrt': cv2.legacy.TrackerCSRT_create,
                    'kcf' : cv2.legacy.TrackerKCF_create,
                    'boosting' : cv2.legacy.TrackerBoosting_create,
                    'mil': cv2.legacy.TrackerMIL_create,
                    'tld': cv2.legacy.TrackerTLD_create,
                    'medianflow': cv2.legacy.TrackerMedianFlow_create,
                    'mosse':cv2.legacy.TrackerMOSSE_create}

trackers =cv2.legacy.MultiTracker_create()

cap =cv2.VideoCapture(0)

while True:
    frame = cap.read()[1]
    
    if frame is None:
        break
        
    frame = cv2.resize(frame,(800,600))

    succes, boxes = trackers.update(frame)

    for box in boxes:
        x,y,w,h = [int(i) for i in box]

        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

    cv2.imshow("tracking",frame)
    key = cv2.waitKey(10)
    
    if key == ord("s"):
        roi = cv2.selectROI("tracking",frame)
        tracker = obj_trackers["kcf"]()
        
        trackers.add(tracker,frame,roi)
    
    
    if key == ord("q"):
        break
    
    
cap.release
cv2.destroyAllWindows()