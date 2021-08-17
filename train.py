from posixpath import split
from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Face Recognition System")


        # --------------------------Root Title--------------------------
        title_lbl = Label(self.root, text="Train Data Set",  font=(
            'times new roman', 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1200, height=45)
        # --------------------------Root Title--------------------------

        #----------------------Train Button----------------------
        b1_1 = Button(self.root, text="Train Data Now",command=self.train_classifier,
                      cursor="hand2", font=(
                          'times new roman', 35, "bold"), bg="gray", fg="blue")
        b1_1.place(x=200, y=300, width=800, height=50)
        #----------------------Train Button----------------------


    def train_classifier(self):
        data_dir=("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training....",imageNp)
            cv2.waitKey(1) == 13
        
        ids = np.array(ids)

        # train classifier and save

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Success","Training Successful...")





if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
