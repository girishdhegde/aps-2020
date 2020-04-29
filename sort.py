import re
import os
import pickle
import shutil
def sort_dir(data):
	convert=lambda text:int(text) if text.isdigit() else text.lower()
	ak=lambda key:[convert(c) for c in re.split('([0-9]+)',key)]
	return sorted(data,key=ak)

#x=(sort_dir(os.listdir("d:/frames2")))

def writefile():
	dest = 'c:/users/girishhegde/iitdimg'
	file = open(dest+'/classified.pkl','rb')
	x=pickle.load(file)
	file.close()

	dest = 'd:/classified.pkl'
	file = open(dest,'rb')
	y=pickle.load(file)
	file.close()
	print(x)
	print(y)
#shutil.copy("c:/users/girishhegde/iitdimg/3d.mp4",'c:/users/girishhegde/iitdimg/frames')
writefile()