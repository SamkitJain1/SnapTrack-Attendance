from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
import os
import csv
from tkinter import filedialog
from tkinter import messagebox


my_data = []
class Attendance:

    def __init__(self, root1):
        self.n, self.s_id, self.r, self.d = None, None, None, None
        self.root = root1
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        # --------------- Variable ---------------
        self.var_stud_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_status = StringVar()

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
        main_bg.place(x=0, y=180, width=1500, height=660)

        # Main title
        title_label = Label(self.root, text="SNAPTRACK ATTENDANCE", font=("times new roman", 35, "bold"), bg="black",
                            fg="white")
        title_label.place(x=0, y=131, width=1500,
                          height=50)  # x and y are 0 because now we're considering with respect to only the image, not the entire window

        # --------------Main Frame--------------
        main_frame = Frame(main_bg, bd=2)
        main_frame.place(x=15, y=70, width=1465, height=500)

        # Left Frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=5, width=730, height=480)

        # image
        # left_image = Image.open(r"Images for Face detection\bg4.png")
        # left_image = left_image.resize((720, 130))
        # self.photoimage_left = ImageTk.PhotoImage(left_image)
        # placing the image as a label
        left_image_label = Label(left_frame, bg="#5882a1")
        left_image_label.place(x=5, y=0, width=717, height=130)

        # left sub-frame
        left_sub_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, font=("times new roman", 12, "bold"))
        left_sub_frame.place(x=5, y=140, width=717, height=310)

        # different labels within the left sub-frame

        # sub label 1 (Student ID)
        student_id_label = Label(left_sub_frame, text="Student ID:", font=("times new roman", 12, "bold"))
        student_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        # a dropdown menu
        student_id_entry = ttk.Entry(left_sub_frame, width=20, textvariable=self.var_stud_id, font=("times new roman", 12, "bold"))
        student_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # sub level 2 (Roll No)
        rollno_label = Label(left_sub_frame, text="Roll No:", font=("times new roman", 12, "bold"))
        rollno_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        # entry field for the above label
        dep_name_entry = ttk.Entry(left_sub_frame, width=20, textvariable=self.var_roll, font=("times new roman", 12, "bold"))
        dep_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # sub level 3 (Name)
        name_label = Label(left_sub_frame, text="Name:", font=("times new roman", 12, "bold"))
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        # entry field for the above label
        name_entry = ttk.Entry(left_sub_frame, width=20, textvariable=self.var_name, font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # sub level 4 (Department)
        dep_label = Label(left_sub_frame, text="Department:", font=("times new roman", 12, "bold"))
        dep_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        # entry field for the above label
        dep_entry = ttk.Entry(left_sub_frame, width=20, textvariable=self.var_dep, font=("times new roman", 12, "bold"))
        dep_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # sub level 5 (Time)
        time_label = Label(left_sub_frame, text="Time:", font=("times new roman", 12, "bold"))
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        # entry field for the above label
        time_entry = ttk.Entry(left_sub_frame, width=20, textvariable=self.var_time, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # sub level 6 (Date)
        date_label = Label(left_sub_frame, text="Date:", font=("times new roman", 12, "bold"))
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        # entry field for the above label
        date_entry = ttk.Entry(left_sub_frame, width=20, textvariable=self.var_date, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # sub level 7 (Attendance Status)
        attendance_status_label = Label(left_sub_frame, text="Attendance Status:", font=("times new roman", 12, "bold"))
        attendance_status_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        # combo box for the above label
        attendance_status_combo = ttk.Combobox(left_sub_frame, textvariable=self.var_status, font=("times new roman", 12, "bold"), width=18, state="readonly")
        attendance_status_combo["values"] = ("Status", "Present", "Absent")
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # ------------ Button Frame ------------

        btn_frame = Frame(left_sub_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=250, width=713, height=35)

        import_csv_btn = Button(btn_frame, text="Import CSV", command=self.import_csv, width=19, font=("times new roman", 12, "bold"), bg="#324a5c", fg="white")
        import_csv_btn.grid(row=0, column=0)

        export_csv_btn = Button(btn_frame, text="Export CSV", command=self.export_csv, width=19, font=("times new roman", 12, "bold"), bg="#324a5c", fg="white")
        export_csv_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", width=19, font=("times new roman", 12, "bold"), bg="#324a5c", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset, width=19, font=("times new roman", 12, "bold"), bg="#324a5c", fg="white")
        reset_btn.grid(row=0, column=3)

        # Right Frame ---------------------------------

        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=5, width=700, height=480)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=5, width=687, height=445)

        # Scroll Bar table -----
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_report_table = ttk.Treeview(table_frame, columns=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_report_table.xview)
        scroll_y.config(command=self.attendance_report_table.yview)

        self.attendance_report_table.heading("id", text="Student ID")
        self.attendance_report_table.heading("roll", text="Roll No")
        self.attendance_report_table.heading("name", text="Name")
        self.attendance_report_table.heading("department", text="Department")
        self.attendance_report_table.heading("time", text="Time")
        self.attendance_report_table.heading("date", text="Date")
        self.attendance_report_table.heading("attendance", text="Status")

        self.attendance_report_table["show"] = "headings"

        self.attendance_report_table.column("id", width=100)
        self.attendance_report_table.column("roll", width=100)
        self.attendance_report_table.column("name", width=100)
        self.attendance_report_table.column("department", width=100)
        self.attendance_report_table.column("time", width=100)
        self.attendance_report_table.column("date", width=100)
        self.attendance_report_table.column("attendance", width=100)

        self.attendance_report_table.pack(fill=BOTH, expand=1)
        self.attendance_report_table.bind("<ButtonRelease>", self.get_cursor)

    # ---------- Button Function ---------

    # fetch data
    def fetch_data(self, rows):
        self.attendance_report_table.delete(*self.attendance_report_table.get_children())
        for i in rows:
            self.attendance_report_table.insert("", END, values=i)

    # import csv
    def import_csv(self):
        global my_data
        my_data.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as file:
            csvread = csv.reader(file, delimiter=",")
            for i in csvread:
                my_data.append(i)
            self.fetch_data(my_data)

    # export csv
    def export_csv(self):
        try:
            if len(my_data) < 1:
                messagebox.showerror("No Data", "No data found to export!", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as file:
                exp_write = csv.writer(file, delimiter=",")

                for i in my_data:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data has been exported to " + os.path.basename(fln))
        except Exception as e:
            messagebox.showerror("Error", f"Due to:\n{str(e)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.attendance_report_table.focus()
        content = self.attendance_report_table.item(cursor_row)
        rows = content["values"]

        self.var_stud_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_status.set(rows[6])

    def reset(self):
        self.var_stud_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("Status")

#
#
#

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()