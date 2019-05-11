from ij import IJ
from ij.process import ImageConverter
from ij.io import DirectoryChooser


#DirectoryChooser.setDefaultDirectory("/Users/willpeterson/Desktop/Huiwang-Lab")
'''print(IJ.getDirectory("current"))
imp = IJ.openImage("0.tif")
print(imp)
'''

#dir = (IJ.getDirectory("Input_directory")) use this for selecting directory
dir="/Users/willpeterson/Desktop/"
dir = dir + "Huiwang-Lab/"
img1 = IJ.openImage(dir+"0.tif")
img2 = IJ.openImage(dir+"2.tif")

def process(imp): 
	IJ.run(imp, "Subtract Background...", "rolling=50");
	IJ.run(imp, "Subtract Background...", "rolling=50");
	ImageConverter.setDoScaling(True);
	IJ.run(imp, "32-bit", "");
	IJ.run(imp, "Smooth", "");
	IJ.setAutoThreshold(imp, "Default dark");
	IJ.run(imp, "NaN Background", "");
	return imp

def stack(img1, img2): 
	#IJ.run(imp, "MultiStackReg", "stack_1=2.tif action_1=[Use as Reference] file_1=[] stack_2=0.tif action_2=[Align to First Stack] file_2=[] transformation=[Rigid Body]");
	return 0


img1 = process(img1)
img1.show()

