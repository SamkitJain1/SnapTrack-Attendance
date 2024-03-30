from tkinter import *

from PIL import Image, ImageTk
from algorithms.train_face_algo import train_function


class Trainer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
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
        main_bg = Label(self.root, bg="dark gray", borderwidth=1)
        main_bg.place(x=0, y=130, width=1500, height=660)

        # Main title
        title_label = Label(main_bg, text="SNAPTRACK ATTENDANCE", font=("times new roman", 35, "bold"), bg="black",
                            fg="white")
        title_label.place(x=0, y=0, width=1500,
                          height=45)  # x and y are 0 because now we're considering with respect to only the image, not the entire window

        #

        # # ----------------Main title-----------------
        # title_label = Label(main_bg, text="Train Face", font=("times new roman", 35, "bold"), bg="black", fg="white")
        # title_label.place(x=0, y=80, width=1500, height=55)  # x and y are 0 because now we're considering with respect to only the image, not the entire window

        # ----------------top image----------------- (one single long image)
        # top_img = Image.open(r"Images for Face detection\bg2.png")
        # top_img = top_img.resize((1500, 325))
        # self.top_photoimage = ImageTk.PhotoImage(top_img)
        #  image has been created as an object, now create a label to represent that image
        label1 = Label(main_bg, bg="#346d8b")
        label1.place(x=0, y=45, width=1500, height=325)

        # --------------bottom image--------------- (same dimensions as top image)
        # bottom_img = Image.open(r"Images for Face detection\bg4.png")
        # bottom_img = bottom_img.resize((1500, 350))
        # self.bottom_photoimage = ImageTk.PhotoImage(bottom_img)
        #  image has been created as an object, now create a label to represent that image
        label2 = Label(self.root, bg="#a9ccdf")
        label2.place(x=0, y=480, width=1500, height=315)

        # ------- Train button--------------------------------------
        btn = Button(self.root, text="Train Data", command=train_function, cursor="hand2", font=("times new roman", 20, "bold"), bg="#324a5c", fg="white")
        btn.place(x=0, y=420, width=1500, height=60)

        # ---------------- Training Classifier ------------------
        # train_face_algo.trainer() # no need of this cause the function is already added as a command in the button


if __name__ == "__main__":
    rootwindow = Tk()  # this is a window object
    obj = Trainer(rootwindow)
    rootwindow.mainloop()
