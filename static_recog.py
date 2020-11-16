#imports for the project include:
#   -the main facial recognition one
#   -os for directory interaction
#   -open cv2 for image and raster manipulation


#documentation: https://face-recognition.readthedocs.io/en/latest/face_recognition.html
import face_recognition
import os
import cv2
import random

#constants no interaction with program is needed outside of these lines ---------------------------
KNOWN_FACES_DIR = "lfw-now" #this is a folder full of folders full of images of one person we know 

#example:
#   data-set/
#   --------nathan cheshire
#   ------------nate1.jpg
#   ------------nate_at_water_park.png
#   --------mark keenum
#   ------------fall_convocation_2015.png

#where are the images we want to attempt to identify faces in relative to this file
UNKNOWN_FACES_DIR = "unknown" 
SHOW_UNKNOWN_FACES = False #draw boxes around found but not identified faces
SAVE_FOLDER = "output" #save the output images to this directory
TOLERANCE = 0.5
UNKNOWN_NAME = 'face_found' #name given to faces found that we could not identify 

FRAME_THICKNESS = 3 #box around found faces thickness
FONT_THICKNESS = 2 #font size for name of found faces
SANS_SERIF = cv2.FONT_HERSHEY_SIMPLEX

GPU_MODEL = "cnn" #use for gpus
CPU_MODEL = "hog" #use for cpus
CHOSEN_MODEL = CPU_MODEL #change this depending on if you have a good GPU

LOOP_TOLERANCE = False
#Run program on the following tollerances and output to a separate directory
TOLERANCE_LIST = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

#--------------------------------------------------------------------------------------------------

def getColor(name):
    return random.randint(0,200)


print('Loading known faces')
known_faces = []
known_names = []

#Oranize known faces as subfolders from our master directory of known faces (dataset)

#The subfolder of our dataset folder is the name of the person, remember these images should 
# only contain the subject for which we have assigned the name to
for name in os.listdir(KNOWN_FACES_DIR):
    print("Loading faces for: " + str(name))
    #loop through all the individual files
    for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
        try:
            print("\tAttempting to find face in: " + str(filename))
            
            #load an rgb image, returns an image as a numpy array
            image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')

            #get the person's face that we are concerend with
            #we make the assumption again that the subject is the only face in
            #the photo so we can grab the first face we find
            encoding = face_recognition.face_encodings(image)[0]

            #add the encoding and name to their approriate arrays
            known_faces.append(encoding)
            known_names.append(name)
        except:
            print("Couldn't find a face in " + filename + " so skipped it.")
            continue

#faces have been loaded and now we may walk through our awaiting unknown images
print('Processing unknown faces from folder: ', UNKNOWN_FACES_DIR)

if LOOP_TOLERANCE:
    for SUB_TOL in TOLERANCE_LIST:
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

            #loop through tuple pairs created using zip of (encoding, face_locations)
            for face_encoding, face_location in zip(encodings, locations):

                #return a list of T/F values that indicate which face_encodings match the face encodings to check
                results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)

                #check for found faces and get index if so
                match = None
                if True in results:  
                    #get the name of the match
                    match = known_names[results.index(True)]
                    print("\t - " + str(match))

                    #get corners so we can draw an outline around the face
                    top_left = (face_location[3], face_location[0])
                    bottom_right = (face_location[1], face_location[2])

                    #smart way to choose a color for the box
                    color = getColor(match)

                    # draw the frame
                    cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                    #draw filled rect to put the name in
                    top_left = (face_location[3], face_location[2])
                    bottom_right = (face_location[1], face_location[2] + 22)
                    cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                    cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), SANS_SERIF, 0.5, (200, 200, 200), FONT_THICKNESS)

                #box found faces that could not be identified if true, same code as above so will not comment
                elif SHOW_UNKNOWN_FACES:
                    match = known_names[results.index(False)]
                    print("\t - " + str(match))
                    top_left = (face_location[3], face_location[0])
                    bottom_right = (face_location[1], face_location[2])
                    color = getColor(UNKNOWN_NAME)
                    cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)
                    top_left = (face_location[3], face_location[2])
                    bottom_right = (face_location[1], face_location[2] + 22)
                    cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                    cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), SANS_SERIF, 0.5, (200, 200, 200), FONT_THICKNESS)

            #save image to download location
            cv2.imwrite(SAVE_FOLDER + "/" + str(TOLERANCE) + "/" + filename, image) 

else:

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

        #loop through tuple pairs created using zip of (encoding, face_locations)
        for face_encoding, face_location in zip(encodings, locations):

            #return a list of T/F values that indicate which face_encodings match the face encodings to check
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)

            #check for found faces and get index if so
            match = None
            if True in results:  
                #get the name of the match
                match = known_names[results.index(True)]
                print("\t - " + str(match))

                #get corners so we can draw an outline around the face
                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])

                #smart way to choose a color for the box
                color = getColor(match)

                # draw the frame
                cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                #draw filled rect to put the name in
                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2] + 22)
                cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), SANS_SERIF, 0.5, (200, 200, 200), FONT_THICKNESS)

            #box found faces that could not be identified if true, same code as above so will not comment
            elif SHOW_UNKNOWN_FACES:
                match = known_names[results.index(False)]
                print("\t - " + str(match))
                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])
                color = getColor(UNKNOWN_NAME)
                cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)
                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2] + 22)
                cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), SANS_SERIF, 0.5, (200, 200, 200), FONT_THICKNESS)

        #save image to download location
        cv2.imwrite(SAVE_FOLDER + "/" + filename, image) 