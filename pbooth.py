import time
import os
import RPi.GPIO as GPIO
from subprocess import call
from picamera import PiCamera

BUTTON_PIN = 18
home = os.environ['HOME']
IMG_FOLDER = "photo_booth"
UPLOADER_CMD = "/home/pi/Documents/Projects/Dropbox-Uploader/dropbox_uploader.sh upload"

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
camera = PiCamera()
camera.resolution = (1024, 768)

def make_timestamp():
	return time.strftime("%a%d%b%Y%H%M%S", time.gmtime())

def make_image_location(name):
	return os.path.join(home, IMG_FOLDER, name);

def updload_picture(img_name, img_path):
	upload = UPLOADER_CMD + " " + img_path + " " + img_name
	call([upload], shell=True)

def take_picture():
	img_name = make_timestamp() + '.jpg';
	img_path = make_image_location(img_name);
	camera.capture(img_path);
	updload_picture(img_name, img_path)

while True:
	input_state = GPIO.input(BUTTON_PIN)
	if input_state == False:
		print ("Taking picture!!")
		take_picture()
		print ("Done!!")