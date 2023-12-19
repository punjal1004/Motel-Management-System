from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        self.bg=ImageTk.PhotoImage(file="/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/new2.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        self.bg1=ImageTk.PhotoImage(file="/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/new3.jpg")
        bg1_lbl=Label(self.root,image=self.bg1)
        bg1_lbl.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        f_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        f_entry.place(x=50,y=130,width=250)      

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)   

        self.l_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.l_entry.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.c_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.c_entry.place(x=50,y=200,width=250)  
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)  

        self.e_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.e_entry.place(x=370,y=200,width=250)

        security_qus=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_qus.place(x=50,y=240)
        self.list_qus=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.list_qus["values"]=("Select","Your Birth Palce","Your pet Name","Yours First School Name","Your Mother's Last name")
        self.list_qus.place(x=50,y=270,width=250)
        self.list_qus.current(0)


        security_ans=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_ans.place(x=370,y=240)

        self.ans_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.ans_entry.place(x=370,y=270,width=250)

        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.pswd_entry = ttk.Entry(frame, textvariable=self.var_pass,font=("times new roman", 15), show="*")  # Hide the password
        self.pswd_entry.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.cpswd_entry = ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15), show="*")  # Hide the confirm password
        self.cpswd_entry.place(x=370, y=340, width=250)

        show_password_cb = Checkbutton(frame, text="Show Password", font=("times new roman", 12, "bold"), bg="white", fg="black", command=self.show_password)
        show_password_cb.place(x=50, y=380)

        img=Image.open("/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/register-now-button1.jpg")
        img = img.resize((200, 50), Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=10,y=420,width=200)

        img1=Image.open("/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/loginpng.png")
        img1 = img1.resize((200, 50), Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=330,y=420,width=200)

    def show_password(self):
        if self.pswd_entry["show"] == "*":
            self.pswd_entry["show"] = ""
            self.cpswd_entry["show"] = ""
        else:
            self.pswd_entry["show"] = "*"
            self.cpswd_entry["show"] = "*"

    def register_data(self):
        if (
            self.var_fname.get().strip() == ""
            or self.var_lname.get().strip() == ""
            or self.var_contact.get().strip() == ""
            or self.var_email.get().strip() == ""
            or self.var_securityQ.get().strip() == "Select"
            or self.var_securityA.get().strip() == ""
            or self.var_pass.get().strip() == ""
            or self.var_confpass.get().strip() == ""
        ):
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get().strip() != self.var_confpass.get().strip():
            messagebox.showerror("Error", "Confirm password and password must be match")
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="Punju@345", database="mydata"
            )
            my_cursor = conn.cursor()
            lemail = self.var_email.get().strip().lower()
            query = "SELECT * FROM register WHERE email = %s"
            value = (lemail,)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User already exists")
            else:
                insert_query = "INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                insert_values = (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get(),
                )
            my_cursor.execute(insert_query, insert_values)

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered successfully!!")

                
if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()

