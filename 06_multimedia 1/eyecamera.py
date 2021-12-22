import cv2
import numpy as np

fc = cv2.CascadeClassifier('./xml/face.xml')
eye = cv2.CascadeClassifier('./xml/eye.xml') 

cap = cv2.VideoCapture(0) 
cap.set(3,640) 
cap.set(4,480)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = fc.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize=(20,20)) 
    for (x,y,w,h) in faces: 
        cv2.rectangle(img, (x,y), (x+w, y+h), (100,150,100) ,2)
        roi_gray = gray[y:y+h, x:x+w]

    eyes = eye.detectMultiScale(gray) 
    for(ex, ey, ew, eh) in eyes: 
        cv2.rectangle(img, (ex,ey), (ex+ew, ey+eh), (0,0,255) ,2)
    cv2.imshow('video', img)
    k= cv2.waitKey(30)&0xff 
    if k == 27:
        break

cap.release()
cv2.destroyAllwindows()