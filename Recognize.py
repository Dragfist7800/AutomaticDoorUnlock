import cv2
import numpy as np
import os

import time

import pandas as pd

import yagmail
import os


def sendMail(img):
    sub = "Unknown person requesting access"
    # mail information
    yag = yagmail.SMTP("gatekeeperwastaken@gmail.com", "!@#$%^&*()1234567890Gatekeeper")

    # sent the mail
    yag.send(
        subject=sub,
        to="tkksctwo@gmail.com",  # email subject
        contents="This person is requesting access to R & D cell",  # email body
        attachments=img  # file attached
    )
    print("Email Sent!")

def recognize_face():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("TrainingImageLabel"+os.sep+"Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    df = pd.read_csv("StudentDetails"+os.sep+"StudentDetails.csv")
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name']
    unlock = pd.DataFrame(columns=col_names)
    #iniciate id counter
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height
    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    while True:
        ret = cam.read()
        img = cam.read()
        img = img[1]
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #img = np.array(img)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )
        
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            confidence: object
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
            if k == 27:
                break
            # Check if confidence is less them 100 ==> "0" is perfect match
            if k == 27:
                break
            if (confidence <=40 ):
                nm = df.loc[df['Id'] == id]['Name'].values
                confidence = "  {0}%".format(round(100 - confidence))
                print("Opening Lock")
                exit(0)
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
                cv2.imwrite("Impostor.jpg",img)
                start_time = time.time()
                seconds = 10
                while True:
                    current_time = time.time()
                    elapsed_time = current_time - start_time

                    if elapsed_time > seconds:
                        sendMail("Impostor.jpg");
                        exit(0)
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
        cv2.imshow('unlock',img)
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()


