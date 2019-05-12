
from ij import IJ
from ij.process import ImageConverter
from ij.io import DirectoryChooser
#from ijopencv.ij      import ImagePlusMatConverter

#DirectoryChooser.setDefaultDirectory("/Users/willpeterson/Desktop/Huiwang-Lab")
'''print(IJ.getDirectory("current"))
imp = IJ.openImage("0.tif")
print(imp)
'''

#dir = (IJ.getDirectory("Input_directory")) use this for selecting directory
dir="/Users/willpeterson/Desktop/"
dir = dir + "Huiwang-Lab/"
img1_path = "0.tif"
img2_path = "2.tif"
img1 = IJ.openImage(dir+img1_path)
img2 = IJ.openImage(dir+img2_path)

def process(imp): 
	try:
		IJ.run(imp, "Subtract Background...", "rolling=50");
		IJ.run(imp, "Subtract Background...", "rolling=50");
		ImageConverter.setDoScaling(True);
		IJ.run(imp, "32-bit", "");
		IJ.run(imp, "Smooth", "");
		IJ.setAutoThreshold(imp, "Default dark");
		IJ.run(imp, "NaN Background", "");
		return imp
	except(AttributeError):
		print("Image not found!")

def stack(img1_path, img2_path):
	imp = IJ.createImage("A Random Image", "8-bit", 512, 512, 0) 
	'''IJ.run(img2,"MultiStackReg", "stack_1=["+img2_path+"]"
	+" action_1=[Use as Reference] file_1=["+img2_path+"]"+
	" stack_2=["+img1_path+"]"
	" action_2=[Align to First Stack]"+
	" file_2=["+img1_path+"] transformation=[Rigid Body]");
	'''
	IJ.run(img1,"MultiStackReg", 
	"stack_1=["+img2_path+"]"
	+ " action_1=[Use as Reference]"
	+ " file_1=["+img2_path+"]"
	+ " stack_2=["+img1_path+"]"
	+ " action_2=[Align to First Stack]"
	+ " file_2=["+img1_path+"]"
	+ " transformation=[Rigid Body]");



stack(img1_path, img2_path)
#img1 = process(img1)
#img2 = process(img2)
#img1.show()
#img2.show()








#stacked_img = stack(img1_path, img2_path)


