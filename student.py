from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Face Recognition System")

        # -----------------variables-----------------
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_std_div = StringVar()
        self.var_std_roll = StringVar()
        self.var_std_gender = StringVar()
        self.var_std_email = StringVar()
        self.var_std_phone = StringVar()
        self.var_std_address = StringVar()

        # -----------------variables-----------------

        # ---------------------------image1---------------------------
        student_img1 = Image.open(r"college_images\student_img1.jfif")
        student_img1 = student_img1.resize((500, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(student_img1)
        # showing to the window
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=400, height=150)
        # ---------------------------image1---------------------------

        # ---------------------------image2---------------------------
        student_img2 = Image.open(r"college_images\student_img2.png")
        student_img2 = student_img2.resize((500, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(student_img2)
        # showing to the window
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=400, y=0, width=400, height=150)
        # ---------------------------image2---------------------------

        # ---------------------------image3---------------------------
        student_img3 = Image.open(r"college_images\student_img3.jfif")
        student_img3 = student_img3.resize((500, 150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(student_img3)
        # showing to the window
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=800, y=0, width=400, height=150)
        # ---------------------------image3---------------------------

        # -----------------------Background image-----------------------
        background_student = Image.open(
            r"college_images\background_student.jfif")
        background_student = background_student.resize(
            (1200, 450), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(background_student)
        # showing to the window
        bg_student_lbl = Label(self.root, image=self.photoimg4)
        bg_student_lbl.place(x=0, y=150, width=1200, height=450)

        # --------------------------Root Title--------------------------
        title_lbl = Label(bg_student_lbl, text="Studenet Management System",  font=(
            'times new roman', 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1200, height=45)
        # --------------------------Root Title--------------------------

        # -----------------------Background image-----------------------

        # -------------------Student Page Main Frame-------------------

        main_frame = Frame(bg_student_lbl, bd=3, bg="white")
        main_frame.place(x=10, y=55, width=1180, height=380)

        # ----------------------Left Label Frame----------------------
        left_frame_lbl = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE,
                                    text="Student Details", font=("times new roman", 12, "bold"))
        left_frame_lbl.place(x=10, y=10, width=560, height=350)

        # student_frame_img_left = Image.open(r"college_images\student_frame_img_left.jfif")
        # student_frame_img_left = student_frame_img_left.resize((540, 50), Image.ANTIALIAS)
        # self.photoimg4 = ImageTk.PhotoImage(student_frame_img_left)
        # # showing to the window
        # f_lbl = Label(left_frame_lbl, image=self.photoimg4)
        # f_lbl.place(x=10, y=10, width=540, height=50)

        # ----------------------current_course-----------------
        current_course_label = LabelFrame(
            left_frame_lbl, bd=3, bg="white", relief=RIDGE, text="Current Course", font=("times new roman", 12, "bold"))
        current_course_label.place(x=5, y=0, width=545, height=90)

        # dep----
        dep_label = Label(current_course_label, bg="white",
                          text="Department", font=("times new roman", 12, "bold"))

        dep_label.grid(row=0, column=0, sticky=W)

        dep_combo = ttk.Combobox(
            current_course_label, textvariable=self.var_dep,  width=15, state="readonly")
        dep_combo["values"] = ("Select Department",
                               "Computer SC", "IT", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, sticky=W)
        # ----------------------current_course-----------------

        # course------
        course_label = Label(current_course_label, text="Course",
                             bg="white", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=5, sticky=W)

        course_combo = ttk.Combobox(current_course_label, textvariable=self.var_course,
                                    width=15, state="readonly")
        course_combo["values"] = ("Select Course",
                                  "FE", "SE", "BE", "TE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, sticky=W)
        # course------

        # Year------
        year_label = Label(current_course_label,  text="Year",
                           bg="white", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=5, sticky=W)

        year_combo = ttk.Combobox(current_course_label, textvariable=self.var_year,
                                  width=15, state="readonly")
        year_combo["values"] = ("Select Year",
                                "2018-19", "2019-20", "2020-21", "2021-22")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, sticky=W)
        # Year------

        # Semester------
        semester_label = Label(current_course_label, text="Semester",
                               bg="white", font=("times new roman", 12, "bold"))
        semester_label.grid(row=1, column=2, padx=5, sticky=W)

        course_combo = ttk.Combobox(current_course_label, textvariable=self.var_semester,
                                    width=15, state="readonly")
        course_combo["values"] = ("Select Semester",
                                  "Semester-1", "Semester-2")
        course_combo.current(0)
        course_combo.grid(row=1, column=3, padx=2, sticky=W)
        # Semester------

        # --------Another half--------
        student_info_label = LabelFrame(
            left_frame_lbl, bd=3, bg="white", relief=RIDGE, text="Class Student Info", font=("times new roman", 12, "bold"))
        student_info_label.place(x=5, y=90, width=545, height=230)

        # -------------------------------
        # student Id
        student_id_label = Label(student_info_label, text="Student ID: ",
                                 bg="white", font=("times new roman", 12, "bold"))
        student_id_label.grid(row=0, column=0, padx=5, sticky=W)

        student_id_entryfield = ttk.Entry(
            student_info_label, textvariable=self.var_std_id, width=20)
        student_id_entryfield.grid(row=0, column=1, padx=5, sticky=W)

        # student Name
        student_name_label = Label(student_info_label, text="Student Name: ",
                                   bg="white", font=("times new roman", 12, "bold"))
        student_name_label.grid(row=0, column=2, padx=5, sticky=W)

        student_name_entryfield = ttk.Entry(
            student_info_label, textvariable=self.var_std_name, width=20)
        student_name_entryfield.grid(row=0, column=3, padx=5, sticky=W)

        # student Class Division
        student_class_div_label = Label(student_info_label, text="Class Division: ",
                                        bg="white", font=("times new roman", 12, "bold"))
        student_class_div_label.grid(row=1, column=0, padx=5, sticky=W)

        student_class_div_combo = ttk.Combobox(student_info_label, textvariable=self.var_std_div,
                                  width=15, state="readonly")
        student_class_div_combo["values"] = ("A", "B", "C")
        student_class_div_combo.current(0)
        student_class_div_combo.grid(row=1, column=1, padx=5, sticky=W)

        # student Roll
        student_roll_label = Label(student_info_label, text="Roll : ",
                                   bg="white", font=("times new roman", 12, "bold"))
        student_roll_label.grid(row=1, column=2, padx=5,  sticky=W)

        student_roll_entryfield = ttk.Entry(
            student_info_label, textvariable=self.var_std_roll, width=20)
        student_roll_entryfield.grid(row=1, column=3, padx=5, sticky=W)

        # student Gender
        student_gender_label = Label(student_info_label, text="Gender : ",
                                   bg="white", font=("times new roman", 12, "bold"))
        student_gender_label.grid(row=2, column=0, padx=5,  sticky=W)

        student_gender_combo = ttk.Combobox(student_info_label, textvariable=self.var_std_gender,
                                  width=15, state="readonly")
        student_gender_combo["values"] = ("Male", "Female", "Other")
        student_gender_combo.current(0)
        student_gender_combo.grid(row=2, column=1, padx=5, sticky=W)

        # student Email
        student_email_label = Label(student_info_label, text="Email : ",
                                    bg="white", font=("times new roman", 12, "bold"))
        student_email_label.grid(row=2, column=2, padx=5, sticky=W)

        student_email_entryfield = ttk.Entry(
            student_info_label, textvariable=self.var_std_email, width=20)
        student_email_entryfield.grid(row=2, column=3, padx=5, sticky=W)

        # student Phone
        student_phone_label = Label(student_info_label, text="Phone : ",
                                    bg="white", font=("times new roman", 12, "bold"))
        student_phone_label.grid(row=3, column=0, padx=5, sticky=W)

        student_phone_entryfield = ttk.Entry(
            student_info_label, textvariable=self.var_std_phone, width=20)
        student_phone_entryfield.grid(row=3, column=1, padx=5, sticky=W)

        # student Address
        student_address_label = Label(student_info_label, text="Address : ",
                                      bg="white", font=("times new roman", 12, "bold"))
        student_address_label.grid(row=3, column=2, padx=5, sticky=W)

        student_address_entryfield = ttk.Entry(
            student_info_label, textvariable=self.var_std_address, width=20)
        student_address_entryfield.grid(row=3, column=3, padx=5, sticky=W)

        # Radio Buttons--------
        self.var_radio1 = StringVar()
        radio_btn1 = ttk.Radiobutton(
            student_info_label, variable=self.var_radio1, text="Take a photo sample", value="Yes")
        radio_btn1.grid(row=4, column=0)
        # ---------------
        radio_btn2 = ttk.Radiobutton(
            student_info_label, variable=self.var_radio1, text="No Photo Sample", value="No")
        radio_btn2.grid(row=4, column=1)

        # Radio Buttons--------

        # Button Frame--------
        btn_frame = Frame(student_info_label, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=125, width=540, height=80)
        # ---------
        save_btn = Button(btn_frame, text="Save", command=self.add_data,
                          width=15, cursor="hand2", bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=10, pady=5)
        # ----------
        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=15,
                            cursor="hand2", bg="blue", fg="white")
        update_btn.grid(row=0, column=1, padx=10, pady=5)
        # ----------
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=15,
                            cursor="hand2", bg="blue", fg="white")
        delete_btn.grid(row=0, column=2, padx=10, pady=5)
        # ----------
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=15,
                           cursor="hand2", bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=10, pady=5)
        # ----------
        take_photo_btn = Button(
            btn_frame, text="Take a Photo", command=self.generate_dataset, width=15, cursor="hand2", bg="green", fg="white")
        take_photo_btn.grid(row=1, column=0, padx=10, pady=5)
        # ----------
        update_photo_btn = Button(
            btn_frame, text="Update Photo", width=15, cursor="hand2", bg="green", fg="white")
        update_photo_btn.grid(row=1, column=2, padx=10, pady=5)
        # Button Frame--------

        # -------------------------------

        # ----------------------Left Label Frame----------------------

        # ----------------------Right Label Frame----------------------
        right_frame_label = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE,
                                       text="Student Details", font=("times new roman", 12, "bold"))
        right_frame_label.place(x=590, y=10, width=560, height=350)

        # --------search system---------
        search_label = LabelFrame(
            right_frame_label, bd=3, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_label.place(x=5, y=0, width=545, height=90)

        # ------------

        search_by_label = Label(search_label, bg="white", text="Search By: ", font=(
            "times new roman", 12, "bold"))

        search_by_label.grid(row=0, column=0, sticky=W)

        search_by_combo = ttk.Combobox(search_label,
                                       width=15, state="readonly")
        search_by_combo["values"] = ("Select",
                                     "Roll ", "Phone", "Mechanical")
        search_by_combo.current(0)
        search_by_combo.grid(row=0, column=1, padx=2, sticky=W)
        # ----------
        search_entryfield = ttk.Entry(search_label, width=20)
        search_entryfield.grid(row=0, column=2, sticky=W)
        # ----------
        # ----------
        search_btn = Button(search_label, text="Search", width=15,
                            cursor="hand2", bg="white", fg="black")
        search_btn.grid(row=1, column=1, pady=5)
        # ----------
        show_btn = Button(search_label, text="Show All", width=15,
                          cursor="hand2", bg="white", fg="black")
        show_btn.grid(row=1, column=2, pady=5)
        # --------search system---------

        # --------------another half frame scroll--------------
        student_info_frame = Frame(
            right_frame_label, bd=2, bg="white", relief=RIDGE)
        student_info_frame.place(x=5, y=90, width=545, height=230)

        scroll_x = ttk.Scrollbar(student_info_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(student_info_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(student_info_frame, columns=(
            "dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "email", "phone", "address", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="Photo")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # --------------another half frame scroll--------------

        # ----------------------Right Label Frame----------------------

        # -------------------Student Page Main Frame-------------------

    # -----------------------function decleration-----------------------

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Saiket#26", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_std_div.get(),
                                                                                                            self.var_std_roll.get(),
                                                                                                            self.var_std_gender.get(),
                                                                                                            self.var_std_email.get(),
                                                                                                            self.var_std_phone.get(),
                                                                                                            self.var_std_address.get(),
                                                                                                            self.var_radio1.get()
                                                                                                        ))
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo(
                    "Success", "Student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)
    # -----------------------function decleration-----------------------

    # ----------------------------fetch data----------------------------

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Saiket#26", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if(len(data) != 0):
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ----------------------------fetch data----------------------------

    # ----------------------------get cursor----------------------------
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_std_div.set(data[6])
        self.var_std_roll.set(data[7])
        self.var_std_gender.set(data[8])
        self.var_std_email.set(data[9])
        self.var_std_phone.set(data[10])
        self.var_std_address.set(data[11])
        self.var_radio1.set(data[12])

    # ----------------------------get cursor----------------------------

    # ---------------------------update func---------------------------
    def update_data(self):
        if self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update this field", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Saiket#26", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s,Name=%s, Division=%s, Roll=%s, Gender=%s, Email=%s, Phone=%s, Address=%s ,PhotoSample=%s where Student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_std_div.get(),
                        self.var_std_roll.get(),
                        self.var_std_gender.get(),
                        self.var_std_email.get(),
                        self.var_std_phone.get(),
                        self.var_std_address.get(),

                        self.var_radio1.get(),
                        self.var_std_id.get()

                    ))

                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Field updated successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to : {str(es)}", parent=self.root)
    # ---------------------------update func---------------------------

    # ---------------------------Delete func---------------------------

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student Id Required Please Select ID")

        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page", "Do you want to delete this field", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                         host="localhost", username="root", password="Saiket#26", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)

                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted this field", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to : {str(es)}", parent=self.root)

    # ---------------------------Delete func---------------------------
    #  ---------------------------reset func---------------------------

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_std_div.set("")
        self.var_std_roll.set("")
        self.var_std_gender.set("")
        self.var_std_email.set("")
        self.var_std_phone.set("")
        self.var_std_address.set("")
        self.var_radio1.set("")

    #  ---------------------------reset func---------------------------

    # ----------------generate dataset take photo sample----------------

    def generate_dataset(self):
            if self.var_std_name.get() == "" or self.var_std_id.get() == "":
                messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Saiket#26", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("select * from student")
                    my_result= my_cursor.fetchall()
                    id=0
                    for x in my_result:
                        id+=1
                    my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s,Name=%s, Division=%s, Roll=%s, Gender=%s, Email=%s, Phone=%s, Address=%s ,PhotoSample=%s where Student_id=%s", (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_std_div.get(),
                            self.var_std_roll.get(),
                            self.var_std_gender.get(),
                            self.var_std_email.get(),
                            self.var_std_phone.get(),
                            self.var_std_address.get(),

                            self.var_radio1.get(),
                            self.var_std_id.get()

                        ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()
                    
# load pre trained models
                        
                    face_classifier=cv2.CascadeClassifier("frontal-face-default.xml")

                    def face_cropped(img):
                        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        # scalling factor=1.3
                        # minimum neibour=5

                        for(x,y,w,h) in faces:
                            face_cropped=img[y:y+h, x:x+w]
                            return face_cropped

                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped face",face)

                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating Dataset completed")

                except Exception as es:messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)




    # ----------------generate dataset take photo sample----------------














if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
