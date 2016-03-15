import picamera
import io
from PIL import Image
from time import sleep

class Camera():
	def __init__(self, img_width, img_height, img_rot=0):
		self.camera = picamera.PiCamera()
		self.value = None
		self.camera.resolution = (img_width,img_height)
		self.img_width = img_width
		self.img_height = img_height
		self.img_rot = img_rot
		self.stream = io.BytesIO()

	
	def get_value(self):
		return self.value

	def update(self): 		#Call to a function to update the 
		return(self.sensor_get_value()) #current picture, aka take a new one
		

	def reset(self):
		self.value = None

	def sensor_get_value(self):
		with self.camera:
			self.camera.start_preview
			#sleep(2)
			self.camera.brightness = 15
			self.camera.contrast = 100
			self.camera.hflip = True
			self.camera.capture(self.stream,format='jpeg')
			print("Captured a image")
		self.stream.seek(0)
		self.image=Image.open(self.stream)
		self.image.save("image.jpeg",format = 'jpeg')
		return (self.image)

	def close(self):
		self.stream.close()

	def preview(self):
		self.camera.start_preview()
		sleep(5)
		self.camera.stop_preview()

#Empty
