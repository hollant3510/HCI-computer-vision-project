#Thomas Holland
#CSC 355
#Homework 4
#determines if the user is shaking there head yes or no

import numpy as np
import cv2


#imports the classifiers
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')


video = cv2.VideoCapture(0)

#creates the empty lists for the x and y values for face and history
xFaceHistory = list()
yFaceHistory = list()

xEyeHistory = list()
yEyeHistory = list()

#reads in video a frame at a time until q is pressed to quit
while(True):

    if len(xFaceHistory) > 10:
        xFaceHistory.pop(0)

    if len(xEyeHistory) > 10:
        xEyeHistory.pop(0)

    if len(yFaceHistory) > 10:
        yFaceHistory.pop(0)

    if len(yEyeHistory) > 10:
        yEyeHistory.pop(0)

    #reads in the video frame
    ignore, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detects where the persons face is and eyes. the 8 variables are defined because I would sometimes get undefined errors if they werent there but it wasnt consistent
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    x = 0
    y = 0
    w = 0
    h = 0
    ex = 0
    ey = 0
    ew = 0
    eh = 0

    for (x,y,w,h) in faces:
        cv2.rectangle(gray, (x,y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_classifier.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_gray, (ex,ey), (ex+ew,ey+eh), (0, 255, 255), 2)

    #records the current x and y values
    xFaceHistory.append(x)
    yFaceHistory.append(y)

    xEyeHistory.append(ex)
    yEyeHistory.append(ey)



    #averages the x and y coordinates of the previous 10 frames
    xaverage = sum(xFaceHistory)/len(xFaceHistory)
    yaverage = sum(yFaceHistory)/len(yFaceHistory)

    #compares the current x and y coordinates with the historys average to determine whether there is any change in where there face is
    if xaverage - x > 10:
        print ("no")

    if xaverage - x < -10:
        print ("no")

    if yaverage - y > 10:
        print ("yes")

    if yaverage - y < -10:
        print ("yes")

    #shows the video
    cv2.imshow('frame', frame)

    #press q to quit/end the program
    if cv2.waitKey(1) & 0xff == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        break


