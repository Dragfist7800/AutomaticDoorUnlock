import os  # accessing the os functions
import Capture_Image
import Train_Image
import Recognize
import eel


# --------------------------------------------------------------
# calling the take image function form capture image.py file

@eel.expose
def CaptureFaces(regId, regName):
    temp_Id = regId  # gets the Id from the webpage form and assigns to this var
    temp_Name = regName  # gets the Name from the webpage form and assigns to this var
    Capture_Image.takeImages(temp_Id, temp_Name)  # Call the takeImage function for registering data
    print("Data acquired!!!!!!!!!!!!!")
    Train_Image.TrainImages()  # Call the Trainimage function to train our model
    print("Model Trained!!!!!!!!!!!!!")


# -----------------------------------------------------------------
# calling the train images from train_images.py file
@eel.expose
def Trainimages():
    Train_Image.TrainImages()


# --------------------------------------------------------------------
# calling the recognize_attendance from recognize.py file
@eel.expose
def RecognizeFaces():
    Recognize.recognize_face()
    # Call the recognize_face function to recognize the person in front of the camera and
    # unlock if the person is registered in the database


eel.init("Design")  # Where all our Html, CSS, JS files are saved
eel.start("main.html")  # Our main Html file which is the homepage
