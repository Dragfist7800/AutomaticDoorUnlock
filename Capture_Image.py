import csv
# import sys
import cv2
import os


# counting the numbers


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# Take image function

def takeImages(regId, regName):
    print("taking data......")
    Id = regId  # input("Enter Your Id: ")
    name = regName  # input("Enter Your Name: ")
    print("Got the data!!")
    print("taking Image......")

    if (name.isalpha()):
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(30, 30),
                # flags=cv2.CV_HAAR_SCALE_IMAGE
            )
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (10, 159, 255), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage" + os.sep + name + "." + Id + '.' +
                            str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('frame', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is more than 100
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
    else:
        if (is_number(Id)):
            print("Enter Alphabetical Name")
        if (name.isalpha()):
            print("Enter Numeric ID")


'''if __name__ == '__main__':
    globals()[sys.argv[1]]()'''
