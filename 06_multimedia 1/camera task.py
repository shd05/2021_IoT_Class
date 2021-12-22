import cv2

img = cv2.imread('IU.jpg')
img2 = cv2.resize(img,(600,400))

cv2. imshow('IU',img)

edge1 = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

cv2.imshow('edge1',edge1)
cv2.imshow('edge2',edge2)
cv2.imshow('edge3',edge3)

cv2.waitKey()

cv2.destroyAllwindows()

import cv2

#카메라 장치열기
cap =cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

fourcc = cv2.VideoWriter_fourcc(*'DIVX')

#동영상 저장을 위한 videoWriter 객체 생성
out = cv2.VideoWriter('output.avi',fourcc,30,(640,480))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame',frame)

    if cv2.waitKey(10) == 27:
        break

#사용자 자원 해제
cap.release()
cv2.destoryAllwindows()