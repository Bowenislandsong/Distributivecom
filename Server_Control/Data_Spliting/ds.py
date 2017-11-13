# image splitting sample editted by Zhiyi Yang

import glob, os
from zipfile import *

file_name0 = ".zip"
with ZipFile(file_name0, 'r') as zip:
	zip.extractall();

file_name1="data_set_1.zip"
file_name2="data_set_2.zip"

zip_archive1 = ZipFile( file_name1,"w",ZIP_DEFLATED)
zip_archive2 = ZipFile( file_name2,"w",ZIP_DEFLATED)

for infile in glob.glob("raytry.py"):
	zip_archive1.write(infile)
	zip_archive2.write(infile)

for infile in glob.glob("1.jpg"):
	zip_archive1.write(infile)
for infile in glob.glob("2.jpg"):
	zip_archive2.write(infile)


zip_archive1.close()
zip_archive2.close()


