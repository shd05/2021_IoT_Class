import cv2


face_cascade= cv2.CascadeClassifier('./xml/face.xml')

img = cv2.imread('AVENG.jpg')
gray = cv2.cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destoroyAllwindows()