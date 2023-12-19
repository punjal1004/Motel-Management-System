from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
from hotel import MotelReservationSystem

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1600x900+0+0")

        
        self.bg=ImageTk.PhotoImage(file="/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/new4.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=170,width=340,height=450)

        img1=Image.open("/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/lg.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbimg = Label(frame, image=self.photoimage1, bg="black", borderwidth=0)
        lbimg.pack(side=TOP, pady=20)  

        login_lbl=Label(frame,text="LOGIN HERE",font=("times new roman",20,"bold"),fg="white",bg="black")
        login_lbl.place(x=80,y=100)

        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=150)

        self.user_entry=ttk.Entry(frame,font=("times new roman",15))
        self.user_entry.place(x=40,y=180,width=270)

        pass1=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        pass1.place(x=70,y=225)

        self.pass_entry=ttk.Entry(frame,font=("times new roman",15), show="*")
        self.pass_entry.place(x=40,y=250,width=270)

        
        img2=Image.open("/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/icon.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbimg = Label(frame,image=self.photoimage2, bg="black", borderwidth=0)
        lbimg.place(x=40, y=150, width=25, height=25)
    
        img3=Image.open("/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/lock-512.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbimg = Label(frame,image=self.photoimage3, bg="black", borderwidth=0)
        lbimg.place(x=40, y=225, width=25, height=25)

        btn = Button(frame,command=self.login, text="Login",font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="dark red")
        btn.place(x=110,y=300,width=120,height=35) 

        regibtn = Button(frame, text="New User Register",command=self.register_window, font=("times new roman", 10, "bold"),borderwidth=0, fg="white", bg="black")
        regibtn.place(x=15,y=350,width=160) 

        forpassbtn = Button(frame, text="Forgot Password",command=self.forgot_password_window, font=("times new roman", 10, "bold"),borderwidth=0, fg="white", bg="black")
        forpassbtn.place(x=10,y=370,width=160) 



    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)



    def login(self):
        if self.user_entry.get().strip()=="" or self.pass_entry.get().strip()=="":
            messagebox.showerror("Error","All feilds required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Punju@345", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(self.user_entry.get(), self.pass_entry.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username or password")
            else:
                messagebox.showinfo("Info","Successfully logged in!")
                self.root.destroy()  # Close the login window
                # Open Motel Reservation System window
                self.open_main_window()
                  ################################################################  #self.new_window=Toplevel(self.new_window)
                    #call here project self.app= 2:16:00
    def open_main_window(self):
        main_root = Tk()
        motel_system = MotelReservationSystem(main_root)
        main_root.mainloop()

    def reset_pass(self):
        if self.list_qus.get()=="Select":
            messagebox.showerror("Error","Select the security qus",parent=self.root2)
        elif self.ans_entry.get()=="":
            messagebox.showerror("Error","Please enter security ans",parent=self.root2)
        elif self.newpass_entry.get()=="":
            messagebox.showerror("Error","Please enter new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Punju@345", database="mydata")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.user_entry.get(),self.list_qus.get(),self.ans_entry.get())
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct ans",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.newpass_entry.get(),self.user_entry.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your pass has been reset",parent=self.root2)
                self.root2.destroy()

    def forgot_password_window(self):
        if self.user_entry.get()=="":
            messagebox.showerror("Error","Please enter Email to reset password") 
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Punju@345", database="mydata")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.user_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter your registerd email id")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                
                security_qus=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_qus.place(x=50,y=80)
                self.list_qus=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.list_qus["values"]=("Select","Your Birth Palce","Your pet Name","Yours First School Name","Your Mother's Last name")
                self.list_qus.place(x=50,y=110,width=250)
                self.list_qus.current(0)


                security_ans=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_ans.place(x=50,y=150)

                self.ans_entry=ttk.Entry(self.root2,font=("times new roman",15))
                self.ans_entry.place(x=50,y=180,width=250)

                new_pass=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_pass.place(x=50,y=220)

                self.newpass_entry=ttk.Entry(self.root2,font=("times new roman",15))
                self.newpass_entry.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)

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
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)
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
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",bg="white")
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
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        elif self.var_pass.get().strip() != self.var_confpass.get().strip():
            messagebox.showerror("Error", "Confirm password and password must be match",parent=self.root)
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
                messagebox.showerror("Error", "User already exists",parent=self.root)
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
        
    def return_login(self):
        self.root.destroy()
if __name__=="__main__":
    main()
