import sys
from tkinter import *
from PIL import Image, ImageTk
from student import Student
import os
from train import Trainer
from face_recognition import FaceRecognizer
from attendance import Attendance

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root  # this is our screen or window
        self.root.geometry("1500x790+0+0")  # setting the width and height for the screen so that it fits the entire laptop screen
        self.root.title("Face Recognition System")

        # background image 1
        img1 = Image.open(r"Images for Face detection\bg1.1.png")
        img1 = img1.resize((500, 130))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        #  image has been created as an object, now create a label to represent that image
        label1 = Label(self.root, image=self.photoimage1)
        label1.place(x=0, y=0, width=500, height=130)

        # background image 2
        img2 = Image.open(r"Images for Face detection\bg1.2.png")
        img2 = img2.resize((500, 130))
        self.photoimage2 = ImageTk.PhotoImage(img2)
        # image has been created as an object, now create a label to represent that image
        label2 = Label(self.root, image=self.photoimage2)
        label2.place(x=500, y=0, width=500, height=130)

        # background image 3
        img3 = Image.open(r"Images for Face detection\bg1.3.png")
        img3 = img3.resize((500, 130))
        self.photoimage3 = ImageTk.PhotoImage(img3)
        # image has been created as an object, now create a label to represent that image
        label3 = Label(self.root, image=self.photoimage3)
        label3.place(x=1000, y=0, width=500, height=130)

        # main background where all the button will be
        main_bg = Label(self.root, bg="#346d8b", borderwidth=1)
        main_bg.place(x=0, y=130, width=1500, height=660)

        # Main title
        title_label = Label(main_bg, text="SNAPTRACK ATTENDANCE", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_label.place(x=0, y=0, width=1500, height=45)  # x and y are 0 because now we're considering with respect to only the image, not the entire window

        # Now we create buttons------------------------------------------------

        # button 1: Student Button (Image+Button)
        bimg1 = Image.open(r"Images for Face detection\1.png")
        bimg1 = bimg1.resize((220, 220))
        self.btnimage1 = ImageTk.PhotoImage(bimg1)
        # image created... now create a button with that image
        btn1 = Button(main_bg, image=self.btnimage1, command=self.student_details, cursor="hand2", borderwidth=0)
        btn1.place(x=200, y=80, width=220, height=220)
        # text button
        btn11 = Button(main_bg, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="#324a5c", fg="white")
        btn11.place(x=200, y=300, width=220, height=40)

        # button 2: Detect Face (Image+Button)
        bimg2 = Image.open(r"Images for Face detection\2.png")
        bimg2 = bimg2.resize((220, 220))
        self.btnimage2 = ImageTk.PhotoImage(bimg2)
        # image created... now create a button with that image
        btn2 = Button(main_bg, image=self.btnimage2, command=self.face_recognizer, cursor="hand2", borderwidth=0)
        btn2.place(x=500, y=80, width=220, height=220)
        # text button
        btn22 = Button(main_bg, text="Detect Face", command=self.face_recognizer, cursor="hand2", font=("times new roman", 15, "bold"),
                       bg="#324a5c", fg="white")
        btn22.place(x=500, y=300, width=220, height=40)

        # button 3: Attendance (Image+Button)
        bimg3 = Image.open(r"Images for Face detection\3.png")
        bimg3 = bimg3.resize((220, 220))
        self.btnimage3 = ImageTk.PhotoImage(bimg3)
        # image created... now create a button with that image
        btn3 = Button(main_bg, image=self.btnimage3, command=self.attendance, cursor="hand2", borderwidth=0)
        btn3.place(x=800, y=80, width=220, height=220)
        # text button
        btn33 = Button(main_bg, text="Attendance", command=self.attendance, cursor="hand2", font=("times new roman", 15, "bold"),
                       bg="#324a5c", fg="white")
        btn33.place(x=800, y=300, width=220, height=40)

        # button 4: Extra Button 1 (Image+Button)
        bimg4 = Image.open(r"Images for Face detection\7.png")
        bimg4 = bimg4.resize((220, 220))
        self.btnimage4 = ImageTk.PhotoImage(bimg4)
        # image created... now create a button with that image
        btn4 = Button(main_bg, image=self.btnimage4, cursor="hand2", borderwidth=0)
        btn4.place(x=1100, y=80, width=220, height=220)
        # text button
        btn44 = Button(main_bg, text="(Extra Button 1)", cursor="hand2", font=("times new roman", 15, "bold"),
                       bg="#324a5c", fg="white")
        btn44.place(x=1100, y=300, width=220, height=40)

        # button 5: Train Face (Image+Button)
        bimg5 = Image.open(r"Images for Face detection\5.png")
        bimg5 = bimg5.resize((220, 220))
        self.btnimage5 = ImageTk.PhotoImage(bimg5)
        # image created... now create a button with that image
        btn5 = Button(main_bg, image=self.btnimage5, command=self.train_data, cursor="hand2", borderwidth=0)
        btn5.place(x=200, y=380, width=220, height=220)
        # text button
        btn55 = Button(main_bg, text="Train Face", command=self.train_data, cursor="hand2", font=("times new roman", 15, "bold"),
                       bg="#324a5c", fg="white")
        btn55.place(x=200, y=600, width=220, height=40)

        # button 6: Photos (Image+Button)
        bimg6 = Image.open(r"Images for Face detection\6.png")
        bimg6 = bimg6.resize((220, 220))
        self.btnimage6 = ImageTk.PhotoImage(bimg6)
        # image created... now create a button with that image
        btn6 = Button(main_bg, command=self.open_img, image=self.btnimage6, cursor="hand2", borderwidth=0)
        btn6.place(x=500, y=380, width=220, height=220)
        # text button
        btn66 = Button(main_bg, command=self.open_img, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"),
                       bg="#324a5c", fg="white")
        btn66.place(x=500, y=600, width=220, height=40)

        # button 7: Extra Button 2 (Image+Button)
        bimg7 = Image.open(r"Images for Face detection\7.png")
        bimg7 = bimg7.resize((220, 220))
        self.btnimage7 = ImageTk.PhotoImage(bimg7)
        # image created... now create a button with that image
        btn7 = Button(main_bg, image=self.btnimage7, cursor="hand2", borderwidth=0)
        btn7.place(x=800, y=380, width=220, height=220)
        # text button
        btn77 = Button(main_bg, text="(Extra Button 2)", cursor="hand2", font=("times new roman", 15, "bold"),
                       bg="#324a5c", fg="white")
        btn77.place(x=800, y=600, width=220, height=40)

        # button 8: Exit (Image+Button)
        bimg8 = Image.open(r"Images for Face detection\8.png")
        bimg8 = bimg8.resize((220, 220))
        self.btnimage8 = ImageTk.PhotoImage(bimg8)
        # image created... now create a button with that image
        btn8 = Button(main_bg, image=self.btnimage8, command=sys.exit, cursor="hand2", borderwidth=0)
        btn8.place(x=1100, y=380, width=220, height=220)
        # text button
        btn88 = Button(main_bg, text="Exit", command=sys.exit, cursor="hand2", font=("times new roman", 15, "bold"),
                       bg="#324a5c", fg="white")
        btn88.place(x=1100, y=600, width=220, height=40)

    # -----------------------------------------------------------
    # --------------------Function Buttons-----------------------

    def open_img(self):
        os.startfile("face_data")

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Trainer(self.new_window)

    def face_recognizer(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognizer(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    rootwindow = Tk()  # this is a window object
    obj = FaceRecognitionSystem(rootwindow)
    rootwindow.mainloop()
