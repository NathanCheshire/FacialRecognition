# FacialRecognition

## General Statistics
University: Mississippi State <br/>
Major: Software Engineering<br/>
Class: CSE4633 Artificial Intelligence<br/>
Term: Fall 2020<br/>
Teacher: Dr. Eric Hansen<br/>
Description brief: Final project on python facial recognition<br/>

## Usage

TODO

## Files Tree and descriptions

```bash
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
