from zipfile import *
import glob, os
print('11111')
zip_archive = ZipFile( 'result.zip',"w",ZIP_DEFLATED)
for infile in glob.glob("123.txt"):
	zip_archive.write(infile)