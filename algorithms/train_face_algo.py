# we already have our data of faces, so it will use that data to train
import os
import cv2
from PIL import Image
import numpy as np
from tkinter import messagebox


def train_function():
    data_dir = r"C:\Users\samki\PycharmProjects\pythonProject1\Attendance System\face_data"
    path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

    faces = []
    ids = []

    for image in path:
        img = Image.open(image).convert('L')  # converted to gray scale image
        image_np = np.array(img, 'uint8')
        id1 = int(os.path.split(image)[1].split('.')[1])

        faces.append(image_np)
        ids.append(id1)
        cv2.imshow("Training...", image_np)
        cv2.waitKey(1) == 13
    ids = np.array(ids)

    # ------------------training the classifier------------------

    classifier = cv2.face.LBPHFaceRecognizer_create()  # LBPHFaceRecognizer_create() !!!!!!!!! DANGER!!!!!!
    classifier.train(faces, ids)
    classifier.write("Classifier.xml")
    cv2.destroyAllWindows()

    messagebox.showinfo("Result", "Training data set completed!")
