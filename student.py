from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1330x600+0+0")
        self.root.title("Face Recognition Attendance System")

        # -------------Variables---------------------
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()

        # 1st image
        img = Image.open(r"D:\Users\tools\Downloads\download.jpeg")
        img = img.resize((1200, 100), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1500, height=100)

        # bg image
        img3 = Image.open(r"D:\Users\tools\Downloads\download.jpeg")
        img3 = img3.resize((1500, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1500, height=710)

        # heading
        title_lbl = Label(bg_img, text="Student Management System", font=("times new roman", 30, "bold"), bg="blue", fg="white")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        main_frame = Frame(bg_img, bd=2, bg=("lightblue"))
        main_frame.place(x=20, y=50, width=1480, height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=650, height=600)

        img_left = Image.open(r"D:\Users\tools\Downloads\download.jpeg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=630, height=100)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=680, y=10, width=640, height=580)

        img_right = Image.open(r"C:\Users\Tomato\Downloads\pexels-olly-3762800.jpg")
        img_right = img_right.resize((720, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=630, height=100)

        # current course
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="White", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=650, height=150)

         # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department","Arts","Computer", "IT", "Medical", "Commerce", "Science")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "BE", "BCA", "BA", "Bcom", "Bsc")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="readonly")
        semester_combo["values"] = ("1", "2", "3", "4", "5", "6", "7", "8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student info
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=250, width=720, height=300)

        # student id
        studentId_label = Label(class_student_frame, text="Student Id:", font=("times new roman", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_student_frame, textvariable=self.var_id, width=20, font=("times new roman", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # dob
        dob_label = Label(class_student_frame, text="DOB:", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)


        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)


        # student name
        studentName_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_name, width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Roll no
        rollno_label = Label(class_student_frame, text="Roll no.:", font=("times new roman", 12, "bold"), bg="white")
        rollno_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)


        rollno_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        rollno_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly")
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # phone no
        phone_label = Label(class_student_frame, text="Phone no:", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # address
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)


        # radio Buttons
        self.var_radio = StringVar()

    
        radionbtn1=ttk.Radiobutton(class_student_frame, text="Take Photo Sample", value="Yes")
        radionbtn1.grid(row=6,column=0)

        radionbtn2=ttk.Radiobutton(class_student_frame, text="No Photo Sample", value="No")
        radionbtn2.grid(row=6,column=1)

       

        # Button Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=210, width=715, height=35)

        add_btn = Button(btn_frame, text="Save", command=self.add_data, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=17)
        add_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=17)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=17)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=17)
        reset_btn.grid(row=0, column=3)

        # Right side table frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=100, width=630, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "roll", "gender", "dob", "phone", "address", "email"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("roll", text="Roll no")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone no")
        self.student_table.heading("address", text="Address")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
    #------------------Function declaration-----------
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_dob.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get() 
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)

    # Fetch Data from Database
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Get Cursor Function (to select data from table to input fields)
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_dob.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])
        self.var_address.set(data[11])

    # Update Data
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognition")
                    my_cursor = conn.cursor()

                    query = """UPDATE student 
                            SET Department=%s, Course=%s, Year=%s, Semester=%s, Student_Name=%s, DOB=%s, 
                            `Roll no`=%s, Gender=%s, Email=%s, `Phone no`=%s, Address=%s 
                            WHERE `Student Id`=%s"""
                    values = (self.var_dep.get(), self.var_course.get(), self.var_year.get(),
                            self.var_semester.get(), self.var_name.get(), self.var_dob.get(),
                            self.var_roll.get(), self.var_gender.get(), self.var_email.get(),
                            self.var_phone.get(), self.var_address.get(), self.var_id.get())
                
                    print("Executing query:", query)
                    print("With values:", values)
                
                    my_cursor.execute(query, values)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
                print(f"Full error: {es}")

    
    # Delete Data
    # Delete Data
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student Id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student's details?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognition")
                    my_cursor = conn.cursor()
                
                    # Corrected SQL query: use backticks instead of single quotes
                    sql = "DELETE FROM student WHERE `Student Id`=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                
                    conn.commit()  # Commit only if deletion is confirmed
                    self.fetch_data()  # Refresh the table or data view
                    conn.close()  # Close the connection
                
                    messagebox.showinfo("Delete", "Student details deleted successfully", parent=self.root)
                else:
                    if not delete:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)




    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Female")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()



