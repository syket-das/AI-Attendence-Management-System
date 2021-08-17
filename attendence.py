from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2
import os
import csv
from tkinter import filedialog


mydata = []


class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Attendence")

        # --------------------variables--------------------
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendence=StringVar()

        # --------------------variables--------------------

        # ---------------------------image1---------------------------
        attendence_img1 = Image.open(r"college_images\attendence1.jfif")
        attendence_img1 = attendence_img1.resize((500, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(attendence_img1)
        # showing to the window
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=400, height=150)
        # ---------------------------image1---------------------------

        # ---------------------------image2---------------------------
        attendence_img2 = Image.open(r"college_images\attendence2.jfif")
        attendence_img2 = attendence_img2.resize((500, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(attendence_img2)
        # showing to the window
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800, y=0, width=400, height=150)
        # ---------------------------image2---------------------------

        # --------------------------Root Title--------------------------
        title_lbl = Label(self.root, text="Studenet Attendence System",  font=(
            'times new roman', 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=155, width=1200, height=45)
        # --------------------------Root Title--------------------------

        # --------------------------Main Frame--------------------------
        main_frame = Frame(self.root, bd=3, bg="lightgray")
        main_frame.place(x=0, y=200, width=1200, height=400)
        # --------------------------Main Frame--------------------------

        # ----------------------Left Label Frame----------------------
        left_frame_lbl = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE,
                                    text="Student Information", font=("times new roman", 12, "bold"))
        left_frame_lbl.place(x=20, y=10, width=560, height=380)

        # ---------
        left_main_frame = Frame(left_frame_lbl, bd=3, relief=RIDGE, bg="white")
        left_main_frame.place(x=0, y=10, width=550, height=300)

        # ---------------------------labes and entry--------------------
        # attendence id------
        attendence_id_label = Label(left_main_frame, text="Attendence ID: ",
                                    bg="white", font=("times new roman", 12, "bold"))
        attendence_id_label.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        attendence_id_entryfield = ttk.Entry(left_main_frame, width=20, textvariable=self.var_atten_id)
        attendence_id_entryfield.grid(
            row=0, column=1, padx=5, pady=10, sticky=W)

        # Name--------
        attendence_name_label = Label(left_main_frame, text="Name: ",
                                      bg="white", font=("times new roman", 12, "bold"))
        attendence_name_label.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        attendence_name_entryfield = ttk.Entry(left_main_frame, width=20,textvariable=self.var_atten_name)
        attendence_name_entryfield.grid(
            row=0, column=3, padx=5, pady=10, sticky=W)

        # Roll--------
        attendence_roll_label = Label(left_main_frame, text="Roll: ",
                                      bg="white", font=("times new roman", 12, "bold"))
        attendence_roll_label.grid(row=1, column=0, padx=5, pady=10, sticky=W)

        attendence_roll_entryfield = ttk.Entry(left_main_frame,  width=20, textvariable=self.var_atten_roll)
        attendence_roll_entryfield.grid(
            row=1, column=1, padx=5, pady=10, sticky=W)
        # ---------------------------labes and entry--------------------
        # Department--------
        attendence_dep_label = Label(left_main_frame, text="Department: ",
                                     bg="white", font=("times new roman", 12, "bold"))
        attendence_dep_label.grid(row=1, column=2, padx=5, pady=10, sticky=W)

        attendence_dep_entryfield = ttk.Entry(left_main_frame,  width=20, textvariable=self.var_atten_dep)
        attendence_dep_entryfield.grid(
            row=1, column=3, padx=5, pady=10, sticky=W)
        # ---------------------------labes and entry--------------------
        # Time--------
        attendence_time_label = Label(left_main_frame, text="Time: ",
                                      bg="white", font=("times new roman", 12, "bold"))
        attendence_time_label.grid(row=2, column=0, padx=5, pady=10, sticky=W)

        attendence_time_entryfield = ttk.Entry(left_main_frame,  width=20, textvariable=self.var_atten_time)
        attendence_time_entryfield.grid(
            row=2, column=1, padx=5, pady=10, sticky=W)
        # Date--------
        attendence_date_label = Label(left_main_frame, text="Time: ",
                                      bg="white", font=("times new roman", 12, "bold"))
        attendence_date_label.grid(row=2, column=2, padx=5, pady=10, sticky=W)

        attendence_date_entryfield = ttk.Entry(left_main_frame, width=20,textvariable=self.var_atten_date)
        attendence_date_entryfield.grid(
            row=2, column=3, padx=5, pady=10, sticky=W)
        # status
        attendence_status_label = Label(left_main_frame, text="Attendence Status : ",
                                        bg="white", font=("times new roman", 12, "bold"))
        attendence_status_label.grid(
            row=3, column=0, padx=5, pady=10,  sticky=W)

        attendence_status_label = ttk.Combobox(left_main_frame,
                                                width=20, textvariable=self.var_atten_attendence, state="readonly")
        attendence_status_label["values"] = ("Present", "Absent")
        attendence_status_label.current(0)
        attendence_status_label.grid(
            row=3, column=1, padx=5, pady=10, sticky=W)
        # ---------------------------labes and entry--------------------
        # Button Frame--------
        btn_frame = Frame(left_main_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=250, width=540, height=40)
        # ---------
        save_btn = Button(btn_frame, text="Import CSV", command=self.importCsv,
                          width=15, cursor="hand2", bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=10, pady=5)
        # ----------
        update_btn = Button(btn_frame, text="Export CSV", command=self.exportCsv, width=15,
                            cursor="hand2", bg="blue", fg="white")
        update_btn.grid(row=0, column=1, padx=10, pady=5)
        # ----------
        delete_btn = Button(btn_frame, text="Update",  width=15,
                            cursor="hand2", bg="blue", fg="white")
        delete_btn.grid(row=0, column=2, padx=10, pady=5)
        # ----------
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=15,
                           cursor="hand2", bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=10, pady=5)
        # ----------------------Left Label Frame----------------------

        # ----------------------Right Label Frame----------------------
        right_frame_label = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE,
                                       text="Attendence Details", font=("times new roman", 12, "bold"))
        right_frame_label.place(x=600, y=10, width=560, height=380)

        right_frame = Frame(right_frame_label, bd=2, relief=RIDGE)
        right_frame.place(x=5, y=5, width=540, height=340)

        scroll_x = ttk.Scrollbar(right_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(right_frame, orient=VERTICAL)

        self.AttendenctReportTable = ttk.Treeview(right_frame, columns=(
            "id", "roll", "name", "department", "time", "date", "attendence"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendenctReportTable.xview)
        scroll_y.config(command=self.AttendenctReportTable.yview)

        self.AttendenctReportTable.heading("id", text="ID")
        self.AttendenctReportTable.heading("roll", text="Roll")
        self.AttendenctReportTable.heading("name", text="Name")
        self.AttendenctReportTable.heading("department", text="Department")
        self.AttendenctReportTable.heading("time", text="Time")
        self.AttendenctReportTable.heading("date", text="Date")
        self.AttendenctReportTable.heading("attendence", text="Attendence")

        self.AttendenctReportTable["show"] = "headings"

        self.AttendenctReportTable.pack(fill=BOTH, expand=1)
        self.AttendenctReportTable.bind("<ButtonRelease>",self.get_cursor)

        # ----------------------Right Label Frame----------------------

        # -------------------------fetch data-------------------------

    def fetchData(self, rows):
        self.AttendenctReportTable.delete(
            *self.AttendenctReportTable.get_children())
        for i in rows:
            self.AttendenctReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="open csv", filetypes=(
            ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)

            self.fetchData(mydata)

    # -------------------------fetch data-------------------------

    # ------------------------export data------------------------

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "Erroe", "No Data Found", parent=self.root)
                return False
            messagebox.showwarning(
                "Success", "Plase set file extension as .csv while saving you file", parent=self.root)
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(
            ), title="open csv", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")))
            with open(fln, "w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                    messagebox.showinfo("Success", "Your Data exported to " +
                                        os.path.basename(fln)+" successfully", parent=self.root)

        except Exception as es:
            messagebox.showerror(
                "Error", f"Due To :{str(es)}", parent=self.root)
    # ------------------------export data------------------------

    # ------------------get cursor------------------
    def get_cursor(self,event):
        cursor_row=self.AttendenctReportTable.focus()
        content=self.AttendenctReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendence.set(rows[6])



    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")






if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()
