
from djitellopy import Tello
import cv2
import time

            
width = 320
height = 240
startCounter = 1 # 0 for flight 1 for testing

# connect to Tello
Person = Tello()
Person.connect()
Person.for_back_velocity = 0
Person.left_right_velocity = 0
Person.up_down_velocity = 0
Person.yaw_velocity = 0
Person.speed = 0

print(Person.get_battery())
print(Person.get_temperature())

Person.streamoff()
Person.streamon()


while True:
    frame_read = Person.get_frame_read()
    myFrame = frame_read.frame
    img = cv2.resize(myFrame, (width,height))
    #to go up in the begining
    if startCounter == 0:
        Person.takeoff()
        time.sleep(3)
        Person.move_left(20)
        time.sleep(3)
        Person.rotate_clockwise(90)
        time.sleep(3)
        startCounter = 1
    # display image
    cv2.imshow("myFrame", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        Person.land()
        break

    




