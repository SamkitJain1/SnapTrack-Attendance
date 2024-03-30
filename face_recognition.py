from tkinter import *

from PIL import Image, ImageTk
from algorithms.face_recognise_algo import face_recogniser

class FaceRecognizer:

    def __init__(self, root):
        self.n, self.s_id, self.r, self.d = None, None, None, None
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
        main_bg.place(x=0, y=130, width=1500, height=665)

        # Main title
        title_label = Label(main_bg, text="SNAPTRACK ATTENDANCE", font=("times new roman", 35, "bold"), bg="black",
                            fg="white")
        title_label.place(x=0, y=0, width=1500,
                          height=45)  # x and y are 0 because now we're considering with respect to only the image, not the entire window

        # # ---------------Main Title---------------
        # title_label = Label(self.root, text="Facial Recognition", font=("times new roman", 35, "bold"), bg="red", fg="white")
        # title_label.place(x=0, y=0, width=1500, height=55)  # x and y are 0 because now we're considering with respect to only the image, not the entire window

        # ----------------Left image----------------- (one single long image)
        # left_img = Image.open(r"Images for Face detection\bg3.png")
        # left_img = left_img.resize((650, 700))  # same as label's height
        # self.left_photoimage = ImageTk.PhotoImage(left_img)
        #  image has been created as an object, now create a label to represent that image
        label1 = Label(main_bg, bg="#346d8b")
        label1.place(x=0, y=45, width=750, height=620)  # height 740 maybe?

        # ----------------Right image----------------- (one single long image)
        right_img = Image.open(r"Images for Face detection\bg3.png")
        right_img = right_img.resize((800, 620))
        self.right_photoimage = ImageTk.PhotoImage(right_img)
        # image has been created as an object, now create a label to represent that image
        label2 = Label(main_bg, image=self.right_photoimage)
        label2.place(x=750, y=45, width=800, height=620)

        # -----------Button---------------------------
        btn = Button(label2, text="Start Face Recognition", command=face_recogniser, cursor="hand2",
                     font=("times new roman", 20, "bold"), bg="#324a5c", fg="white")
        btn.place(x=230, y=450, width=320, height=55)

        # ---------Image logo------------
        logo_img = Image.open(r"Images for Face detection\logoimg.png")
        logo_img = logo_img.resize((300, 300))
        self.logo_photoimage = ImageTk.PhotoImage(logo_img)
        label3 = Label(label2, image=self.logo_photoimage)
        label3.place(x=240, y=120, width=300, height=300)

    # -----------function for face_recognise_algo -------------


if __name__ == "__main__":
    rootwindow = Tk()  # this is a window object
    obj = FaceRecognizer(rootwindow)
    rootwindow.mainloop()
