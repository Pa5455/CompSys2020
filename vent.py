import RPi.GPIO as GPIO
from time import sleep
from temp_hum import environment_temp 


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25, GPIO.OUT)

pwm = GPIO.PWM(25, 50)
pwm.start(0)


def setAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(25, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(25, False)
    pwm.ChangeDutyCycle(duty)

   

def vent_open():
    setAngle(30)
    #print("Vent Open!")
    

def vent_close():
    setAngle(0)
    #print("Vent Closed")

def auto_vent():
        temp=environment_temp()
        sleep(2)  
        if temp > 25:
            vent_open()
            vent_pos = 1
            sleep(5)
        else:
            vent_close()
            vent_pos = 0
            sleep(5)
        return vent_pos






