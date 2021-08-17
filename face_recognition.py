from posixpath import split
from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
from mysql.connector import cursor
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Face Recognition System")


        # --------------------------Root Title--------------------------
        title_lbl = Label(self.root, text="Face Recognition",  font=(
            'times new roman', 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1200, height=45)
        # --------------------------Root Title--------------------------


        #----------------------recognize Button----------------------
        b1_1 = Button(self.root, text="Start Face Recognizer",command=self.face_recog , 
                      cursor="hand2", font=(
                          'times new roman', 35, "bold"), bg="gray", fg="green")
        b1_1.place(x=200, y=300, width=800, height=50)
        #----------------------recognize Button----------------------

# ------------------------------attendence------------------------------
    def mark_attendence(self,i,r,n,d):
        with open("Attendence/attendence.csv","r+",newline="\n")as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n},{d},{dtString},{d1}, Present")

# ------------------------------attendence------------------------------



# ----------------------------face recognise----------------------------
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1 - predict/300)))

                conn = mysql.connector.connect(
                        host="localhost", username="root", password="Saiket#26", database="face_recognizer")
                my_cursor = conn.cursor()


                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute(
                    "select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)


               








                if confidence > 77:
                    cv2.putText(img,f"Id: {i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll: {r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name: {n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department: {d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)

                else:
                    
                    cv2.rectangle(img,(x, y), (x+w, y+h), (0, 0,255), 3)
                    cv2.putText(img, "Unkown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)


                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade, 1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade = cv2.CascadeClassifier("frontal-face-default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        








# ----------------------------face recognise----------------------------








if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
