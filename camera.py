from picamera import PiCamera
from time import sleep

camera = PiCamera()

action = input("Enter 1 for photo or 2 for video: ")

camera.rotation = 180

if action == "1":
  camera.start_preview() # Previews only temporarily necessary
  sleep(5)
  camera.capture('/home/pi/Desktop/folder/images/image.jpg')
  camera.stop_preview()
elif action == "2":
  duration = input("Video length is seconds: ")
  camera.brightness = 55
  camera.start_preview()
  camera.start_recording('/home/pi/Desktop/folder/videos/video.h264')
  sleep(int(duration) - 1)
  camera.stop_recording()
  camera.stop_preview()
else:
  print("You did not enter 1 or 2")

# Insert API code here, use picture from above.

print("Done execution.")
