from ij import IJ, WindowManager
from ij.io import OpenDialog
from ij.process import ImageConverter
from javax.swing import JFrame, JLabel, JButton, JPanel, JComboBox
from java.awt import GridBagLayout, GridBagConstraints
img_paths = []
opened_imgs = []
dropdown = None
current_file = None
shortened_paths = {'': 'file not found'}

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

	container_panel = JPanel(GridBagLayout());	
	c = GridBagConstraints();
	
	dropdown = JComboBox(img_paths);
	c.fill = GridBagConstraints.HORIZONTAL;
	c.gridx = 0;
	c.gridy = 0;
	c.weightx = 0.5;
	c.gridwidth = 3;
	container_panel.add(dropdown, c);

	add_file_button = JButton('<html>add image</html>', actionPerformed=select_file);
	c.fill = GridBagConstraints.HORIZONTAL;
	c.gridx = 3;
	c.gridy = 0;
	c.weightx = 0.5;
	c.gridwidth = 1;
	container_panel.add(add_file_button, c);
	
	process_file_button = JButton('<html>Process file from dropbox: </html>', actionPerformed=process_img);
	c.fill = GridBagConstraints.HORIZONTAL;
	c.gridx = 0;
	c.gridy = 1;
	c.weightx = 0.5;
	c.gridwidth = 2;
	container_panel.add(process_file_button, c);
	
	process_all_button = JButton('<html>process all</html>', actionPerformed=process_stack);
	c.fill = GridBagConstraints.HORIZONTAL;
	c.gridx = 2;
	c.gridy = 1;
	c.weightx = 0.5;
	c.gridwidth = 2;
	container_panel.add(process_all_button, c);
	current_file = dropdown.getSelectedItem();
	
	frame.add(container_panel);
	frame.visible = True;


create_gui()


