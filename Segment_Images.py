from ij import IJ, WindowManager
from ij.io import OpenDialog
from ij.process import ImageConverter
from javax.swing import JFrame, JLabel, JButton, JPanel, JComboBox, BoxLayout
from java.awt import BorderLayout, GridLayout, FlowLayout
img_paths = []
opened_imgs = []
dropdown = None
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
		print("error processing!");

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
	global dropdown
	len_stack = dropdown.getItemCount();
	for i in range(0, len_stack):
		temp_file = (dropdown.getItemAt(i));
		img = IJ.openImage(temp_file);
		
	return 0;


def process_img(self): 
	global current_file
	current_file = dropdown.getSelectedItem();
	temp_img = IJ.openImage(current_file);
	processed_temp = process(temp_img);
	processed_temp.show();

def create_gui(): 
	global dropdown, current_file
	frame = JFrame('',
            defaultCloseOperation = JFrame.DISPOSE_ON_CLOSE,
            size = (300, 300));

	add_file_button = JButton('add image', actionPerformed=select_file);
	process_all_button = JButton('process all', actionPerformed=process_stack);
	dropdown = JComboBox(img_paths);
	current_file = dropdown.getSelectedItem();
	process_file_button = JButton('Process file from dropbox: ', actionPerformed=process_img);
	
	container_panel = JPanel(GridLayout(2,1));
	top_panel = JPanel(FlowLayout());
	bottom_panel = JPanel(FlowLayout())
	top_panel.add(dropdown);
	bottom_panel.add(process_file_button);
	bottom_panel.add(add_file_button);
	bottom_panel.add(process_all_button);	
	container_panel.add(top_panel);
	container_panel.add(bottom_panel);	
	frame.add(container_panel);
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



