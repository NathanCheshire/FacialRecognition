#imports used for face detection, face drawing, file manipulation, and random color
import face_recognition
import os
import cv2
import random

#directory of images to find faces in
UNKNOWN_FACES_DIR = "group-photos"

#directory to output to
SAVE_FOLDER = "output"

#face box prefs
FRAME_THICKNESS = 3 
FONT_THICKNESS = 2 
SANS_SERIF = cv2.FONT_HERSHEY_SIMPLEX

#tolerance value for fr
TOLERANCE  =0.2

#optimization prefs
GPU_MODEL = "cnn"
CPU_MODEL = "hog" 
CHOSEN_MODEL = CPU_MODEL

#Random color function for frame drawing
def getColor():
    return random.randint(0,200)

#these are irrelavent but here to make the program work
known_faces = []
known_names = []

#Attempt to find known faces in the unknown images
for filename in os.listdir(UNKNOWN_FACES_DIR):

    print('Processing file: ', filename)

    #load the image as we did before
    image = face_recognition.load_image_file(f'{UNKNOWN_FACES_DIR}/{filename}')

    #returns 2d array bounding boxes for the found faces
    locations = face_recognition.face_locations(image, model=CHOSEN_MODEL)

    #get the 128-dimension face encoding for each face found in the image
    encodings = face_recognition.face_encodings(image, locations)

    #RGB -> BGR for cv2 usage
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    numEncodings = len(encodings)
    print("Found " + str(numEncodings), end = '')
    if numEncodings > 1:
        print(" faces")
    else:
        print(" face")

    #draw a box around the unknown faces
    for face_encoding, face_location in zip(encodings, locations):
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE) 
        match = None
        top_left = (face_location[3], face_location[0])
        bottom_right = (face_location[1], face_location[2])
        color = getColor()
        cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)
        top_left = (face_location[3], face_location[2])
        bottom_right = (face_location[1], face_location[2] + 22)

    #save image
    cv2.imwrite(SAVE_FOLDER + "/" + filename, image) 