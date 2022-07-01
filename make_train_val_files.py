import os
import csv

images = os.listdir("darknet/data/images/")

nombre_images = len(images)

i = 1
for image in images:
	if i < (nombre_images - 5):
		with open("darknet/data/train.txt", 'a') as f:
			f_e = csv.writer(f, delimiter = ',')
			f_e.writerow(["/content/darknet/data/images/" + image])
		i += 1
	else:
		with open("darknet/data/val.txt", 'a') as f:
			f_e = csv.writer(f, delimiter = ',')
			f_e.writerow(["/content/darknet/data/images/" + image])
		i += 1
	
