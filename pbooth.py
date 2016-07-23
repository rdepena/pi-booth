import time
import os
import RPi.GPIO as GPIO
from subprocess import call
from picamera import PiCamera

BUTTON_PIN = 18
LED_PIN = 17
HOME = '/home/pi'
IMG_FOLDER = "photo_booth"
UPLOADER_CMD = os.path.join(HOME, "Documents/Projects/Dropbox-Uploader/dropbox_uploader.sh upload")

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)
camera = PiCamera()
camera.resolution = (1024, 768)
camera.image_effect = "none"

def make_timestamp():
	return time.strftime("%a%d%b%Y%H%M%S", time.gmtime())

def make_image_location(name):
	return os.path.join(HOME, IMG_FOLDER, name)

def updload_picture(img_name, img_path):
	upload = UPLOADER_CMD + " " + img_path + " " + img_name
	call([upload], shell=True)

def count_down(duration, intervals):
	while(intervals > 0):
		GPIO.output(LED_PIN, GPIO.HIGH)
		time.sleep(duration)
		GPIO.output(LED_PIN, GPIO.LOW)
		time.sleep(duration)
		intervals -=1

def take_picture():
	img_name = make_timestamp() + '.jpg'
	img_path = make_image_location(img_name)
	camera.capture(img_path)
	updload_picture(img_name, img_path)

while True:
	input_state = GPIO.input(BUTTON_PIN)
	if input_state == False:
		count_down(0.5, 3)
		take_picture()
		#indication that all is done
		count_down(0.2, 3)
	time.sleep(0.3)