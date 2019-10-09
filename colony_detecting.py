
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pickle


#need to correct directory below: !!!!!!!!!!!!!	
dir="/Users/willpeterson/Desktop/Huiwang-Lab/Detection/"
# temp_file = dir+'Good_51_8Ratio.png'
temp_file = dir+'60_Good.png'
img = cv2.imread(temp_file,0)


img_copy = img

#simple blob detections works best when image is negative:
img_neg = abs(255-img)

params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 10  
params.filterByCircularity = True
params.minCircularity = 0.6

detector = cv2.SimpleBlobDetector_create() 
keypoints = detector.detect(img_neg)
img_points = cv2.drawKeypoints(img_copy, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

np_keypoints = np.array([(k.pt) for k in keypoints], dtype=[('x', np.intc,), ('y', np.intc)])
keypoint_radii = np.array([k.angle for k in keypoints])

cropped_particles = []
x_keypoints = np.array(np_keypoints['x'])
y_keypoints = np.array(np_keypoints['y'])
new_img = np.zeros(shape=(len(img),len(img[0])))

for r in range(0, len(x_keypoints)):
	curr_rad = 10#np.int(np.floor(r+keypoint_radii[r]))
	# print(keypoint_radii[r])
	# print([x_keypoints[r],x_keypoints[r]+curr_rad,y_keypoints[r],y_keypoints[r]+curr_rad-2])
	try: 
		# print(img[x_keypoints[r]:x_keypoints[r]+curr_rad,y_keypoints[r]:y_keypoints[r]+curr_rad-2])
		new_img[x_keypoints[r]:x_keypoints[r]+curr_rad,y_keypoints[r]:y_keypoints[r]+curr_rad] = img[x_keypoints[r]:x_keypoints[r]+curr_rad,y_keypoints[r]:y_keypoints[r]+curr_rad]
	except: 
		continue


circled_petri = cv2.imread(dir+'60_MMStack.ome.tif',0)
petri_61 = cv2.imread(dir+'61_MMStack.ome.tif',0) 
plt.figure(1)
plt.imshow((circled_petri-petri_61)+new_img)
plt.show()

