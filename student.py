from tkinter import *
from tkinter import ttk

import mysql.connector
from PIL import Image, ImageTk
from tkinter import messagebox
from algorithms.capture_photos_algo import take_photo


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        #  ----------------------variables-------------------------
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()  # 14 fields-----------

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

        img4 = Image.open(r"Images for Face detection\bg1.3.png")
        img4 = img4.resize((1500, 660))
        self.photoimage_bg = ImageTk.PhotoImage(img4)
        # image has4 been created as an object, now create a label to represent that image
        bg_img = Label(self.root, bg="#346d8b", borderwidth=1)
        bg_img.place(x=0, y=130, width=1500, height=660)

        # ----------------Main title-----------------
        title_label = Label(bg_img, text="SNAPTRACK ATTENDANCE", font=("times new roman", 35, "bold"), bg="black",
                            fg="white")
        title_label.place(x=0, y=0, width=1500,
                          height=45)  # x and y are 0 because now we're considering with respect to only the image, not the entire window

        # Main Frame window
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=15, y=55, width=1465, height=600)

        # Left Frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=730, height=580)
        # image
        # left_image = Image.open(r"Images for Face detection\bg4.1.png")
        # left_image = left_image.resize((720, 130))
        # self.photoimage_left = ImageTk.PhotoImage(left_image)
        # placing the image as a label
        left_image_label = Label(left_frame, bg="#5882a1")
        left_image_label.place(x=5, y=0, width=717, height=130)

        # Current Course Frame
        current_course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Current Course Information",
                                          font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=140, width=717, height=110)

        # different labels within the current course

        # sub label 1 (Department)
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=2, pady=5, sticky=W)
        # a dropdown menu
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"),
                                 width=17, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Commerce")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        # sub label 2 (Course)
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=2, pady=5, sticky=W)
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,
                                    font=("times new roman", 12, "bold"), width=17, state="readonly")
        course_combo["values"] = ("Select Course", "BCom", "BBA", "BCA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        # sub label 3 (Year)
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=2, pady=5, sticky=W)
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,
                                  font=("times new roman", 12, "bold"), width=17, state="readonly")
        year_combo["values"] = ("Select Year", "1st", "2nd", "3rd", "4th")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        # sub label 4 (Semester)
        sem_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"))
        sem_label.grid(row=1, column=2, padx=2, pady=5, sticky=W)
        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester,
                                 font=("times new roman", 12, "bold"), width=17, state="readonly")
        sem_combo["values"] = ("Select Semester", "I", "II", "III", "IV", "V", "VI", "VII", "VIII")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=5, sticky=W)

        # Class Student Information Frame
        class_student_info_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Class Student Information",
                                              font=("times new roman", 12, "bold"))
        class_student_info_frame.place(x=5, y=260, width=717, height=295)

        # different labels within the class student information frame

        # sub level 1 (student ID)
        student_id_label = Label(class_student_info_frame, text="Student ID:", font=("times new roman", 12, "bold"))
        student_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        # entry field for the above label
        student_id_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_std_id, width=20,
                                     font=("times new roman", 12, "bold"))
        student_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # sub level 2 (student name)
        student_name_label = Label(class_student_info_frame, text="Student Name:", font=("times new roman", 12, "bold"))
        student_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        # entry field for the above label
        student_name_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_std_name, width=20,
                                       font=("times new roman", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # sub level 3 (Division)
        course1_label = Label(class_student_info_frame, text="Division:", font=("times new roman", 12, "bold"))
        course1_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        # entry field for the above label
        course1_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_div, width=20,
                                  font=("times new roman", 12, "bold"))
        course1_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # sub level 4 (Roll No)
        rollno_label = Label(class_student_info_frame, text="Roll No:", font=("times new roman", 12, "bold"))
        rollno_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        # entry field for the above label
        rollno_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_roll, width=20,
                                 font=("times new roman", 12, "bold"))
        rollno_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # sub level 5 (Gender)
        gender_label = Label(class_student_info_frame, text="Gender:", font=("times new roman", 12, "bold"))
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        # combo box for the above label
        gender_combo = ttk.Combobox(class_student_info_frame, textvariable=self.var_gender,
                                    font=("times new roman", 12, "bold"), width=18, state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # sub level 6 (DOB)
        dob_label = Label(class_student_info_frame, text="DOB:", font=("times new roman", 12, "bold"))
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        # entry field for the above label
        dob_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_dob, width=20,
                              font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # sub level 7 (Email)
        email_label = Label(class_student_info_frame, text="Email:", font=("times new roman", 12, "bold"))
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        # entry field for the above label
        email_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_email, width=20,
                                font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # sub level 8 (Phone No)
        student_id_label = Label(class_student_info_frame, text="Phone No:", font=("times new roman", 12, "bold"))
        student_id_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        # entry field for the above label
        student_id_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_phone, width=20,
                                     font=("times new roman", 12, "bold"))
        student_id_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # sub level 9 (Address)
        address_label = Label(class_student_info_frame, text="Address:", font=("times new roman", 12, "bold"))
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        # entry field for the above label
        address_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_address, width=20,
                                  font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # sub level 10 (Teacher)
        teacher_label = Label(class_student_info_frame, text="Teacher:", font=("times new roman", 12, "bold"))
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        # entry field for the above label
        teacher_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_teacher, width=20,
                                  font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio buttons
        self.var_radio = StringVar()

        radiobtn1 = ttk.Radiobutton(class_student_info_frame, variable=self.var_radio, text="Take a photo sample",
                                    value="Yes")
        radiobtn1.grid(row=5, column=0, padx=10, pady=5, sticky=W)

        radiobtn2 = ttk.Radiobutton(class_student_info_frame, variable=self.var_radio, text="No photo sample",
                                    value="no")
        radiobtn2.grid(row=5, column=1, padx=6)

        # ---------------------Buttons Frame------------------------

        btn_frame = Frame(class_student_info_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=713, height=35)

        save_btn = Button(btn_frame, command=self.add_data, text="Save", width=19, font=("times new roman", 12, "bold"),
                          bg="#324a5c", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, command=self.update_data, text="Update", width=19, font=("times new roman", 12, "bold"), bg="#324a5c",
                            fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=19, font=("times new roman", 12, "bold"), bg="#324a5c",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, command=self.reset, text="Reset", width=19, font=("times new roman", 12, "bold"), bg="#324a5c",
                           fg="white")
        reset_btn.grid(row=0, column=3)

        # button frame no. 2--------------------------
        btn_frame2 = Frame(class_student_info_frame, bd=2, relief=RIDGE)
        btn_frame2.place(x=0, y=235, width=713, height=35)

        take_photo_btn = Button(btn_frame2, command=self.generate_dataset, text="Take Photo Sample", width=39, font=("times new roman", 12, "bold"),
                                bg="#324a5c", fg="white")
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame2, text="Update Photo Sample", width=38,
                                  font=("times new roman", 12, "bold"), bg="#324a5c", fg="white")
        update_photo_btn.grid(row=1, column=1)

        # ---------------------------------------------------

        # Right Frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=700, height=580)

        # right_image = Image.open(r"Images for Face detection\bg4.1.png")
        # right_image = right_image.resize((720, 130))
        # self.photoimage_right = ImageTk.PhotoImage(right_image)
        # placing the image as a label
        left_image_label = Label(right_frame, bg="#5882a1")
        left_image_label.place(x=5, y=0, width=687, height=130)

        # ------------------ Search System ------------------
        search_system_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search System",
                                         font=("times new roman", 12, "bold"))
        search_system_frame.place(x=5, y=140, width=687, height=70)

        search_label = Label(search_system_frame, text="Search by:", font=("times new roman", 12, "bold"))
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        search_combo = ttk.Combobox(search_system_frame, font=("times new roman", 12, "bold"), width=10,
                                    state="readonly")
        search_combo["values"] = ("Select", "Roll_No", "Phone")
        search_combo.current(0)
        search_combo.grid(row=0, column=2, padx=2, pady=5, sticky=W)

        search_entry = ttk.Entry(search_system_frame, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=3, padx=10, pady=4, sticky=W)

        search_btn = Button(search_system_frame, text="Search", width=14, font=("times new roman", 12, "bold"),
                            bg="#324a5c", fg="white")
        search_btn.grid(row=0, column=4, padx=4)

        showall_btn = Button(search_system_frame, text="Show All", width=14, font=("times new roman", 12, "bold"),
                             bg="#324a5c", fg="white")
        showall_btn.grid(row=0, column=5, padx=4)

        # -------------------- Table Frame --------------------
        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=215, width=687, height=340)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="RollNo")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")  # --------------------------only 11 fields instead of 14 ---RECTIFIED!!
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
        # setting widths
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)  # --------------------------only 11 fields instead of 14 ---RECTIFIED!
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # ----------------function decoration------------------- (defining functions to put in the above buttons)

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Samkit!sqL20",
                                               database="attendence_system")
                cursor = conn.cursor()
                cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                               (
                                   self.var_dep.get(),
                                   self.var_course.get(),
                                   self.var_year.get(),
                                   self.var_semester.get(),
                                   self.var_std_id.get(),
                                   self.var_std_name.get(),
                                   self.var_div.get(),
                                   self.var_roll.get(),
                                   self.var_gender.get(),
                                   self.var_dob.get(),
                                   self.var_email.get(),
                                   self.var_phone.get(),
                                   self.var_address.get(),
                                   self.var_teacher.get(),
                                   self.var_radio.get()
                               )
                               )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details added successfully!", parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", f"Due to:\n {str(e)}", parent=self.root)

    # -----------------------------fetch data---------------------------------
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Samkit!sqL20",
                                       database="attendence_system")
        cursor = conn.cursor()
        cursor.execute("select * from student")
        data = cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # --------------------------get cursor------------------------------
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio.set(data[14])

    # ------------------------update function---------------------------
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Are you sure you want to update?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Samkit!sqL20",
                                                   database="attendence_system")
                    cursor = conn.cursor()
                    cursor.execute("update student set department=%s, course=%s, year=%s, semester=%s, name=%s, division=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photosample=%s where student_id=%s;",
                                   (
                                       self.var_dep.get(),
                                       self.var_course.get(),
                                       self.var_year.get(),
                                       self.var_semester.get(),
                                       self.var_std_name.get(),
                                       self.var_div.get(),
                                       self.var_roll.get(),
                                       self.var_gender.get(),
                                       self.var_dob.get(),
                                       self.var_email.get(),
                                       self.var_phone.get(),
                                       self.var_address.get(),
                                       self.var_teacher.get(),
                                       self.var_radio.get(),
                                       self.var_std_id.get()
                                   )
                                   )
                else:
                    return

                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "Student details updated successfuly!", parent=self.root)
                conn.close()

            except Exception as e:
                messagebox.showerror("Error", f"Due to:\n {str(e)}", parent=self.root)

    # ----------------delete function---------------
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required to perform this action", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Student Record", "Are you sure you want to delete the selected record?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Samkit!sqL20",
                                                   database="attendence_system")
                    cursor = conn.cursor()
                    cursor.execute("delete from student where student_id=%s", (self.var_std_id.get(),))
                else:
                    return
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Delete", "Student data deleted successfully!", parent=self.root)
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Due to:\n {str(e)}", parent=self.root)

    # --------------------reset function-------------------
    def reset(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio.set("")

    # --------------------Take Photo Sample (Generate data set) -------------------
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Samkit!sqL20",
                                               database="attendence_system")
                cursor = conn.cursor()
                cursor.execute("select * from student")
                result = cursor.fetchall()
                s_id = 0
                for _ in result:
                    s_id += 1
                cursor.execute(
                    "update student set department=%s, course=%s, year=%s, semester=%s, name=%s, division=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photosample=%s where student_id=%s;",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio.get(),
                        self.var_std_id.get()
                    )
                    )

                # -------------------take photo algo-------------------
                take_photo(s_id)

                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()

                messagebox.showinfo("Result", "Generating data set successfull!")

            except Exception as e:
                messagebox.showerror("Error", f"Due to:\n{str(e)}", parent=self.root)


if __name__ == "__main__":
    rootwindow = Tk()  # this is a window object
    obj = Student(rootwindow)
    rootwindow.mainloop()


# add -----> "can't update the student ID"
