from camera1 import Camera
from threading import Thread
from imager2 import Imager
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
output = 21
GPIO.setup(output, GPIO.OUT)
GPIO.output(output, False)


class RedDetector(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.camera = Camera(400,250)
		self.value = False
		print("test")
		self.run()
	

		
	def is_red(self, image):
		red_pixels = 0
		image.convert('RGB')
		pix = image.load()
		for x in range(400):
			for y in range(250):
				pixel = pix[x,y]
				#pixel = image.getpixel((x,y))
				if ((pixel[0] >= 100) and (pixel[1] >= 100) and (pixel[2] >= 100)):
					red_pixels += 1
					pix[x,y] = (0,255,0)
					#print("one red pixel added")
			percentage = red_pixels/128/96
			if percentage >= 0.05:
				self.value = True
			else:
				self.value = False
		#print(red_pixels)
		image.save("Change_color.jpeg")	
		return red_pixels

	def run(self):
		#print("trying to capture")
		self.image = self.camera.update()
            #image = Imager("image.png",self.camera.get_value())
		pixel = self.is_red(self.image)
		if (pixel > 30):
			GPIO.output(output, False)
		else:
			GPIO.output(output, True)
		#self.camera.close()

	def get_value(self):
		return self.value

	def update(self):
		pass
