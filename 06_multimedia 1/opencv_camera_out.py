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