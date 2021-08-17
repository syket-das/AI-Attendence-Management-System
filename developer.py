
from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Developer Information")


        # --------------------------Root Title--------------------------
        title_lbl = Label(self.root, text="Developer Information",  font=(
            'times new roman', 35, "bold"), bg="white", fg="lightblue")
        title_lbl.place(x=0, y=0, width=1200, height=45)
        # --------------------------Root Title--------------------------


        # ---------------------------image1---------------------------
        student_img1 = Image.open(r"college_images\edit1.jpg")
        student_img1 = student_img1.resize((400, 400), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(student_img1)
        # showing to the window
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=100, y=100, width=400, height=400)
        # ---------------------------image1---------------------------
        # ---------------------------image2---------------------------
        student_img2 = Image.open(r"college_images\developer_bio.jpg")
        student_img2 = student_img2.resize((400, 400), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(student_img2)
        # showing to the window
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=600, y=100, width=400, height=400)
        # ---------------------------image2---------------------------






if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
