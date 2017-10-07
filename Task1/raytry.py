#from PIL import Image, ImageFilter

from PIL import Image
import glob, os

i = 0;
for infile in glob.glob("*.jpg"):
	im = Image.open(infile)
	im.save('Image'+str(i)+'.png')
	i+=1;
