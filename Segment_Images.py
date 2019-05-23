from ij import IJ, WindowManager
from ij.io import OpenDialog
from ij.process import ImageConverter
from javax.swing import JButton, JFrame, JLabel

img_paths = []
opened_imgs = []
def process(imp): 
	try:
		IJ.run(imp, "Subtract Background...", "rolling=50");
		IJ.run(imp, "Subtract Background...", "rolling=50");
		ImageConverter.setDoScaling(True);
		IJ.run(imp, "32-bit", "");
		IJ.run(imp, "Smooth", "");
		IJ.setAutoThreshold(imp, "Default dark");
		IJ.run(imp, "NaN Background", "");
		return imp;
	except(AttributeError):
		print("Image not found!");

def select_file(self):
	global img_paths, opened_imgs 
	path = OpenDialog('Select an image file').getPath();
	if(path): 
		img_paths.append(path);
		opened_imgs.append(IJ.openImage(path));
		opened_imgs[-1].show();
		
	else:
		print("file not selected/found")


def create_gui(): 
	frame = JFrame('',
            defaultCloseOperation = JFrame.DISPOSE_ON_CLOSE,
            size = (300, 300));
    
	button = JButton('get image', actionPerformed=select_file);
	label1 = JLabel();    	
	frame.add(button);
	frame.visible = True;



#img1_path = OpenDialog('Select an image file').getPath();
#img1 = IJ.openImage('/Users/willpeterson/Desktop/Huiwang-Lab/processing/0.tif');
#img2_path = OpenDialog('Select an image file').getPath();
#img2 = IJ.openImage('/Users/willpeterson/Desktop/Huiwang-Lab/processing/2.tif');
#img1.show();
#img2.show();
#print(IJ.getImage());
create_gui()

#process(img1);
#process(img2);



