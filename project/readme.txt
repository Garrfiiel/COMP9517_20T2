COMP9517 Group Project readme

#########################
Group Name: 9517_group
Project name: Cell detection and tracking
#########################


Summary: 
The program could read the images from different datasets, and preprocess the images sequentially and respectively to detect and track inner cell motion and mitosis.

Requirements:
All three files must be included.
--main.ipynb              
--IO_IMAGE.py           for reading and writing.
--preprocessing.py     including different preprocessing progress on different datasets

Configuration: 
Python 3.7.4
scikit-image 0.15.0
opencv 3.4.1
scipy 1.3.1
jupyter notebook 6.0.1

Usage:
! ! ! ! ! !  Don't choose the dataset1 if you don't have corresponding segemented results (which come from other CNN model's results -- markers)  There is a example of dataset 1 sequence1 in the folder. If wanna see the results ,replce the original folder and do the following.

1. change the path in main.ipynb to the directory where the datasets are
2. change the DATASET and SEQ to the wanted tested (interger) dataset and sequence
3. run through all the parts above the boundary, the results will be saved in two folders, respectively the imgs with bbox and the images with trajectories.
----
functional:
UI:  run the UI part if wanna see the detailed information for task3, click the cell center and then the information will be printed on the window

show pic: choose various i to show the images ( raw , processed , fianl result )