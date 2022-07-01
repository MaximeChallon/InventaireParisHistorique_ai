import os
import csv
import pandas as pd
from PIL import Image


# liste des images annotées
for image in os.listdir("darknet/data/images/"):
	#print(image)
	pass

df = pd.read_csv("Test_PH-export.csv")
#print(df)
for index, row in df.iterrows():
	x_min = row['xmin']
	x_max = row['xmax']
	y_min = row['ymin']
	y_max = row['ymax']
	
	im = Image.open("darknet/data/images/" + row['image'])
	width, height = im.size
	print(row)
	
	x_center = float((x_min + x_max)) / 2 / width
	y_center = float((y_min + y_max)) / 2 / height
	w = float((x_max - x_min)) / height
	h = float((y_max - y_min)) / width
	class_index = 0
	with open ("darknet/data/labels/"+ row['image'].replace('jpg', 'txt'), "a") as f:
		f_e = csv.writer(f, delimiter=' ',quoting=csv.QUOTE_MINIMAL)
		f_e.writerow([class_index, x_center, y_center, w, h])
