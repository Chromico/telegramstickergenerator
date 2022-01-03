import re
import os, sys
from PIL import Image



	


#step 1 get a list of all files in the current directory:
file_list = os.scandir('./')
for this_filehandler in file_list:
	#clause 1: Must be png
	if (re.fullmatch(r'.+\.png$', this_filehandler.path)):
		#clause 2: Must contain "step02"
		if (re.fullmatch(r'.+step\s?0?2.+', this_filehandler.path)):			
			print(this_filehandler.path)
			#process: Find limits of the image…
			im = Image.open(this_filehandler.path)
			most_north_opacity_pixel = im.size[1]
			most_south_opacity_pixel = 0
			most_east_opacity_pixel = 0
			most_west_opacity_pixel = im.size[0]
			for px in range(0,im.size[0]):
				for py in range(0,im.size[1]):
					if (im.getpixel((px,py))[3] > 50):
						if (px < most_west_opacity_pixel):
							most_west_opacity_pixel = px						
						if (px > most_east_opacity_pixel):
							most_east_opacity_pixel = px					
						if (py > most_south_opacity_pixel):
							most_south_opacity_pixel = py				
						if (py < most_north_opacity_pixel):
							most_north_opacity_pixel = py
			#process: Crop the image along this lines
			crop_box = (most_west_opacity_pixel,most_north_opacity_pixel,most_east_opacity_pixel,most_south_opacity_pixel)
			cropped_image = im.crop(crop_box)
			new_filename = re.sub(r'step\s?0?2[^\.]*\.png','step03 cropped.png',this_filehandler.path)
			if (new_filename != this_filehandler.path):
				cropped_image.save(new_filename)
			#resize to 512 pixels
			if (cropped_image.size[0] > cropped_image.size[1]):
				size_factor = cropped_image.size[0] / 512.0
			else:
				size_factor = cropped_image.size[1] / 512.0
			resized_image = cropped_image.resize((int(cropped_image.size[0]/size_factor),int(cropped_image.size[1]/size_factor)))
			new_filename = re.sub(r'step\s?0?2[^\.]*\.png','step04 resized.png',this_filehandler.path)
			if (new_filename != this_filehandler.path):
				resized_image.save(new_filename)
			#generate a white shadowcopy
			white_shadow = Image.new('RGBA',(resized_image.size[0]+14,resized_image.size[1]+14),(0,0,0,0))
			black_shadow = Image.new('RGBA',(resized_image.size[0]+14,resized_image.size[1]+14),(222,222,222,0))
			for px in range(0,resized_image.size[0]):
				for py in range(0,resized_image.size[1]):
					if (resized_image.getpixel((px,py))[3] > 80):
						white_shadow.putpixel((px+12,py+12),(255,255,255,255))
			for px in range(0,white_shadow.size[0]):
				for py in range(0,white_shadow.size[1]):
					if (white_shadow.getpixel((px,py)) == (255,255,255,255)):
						px2 = px-5
						py2 = py-5
						black_shadow.putpixel((px2,py2),(0,0,0,153))
						for x_shift in range(-7,+7):
							for y_shift in range(-7,+7):
								if (px2+x_shift > 0 and px2+x_shift < white_shadow.size[0] and py2+y_shift > 0 and py2+y_shift < white_shadow.size[1]):
									this_opacity = int(255-10*abs(x_shift * y_shift))
									if (this_opacity > 80):
										if (white_shadow.getpixel((px2+x_shift,py2+y_shift))[3] < this_opacity):
											white_shadow.putpixel((px2+x_shift,py2+y_shift),(255,254,255,this_opacity))
										if (black_shadow.getpixel((px2+x_shift,py2+y_shift))[3] < this_opacity*0.6):
											black_shadow.putpixel((px2+x_shift,py2+y_shift),(0,0,0,int(this_opacity*0.6)))
			new_filename = re.sub(r'step\s?0?2[^\.]*\.png','step05 white shadowcopy.png',this_filehandler.path)
			if (new_filename != this_filehandler.path):
				white_shadow.save(new_filename)
			new_filename = re.sub(r'step\s?0?2[^\.]*\.png','step06 black shadowcopy.png',this_filehandler.path)
			if (new_filename != this_filehandler.path):
				black_shadow.save(new_filename)
			combined_image = Image.new('RGBA',(white_shadow.size[0]+28,white_shadow.size[1]+28),(0,0,0,0))
			combined_image.alpha_composite(black_shadow,(10,5))
			combined_image.alpha_composite(white_shadow,(0,14))
			combined_image.alpha_composite(resized_image,(8,20))
			new_filename = re.sub(r'step\s?0?2[^\.]*\.png','step07 combine4-6.png',this_filehandler.path)
			if (new_filename != this_filehandler.path):
				combined_image.save(new_filename)
			#resize to 512 pixels
			if (combined_image.size[0] > combined_image.size[1]):
				size_factor = combined_image.size[0] / 512.0
			else:
				size_factor = combined_image.size[1] / 512.0
			resized_image2 = combined_image.resize((int(combined_image.size[0]/size_factor),int(combined_image.size[1]/size_factor)))
			new_filename = re.sub(r'step\s?0?2[^\.]*\.png','step08 final.png',this_filehandler.path)
			if (new_filename != this_filehandler.path):
				resized_image2.save(new_filename)


