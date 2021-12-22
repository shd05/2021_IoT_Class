import picamera
import time  

path = '/home/pi/src5/06_multimedia'

camera = picamera.PiCamera()

try:
    camera.resolution = (640,480)
    camera.start_preview()
    time.sleep(3) # 카메라 촬영시 준비시간
    camera.rotation = 180
    camera.start_recording('%s/video.h264' % path)
    # camera.capture('%s/photo.jpg' % path) #사진촬영
    input('press enter to stop')
    time.sleep(10)
    camera.stop_recording()

finally:
    camera.stop_preview()