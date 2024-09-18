from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from PIL import Image
from student import Student


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1330x600+0+0")
        self.root.title("Face recognition attendance system")

        img=Image.open(r"C:\Users\Tomato\Downloads\WhatsApp Image 2024-09-03 at 13.26.09_60519afb.jpg")
        img = img.resize((1200,100), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1500,height=100)

        #bg image
        img3=Image.open(r"C:\Users\Tomato\Downloads\bg2.jpg")
        img3 = img3.resize((1500, 710), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1500,height=710)

        #heading
        title_lbl=Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",30,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        #Student button
        img4=Image.open(r"C:\Users\Tomato\Downloads\face pic.jpeg")
        img4 = img4.resize((180, 100), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=180,height=100)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=200,width=180,height=40)

        # face detecetion button 
        img5=Image.open(r"C:\Users\Tomato\Downloads\face pic.jpeg")
        img5 = img5.resize((180, 100), Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=450,y=100,width=180,height=100)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=200,width=180,height=40)

        #Attendance button
        img6=Image.open(r"C:\Users\Tomato\Downloads\face pic.jpeg")
        img6 = img6.resize((180, 100), Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=700,y=100,width=180,height=100)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=200,width=180,height=40)

        # Help desk button
        img7=Image.open(r"C:\Users\Tomato\Downloads\face pic.jpeg")
        img7 = img7.resize((180, 100), Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=950,y=100,width=180,height=100)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=950,y=200,width=180,height=40)


        # Train Face button
        img8=Image.open(r"C:\Users\Tomato\Downloads\face pic.jpeg")
        img8 = img8.resize((180, 100), Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=350,width=180,height=100)

        b1_1=Button(bg_img,text="Train Face",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=450,width=180,height=40)

        # photos button
        img9=Image.open(r"C:\Users\Tomato\Downloads\face pic.jpeg")
        img9 = img9.resize((180, 100), Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=450,y=350,width=180,height=100)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=450,width=180,height=40)

        # Developer button
        img10=Image.open(r"C:\Users\Tomato\Downloads\face pic.jpeg")
        img10 = img10.resize((180, 100), Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=700,y=350,width=180,height=100)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=450,width=180,height=40)

        # Exit button
        img11=Image.open(r"C:\Users\Tomato\Downloads\face pic.jpeg")
        img11 = img11.resize((180, 100), Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=950,y=350,width=180,height=100)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=950,y=450,width=180,height=40)

    # -------------Function Button--------------

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)










if __name__  == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()