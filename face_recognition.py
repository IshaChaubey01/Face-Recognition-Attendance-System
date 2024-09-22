from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1330x600+0+0")
        self.root.title("Face Recognition Attendance System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30, "bold"), bg="blue", fg="white")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        # 1st image
        img_top = Image.open(r"D:\Users\tools\Downloads\download.jpeg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # 2nd image
        img_bottom = Image.open(r"D:\Users\tools\Downloads\download.jpeg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Button for face recognition
        b1_1 = Button(f_lbl, text="FACE RECOGNITION", cursor="hand2", font=("times new roman", 12, "bold"), bg="red", fg="white", command=self.face_recog)
        b1_1.place(x=250, y=520, width=200, height=50)

    # -----------------face recognition-------------------
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                
                # Correct handling of predict tuple
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Student_Name FROM student WHERE `Student Id`=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(map(str, n)) if n else "Unknown"

                my_cursor.execute("SELECT Department FROM student WHERE `Student Id`=" + str(id))
                m = my_cursor.fetchone()
                m = "+".join(map(str, m)) if m else "Unknown"

                my_cursor.execute("SELECT `Roll no` FROM student WHERE `Student Id`=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(map(str, r)) if r else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"Roll no: {r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Student_Name: {n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {m}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)  # 0 for laptop camera, use 1 for external camera

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognition", img)

            if cv2.waitKey(1) == 27:  # Press 'Enter' to break
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()




        



if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()