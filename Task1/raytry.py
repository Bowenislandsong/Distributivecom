#from PIL import Image, ImageFilter

from PIL import Image
import glob, os
import ray
ray.init(redis_address="155.41.32.188:6379")
i = 0;
for infile in glob.glob("*.jpg"):
	im = Image.open(infile)
	im.save('Image'+str(i)+'.png')
	i+=1;
