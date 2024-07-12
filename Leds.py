import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)#sets the GPIO pins as outputs
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)


def Flash(colour,len):
	colours = {'blue': 23, 'red': 24, 'green': 25}  #the gpio pins each colour corrosponds to 
	GPIO.output(colours[colour], True)
	time.sleep(len)
	GPIO.output(colours[colour], False)
	
def On(colour):
	colours = {'blue': 23, 'red': 24, 'green': 25} #the gpio pins each colour corrosponds to 

def Off(colour):
	colours = {'blue': 23, 'red': 24, 'green': 25} #the gpio pins each colour corrosponds to 
	GPIO.output(colours[colour], False)
