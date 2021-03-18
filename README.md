# FacialRecognition

## General Statistics
University: Mississippi State <br/>
Major: Software Engineering<br/>
Class: CSE4633 Artificial Intelligence<br/>
Term: Fall 2020<br/>
Teacher: Dr. Eric Hansen<br/>
Description brief: Final project on python facial recognition<br/>

## Usage

You should have python installed on your machine (obviously) so that you can execute the python scripts. Whether that is through the command line, IDLE, PyCharm, or any other IDE that can interpret and execute python code is irrelavent. Within the static_recog.py script, there are variables with descriptions that you will need to change. For example, you will need to compile your own data set for training and setup the file structure as is necessary for the algorithm to mark each person correctly. TL;DR, the static_recog.py file explains everything.

The same logic applies for the face_counter.py script although less edits and data is required.

## Variables to change within static_recog.py

```
KNOWN_FACES_DIR = "" this is the mater directory for your training data. Here you will create sub-folders with the names of known people to train on, the name of the individual pictures is irrelavent.

#example:
#   data-set/
#   --------nathan cheshire
#   ------------nate1.jpg
#   ------------nate_at_water_park.png
#   --------mark keenum
#   ------------fall_convocation_2015.png

UNKNOWN_FACES_DIR = "unknown" is where the image directory we want to attempt to identify faces in relative to this script file are located
SHOW_UNKNOWN_FACES = False will not draw boxes around found yet not identified faces
SAVE_FOLDER = "output" is where to save the edited images (boxes are placed around faces and labeled)
TOLERANCE = 0.5 is the tolerance value for how closely one face matches another
UNKNOWN_NAME = 'face_found' whatever you want to name unknown faces if you have SHOW_UNKNOWN_FACES set to True

FRAME_THICKNESS = 3 box around found faces thickness
FONT_THICKNESS = 2 font size for name of found faces
SANS_SERIF = cv2.FONT_HERSHEY_SIMPLEX font for the name labels

GPU_MODEL = "cnn" use this for powerful GPU
CPU_MODEL = "hog" use this if you do not have a powerful GPU
CHOSEN_MODEL = CPU_MODEL 

LOOP_TOLERANCE = False set this to True if you want to loop through all the values in TOLERANCE_LIST for all your data the needs classification. A new folder will be created for each tolerance of course.
TOLERANCE_LIST = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] you can change this to any number you like in the range [0,1]
```

## Files Tree and descriptions

```
FacialRecognition
├──Report                              
|  ├──data.xlsx                       //excel sheet of data from tolerances
|  ├──nvc29_Final_Project_Report.docx //the final report document, a good read
|  ├──trumpandbiden.jpf               //a picture I used in my report from one of the 2020 presidential debates
├──lfw-now                            //directory where your training data goes
|  ├──Biden                           
|  ├──Chris Evans
|  ├──Chris Hemsworth
|  ├──Mark Ruffalo
|  ├──Nathan Cheshire
|  ├──Robert Downy Jr
|  ├──Vincent Cheshire
|  ├──Trump
├──output                             //images from a directory titled "unknown" are searched for known faces. If any are found, they are highlighted and placed in this directory
|  ├──3.png
|  ├──IMG_1204.JPG
|  ├──Philmont.jpg
|  ├──Shaffers peak.jpg
|  ├──avangers.jpg
├──LICENSE
├──MAE.py                             //mean absolute error calculator
├──MAE_RAW.txt
├──face_counter.py                    //count the number of faces in an impage
├──facial_detection_data.log
├──nathan_dad_avengers_0.5_tol.zip    //me, my father, and four avengers facially recog'd at a tolerance of 0.5
├──nathan_dad_avengers_0.6_tol.zip
├──static_recog.py                    //the main code base for the project where you input your data
```
