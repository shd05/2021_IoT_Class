import cv2

#카메라 장치열기
cap =cv2.VideoCapture(0)  
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
edge1 = cv2.Canny(cap,50,100)
if not cap.isOpened():
    print('Camera open failed')
    exit()


while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame',frame)
    cv2.imshow('frame_GRAY',gray)
    cv2.imshow('edge1',edge1)

    if cv2.waitKey(10) == 27:
        break

#사용자 자원 해제
cap.release()
cv2.destoryAllwindows()