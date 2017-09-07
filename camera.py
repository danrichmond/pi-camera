from picamera import PiCamera
from time import sleep

camera = PiCamera()

action = input("Enter 1 for photo or 2 for video: ")

camera.rotation = 180

if action == "1":
  camera.start_preview() # Is the preview necessary?
  sleep(5)
  camera.capture('/home/pi/Desktop/folder/images/image.jpg')
  camera.stop_preview() # Is the preview necessary?
elif action == "2":
  duration = input("Video length is seconds: ")
  camera.brightness = 55
  camera.start_preview() # Is the preview necessary?
  camera.start_recording('/home/pi/Desktop/folder/videos/video.h264')
  sleep(int(duration) - 1) # Record for duration user gave
  camera.stop_recording()
  camera.stop_preview() # Is the preview necessary?
else:
  print("You did not enter 1 or 2")

print("Done execution.")
