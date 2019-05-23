from ij import IJ, WindowManager
from ij.io import OpenDialog
from ij.process import ImageConverter
from javax.swing import JFrame, JLabel, JButton, JPanel, JComboBox
from java.awt import BorderLayout, GridLayout

img_paths = []
opened_imgs = []
dropdown = None
current_img = None
current_file = None
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
		dropdown.addItem(path);
	else:
		print("file not selected/found")

def add_path_to_dropdown(): 
	dropdown = JComboBox(img_paths);
	grid_panel.add(dropdown, BorderLayout.CENTER);
	frame.add(grid_panel);


def process_stack(self):
	#do nothing
	return 0;


def set_current_img(self): 
	global current_file
	current_file = dropdown.getSelectedItem();
	print(current_file)

def create_gui(): 
	global dropdown, current_file
	frame = JFrame('',
            defaultCloseOperation = JFrame.DISPOSE_ON_CLOSE,
            size = (300, 300));
	grid_panel = JPanel();
	grid_panel.setLayout(BorderLayout());
	center_flowPanel = JPanel();
	center_flowPanel.setLayout(GridLayout());
	button = JButton('get image', actionPerformed=select_file);
	process_all_button = JButton('process all', actionPerformed=process_stack);
	dropdown = JComboBox(img_paths);
	current_file = dropdown.getSelectedItem();
	process_file_button = JButton('Process only: ', actionPerformed=set_current_img);
	grid_panel.add(button, BorderLayout.NORTH);
	center_flowPanel.add(dropdown);
	center_flowPanel.add(process_file_button);
	grid_panel.add(process_all_button, BorderLayout.SOUTH); 
	grid_panel.add(center_flowPanel, BorderLayout.CENTER);   	
	frame.add(grid_panel);
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



