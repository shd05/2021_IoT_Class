import picamera
import time

path = '/home/pi/src5/06_multimedia'

camera = picamera.PiCamera()

try:
    while True:
        val = input('photo: 1, video: 2, exit 9')

        camera.resolution = (640,480)
        camera.start_preview()
        time.sleep(3) # 카메라 촬영시 준비시간
        if val =='1':
            
            print("사진촬영")
            now_str = time.strftime("%Y%m%d_%H%M%S")
            camera.capture('%s/photo_%s.jpg'% (path,now_str)) #사진촬영
            time.sleep(10)
            
        elif val =='2':     
            now_str = time.strftime("%Y%m%d_%H%M%S")
            print("동영상 촬영")
            camera.start_recording('%s/video_%s.h264' % (path, now_str))
            time.sleep(10)
            camera.stop_recording()
        elif val =='9':
            break
        else:
            print("incorrect command")
finally:
    camera.stop_preview()