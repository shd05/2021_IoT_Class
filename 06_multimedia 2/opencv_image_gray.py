import cv2

img = cv2.imread('IU.jpg')
img2 = cv2.resize(img,(600,400))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('IU',img2)
cv2.imshow('IU_GRAY',gray)

while True:
    if cv2.waitKey() == 13:
        break

cv2.imwrite('IU_GRAY.jpg',gray)

cv2.destoryAllwindows()