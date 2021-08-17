from tkinter import * 
from tkinter import font 
from tkinter import ttk
from PIL import Image,ImageTk
import os


from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("Face Recognition System")

        # ---------------------------image1---------------------------
        img1 = Image.open(r"college_images\img1.jfif")
        img1 = img1.resize((500, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        # showing to the window
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=400, height=150)
        # ---------------------------image1---------------------------

        # ---------------------------image2---------------------------
        img2 = Image.open(r"college_images\img2.jfif")
        img2 = img2.resize((500, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        # showing to the window
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=400, y=0, width=400, height=150)
        # ---------------------------image2---------------------------

        # ---------------------------image3---------------------------
        img3 = Image.open(r"college_images\img3.jfif")
        img3 = img3.resize((500, 150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        # showing to the window
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=800, y=0, width=400, height=150)
        # ---------------------------image3---------------------------



        # -----------------------Background image-----------------------
        background_root = Image.open(r"college_images\background_root.jfif")
        background_root = background_root.resize((1200, 450), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(background_root)
        # showing to the window
        bg_root_lbl = Label(self.root, image=self.photoimg4)
        bg_root_lbl.place(x=0, y=150, width=1200, height=450)

        # --------------------------Root Title--------------------------
        title_lbl = Label(bg_root_lbl, text="Face Recognition And Attendence System",  font=(
            'times new roman', 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1200, height=45)
        # --------------------------Root Title--------------------------

        # -----------------------Background image-----------------------

        


        #---------------Root Image Buttons For Navigation---------------


        #----------------------Student Button----------------------
        student_img_btn = Image.open(r"college_images\student_img_btn.png")
        student_img_btn = student_img_btn.resize((100, 100), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(student_img_btn)

        b1 = Button(bg_root_lbl, image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200, y=100, width=100, height=100)

        b1_1 = Button(bg_root_lbl, text="Student Details",command=self.student_details,
                     cursor="hand2")
        b1_1.place(x=200, y=200, width=100, height=30)
        #----------------------Student Button----------------------
        
        #----------------------Detect Face Button----------------------
        detect_face_img_btn = Image.open(r"college_images\detect_face_img_btn.png")
        detect_face_img_btn = detect_face_img_btn.resize((100, 100), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(detect_face_img_btn)

        b2 = Button(bg_root_lbl, command=self.face_data   ,image=self.photoimg6, cursor="hand2")
        b2.place(x=400, y=100, width=100, height=100)

        b2_1 = Button(bg_root_lbl, command=self.face_data ,text="Detect Face" , cursor="hand2")
        b2_1.place(x=400, y=200, width=100, height=30)
        #----------------------Detect Face Button----------------------


        #----------------------Attendence Button----------------------
        attendence_img_btn = Image.open(r"college_images\attendence_img_btn.jfif")
        attendence_img_btn = attendence_img_btn.resize((100, 100), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(attendence_img_btn)

        b3 = Button(bg_root_lbl,command=self.attendenct_data, image=self.photoimg7, cursor="hand2")
        b3.place(x=600, y=100, width=100, height=100)

        b3_1 = Button(bg_root_lbl,command=self.attendenct_data,text="Attendence" , cursor="hand2")
        b3_1.place(x=600, y=200, width=100, height=30)
        #----------------------Attendence Button----------------------


        #----------------------Help Button----------------------
        help_img_btn = Image.open(r"college_images\help_img_btn.jfif")
        help_img_btn = help_img_btn.resize((100, 100), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(help_img_btn)

        b4 = Button(bg_root_lbl, image=self.photoimg8, cursor="hand2")
        b4.place(x=800, y=100, width=100, height=100)

        b4_1 = Button(bg_root_lbl,text="Help Desk" , cursor="hand2")
        b4_1.place(x=800, y=200, width=100, height=30)
        #----------------------Help Button----------------------

        
        #----------------------Train Button----------------------
        train_img_btn = Image.open(r"college_images\train_img_btn.png")
        train_img_btn = train_img_btn.resize((100, 100), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(train_img_btn)

        b5 = Button(bg_root_lbl,command=self.train_data, image=self.photoimg9, cursor="hand2")
        b5.place(x=200, y=250, width=100, height=100)

        b5_1 = Button(bg_root_lbl,command=self.train_data,text="Train AI" , cursor="hand2")
        b5_1.place(x=200, y=350, width=100, height=30)
        #----------------------Train Button----------------------


        #----------------------Photos Button----------------------
        photo_img_btn = Image.open(r"college_images\photo_img_btn.png")
        photo_img_btn = photo_img_btn.resize((100, 100), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(photo_img_btn)

        b6 = Button(bg_root_lbl, image=self.photoimg10, cursor="hand2",command=self.open_img)
        b6.place(x=400, y=250, width=100, height=100)

        b6_1 = Button(bg_root_lbl,text="Photos" , cursor="hand2",command=self.open_img)
        b6_1.place(x=400, y=350, width=100, height=30)
        #----------------------Photos Button----------------------


        #----------------------Developer Button----------------------
        developer_img_btn = Image.open(r"college_images\developer_img_btn.png")
        developer_img_btn = developer_img_btn.resize((100, 100), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(developer_img_btn)

        b7 = Button(bg_root_lbl, image=self.photoimg11,command=self.developer_data, cursor="hand2")
        b7.place(x=600, y=250, width=100, height=100)

        b7_1 = Button(bg_root_lbl,text="Developer" ,command=self.developer_data, cursor="hand2")
        b7_1.place(x=600, y=350, width=100, height=30)
        #----------------------Developer Button----------------------


        #----------------------Exit Button----------------------
        exit_img_btn = Image.open(r"college_images\exit_img_btn.png")
        exit_img_btn = exit_img_btn.resize((100, 100), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(exit_img_btn)

        b7 = Button(bg_root_lbl, image=self.photoimg12, cursor="hand2")
        b7.place(x=800, y=250, width=100, height=100)

        b7_1 = Button(bg_root_lbl,text="Developer" , cursor="hand2")
        b7_1.place(x=800, y=350, width=100, height=30)
        #----------------------Exit Button----------------------

    # -----------------------------show img-----------------------------
    def open_img(self):
        os.startfile("data")

    # -----------------------------show img-----------------------------


        # -----------------------Function Buttons-----------------------

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

        # -----------------------Function Buttons-----------------------

        # -----------------------Function Buttons-----------------------

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

        # -----------------------Function Buttons-----------------------

        # -----------------------Function Buttons-----------------------

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

        # -----------------------Function Buttons-----------------------

        # -----------------------Function Buttons-----------------------

    def attendenct_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)

        # -----------------------Function Buttons-----------------------
        # -----------------------Function Buttons-----------------------

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

        # -----------------------Function Buttons-----------------------



        #---------------Root Image Button For Navigation---------------





if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
