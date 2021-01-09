#this is a file to run the camera and send fiel to firebase database, similar to lab in week 10
#The pic gets stored on file and then published to firebase database, using similar to webhooks

from picamera import PiCamera
import datetime
from time import sleep
import store_FileFB


camera = PiCamera()
camera.start_preview()

def cam():
    frame = 1 

    fileLoc = f'/home/pi/assignmentIOT/img/frame{frame}.jpg' # set location of image file and current time
    currentTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    camera.capture(fileLoc) # capture image and store in fileLoc
    print(f'frame {frame} taken at {currentTime}') # print frame number to console
    store_FileFB.store_file(fileLoc)
    store_FileFB.push_db(fileLoc, currentTime)
    frame += 1
    sleep(2)
    camera.stop_preview()
    return

   


