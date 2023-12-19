from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Motel Reservation System")
        self.root.geometry("1295x550+230+220")
        

        #Variable
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name= StringVar()
        self.var_first_name= StringVar()   
        self.var_last_name= StringVar()   
        self.var_gender= StringVar()   
        self.var_mobile= StringVar()   
        self.var_email= StringVar()   
        self.var_natinality=StringVar()
        self.var_idproof=StringVar()
        self.var_id_number=StringVar()
        self.var_address= StringVar()   
        self.var_postcode= StringVar()     
      

        #Title
        lb1_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lb1_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = Image.open("/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/logo.jpg")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbimage = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbimage.place(x=5, y=2, width=100, height=40)

        #LabelFrame
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman", 16, "bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        # labes snd entries

        lbl_cust_ref = Label(labelframeleft,text="Customer Referance",font=("times new roman", 14, "bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref= ttk.Entry(labelframeleft,textvariable=self.var_ref,font=("times new roman", 15, "bold"),width=29,state="readonly")
        enty_ref.grid(row=0,column=1)


        #Customer First Name
        cfname = Label(labelframeleft,text="First Name",font=("times new roman", 14, "bold"),padx=2,pady=6)
        cfname.grid(row=1,column=0,sticky=W)

        txtcfname= ttk.Entry(labelframeleft,textvariable=self.var_first_name,font=("times new roman", 15, "bold"),width=29)
        txtcfname.grid(row=1,column=1)

        #Customer Last Name
        clname = Label(labelframeleft,text="Last Name",font=("times new roman", 14, "bold"),padx=2,pady=6)
        clname.grid(row=2,column=0,sticky=W)

        txtclname= ttk.Entry(labelframeleft,textvariable=self.var_last_name,font=("times new roman", 15, "bold"),width=29)
        txtclname.grid(row=2,column=1)

        #gender
        lbl_gender = Label(labelframeleft,font=("times new roman", 14, "bold"),text="Gender:",padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("times new roman", 15, "bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #Mobile number
        lblmobile = Label(labelframeleft,text="Mobile:",font=("times new roman", 14, "bold"),padx=2,pady=6)
        lblmobile.grid(row=4,column=0,sticky=W)

        txtmobile= ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("times new roman", 15, "bold"),width=29)
        txtmobile.grid(row=4,column=1)

        #Email
        lblmobile = Label(labelframeleft,text="Email:",font=("times new roman", 14, "bold"),padx=2,pady=6)
        lblmobile.grid(row=5,column=0,sticky=W)

        txtmobile= ttk.Entry(labelframeleft,textvariable=self.var_email,font=("times new roman", 15, "bold"),width=29)
        txtmobile.grid(row=5,column=1)


        #address

        lblmobile = Label(labelframeleft,text="Address:",font=("times new roman", 14, "bold"),padx=2,pady=6)
        lblmobile.grid(row=6,column=0,sticky=W)

        txtmobile= ttk.Entry(labelframeleft,textvariable=self.var_address,font=("times new roman", 15, "bold"),width=29)
        txtmobile.grid(row=6,column=1)

        #postcode

        lblPostCode = Label(labelframeleft,text="Postcode:",font=("times new roman", 14, "bold"),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)

        txtPostCode= ttk.Entry(labelframeleft,textvariable=self.var_postcode,font=("times new roman", 15, "bold"),width=29)
        txtPostCode.grid(row=7,column=1)

        #Nationality

        lbl_nationality = Label(labelframeleft,font=("times new roman", 14, "bold"),text="Nationality:",padx=2,pady=6)
        lbl_nationality.grid(row=8,column=0,sticky=W)

        combo_natinality=ttk.Combobox(labelframeleft,textvariable=self.var_natinality,font=("times new roman", 15, "bold"),width=27,state="readonly")
        combo_natinality["value"]=("Indian","American","British","Other")
        combo_natinality.current(0)
        combo_natinality.grid(row=8,column=1)

        #ID_proof
        lbl_idproof = Label(labelframeleft,font=("times new roman", 14, "bold"),text="ID Proof:",padx=2,pady=6)
        lbl_idproof.grid(row=9,column=0,sticky=W)

        combo_idproof=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("times new roman", 15, "bold"),width=27,state="readonly")
        combo_idproof["value"]=("Passport","Driving License","State Id")
        combo_idproof.current(0)
        combo_idproof.grid(row=9,column=1)

        #idnumber

        lblidnumber = Label(labelframeleft,text="ID Number:",font=("times new roman", 14, "bold"),padx=2,pady=6)
        lblidnumber.grid(row=10,column=0,sticky=W)

        txtidnumber= ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=("times new roman", 15, "bold"),width=29)
        txtidnumber.grid(row=10,column=1)


        #Buttons

        btn_frame= Frame(labelframeleft,bd = 2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnadd=Button(btn_frame,text="ADD",command=self.add_data,font=("times new roman", 14, "bold"),bg="black",fg="gold",width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="UPDATE",command=self.update,font=("times new roman", 14, "bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="DELETE",command=self.delete_data,font=("times new roman", 14, "bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="RESET",command=self.reset_data,font=("times new roman", 14, "bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)


    #Table Frame Search system
        table_frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman", 16, "bold"),padx=2,)
        table_frame.place(x=435,y=50,width=860,height=490)

        lblsearchby = Label(table_frame,text="Search By:",font=("times new roman", 15, "bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("times new roman", 15, "bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtsearch= ttk.Entry(table_frame,textvariable=self.txt_search,font=("times new roman", 15, "bold"),width=24)
        txtsearch.grid(row=0,column=2,padx=2)

        btnsearch=Button(table_frame,text="SEARCH",command=self.serach,font=("times new roman", 14, "bold"),bg="black",fg="gold",width=9)
        btnsearch.grid(row=0,column=3,padx=1)

        btnshowall=Button(table_frame,text="SHOWALL",command=self.fetch_data,font=("times new roman", 14, "bold"),bg="black",fg="gold",width=9)
        btnshowall.grid(row=0,column=4,padx=1)

        #Show data table

        details_table= Frame(table_frame,bd = 2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_Details_Table=ttk.Treeview(details_table,columns=("ref","firstname","lastname","gender","mobile","email","address","postcode","nationality","idproof","idnumber"),
                                             xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_Details_Table.xview)
        scroll_y.config(command=self.cust_Details_Table.yview)

        self.cust_Details_Table.heading("ref",text="Refer No")
        self.cust_Details_Table.heading("firstname",text="First Name")
        self.cust_Details_Table.heading("lastname",text="Last Name")
        self.cust_Details_Table.heading("gender",text="Gender")
        self.cust_Details_Table.heading("mobile",text="Mobile")
        self.cust_Details_Table.heading("email",text="Email")
        self.cust_Details_Table.heading("address",text="Address")
        self.cust_Details_Table.heading("postcode",text="Postcode")
        self.cust_Details_Table.heading("nationality",text="Nationality")
        self.cust_Details_Table.heading("idproof",text="IdProof")
        self.cust_Details_Table.heading("idnumber",text="IDNumber")

        self.cust_Details_Table["show"]="headings"

        self.cust_Details_Table.column("ref",width=100)
        self.cust_Details_Table.column("firstname",width=100)
        self.cust_Details_Table.column("lastname",width=100)
        self.cust_Details_Table.column("gender",width=100)
        self.cust_Details_Table.column("mobile",width=100)
        self.cust_Details_Table.column("email",width=100)
        self.cust_Details_Table.column("address",width=100)
        self.cust_Details_Table.column("postcode",width=100)
        self.cust_Details_Table.column("nationality",width=100)
        self.cust_Details_Table.column("idproof",width=100)
        self.cust_Details_Table.column("idnumber",width=100)

        self.cust_Details_Table.pack(fill=BOTH,expand=1)
        self.cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()== "" or self.var_last_name.get() == "":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif len(self.var_mobile.get()) != 10:
            messagebox.showerror("Error", "Mobile number should be 10 digits", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO customer (Ref, firstname, lastname, gender, mobile, email, address, postcode, nationality, idproof, idnumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                                                                                            self.var_ref.get(),
                                                                                                                                            self.var_first_name.get(),
                                                                                                                                            self.var_last_name.get(),
                                                                                                                                            self.var_gender.get(),
                                                                                                                                            self.var_mobile.get(),
                                                                                                                                            self.var_email.get(),
                                                                                                                                            self.var_address.get(),
                                                                                                                                            self.var_postcode.get(),
                                                                                                                                            self.var_natinality.get(),
                                                                                                                                            self.var_idproof.get(),
                                                                                                                                            self.var_id_number.get()
                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning", f"Something went wrong: {str(e)}", parent=self.root)
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows= my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
            for i in rows:
                self.cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row= self.cust_Details_Table.focus()
        content=self.cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_first_name.set(row[1]),
        self.var_last_name.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_mobile.set(row[4]),
        self.var_email.set(row[5]),
        self.var_address.set(row[6]),
        self.var_postcode.set(row[7])
        self.var_natinality.set(row[8]),
        self.var_idproof.set(row[9]),
        self.var_id_number.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set firstname=%s,lastname=%s,gender=%s,mobile=%s,email=%s,address=%s,postcode=%s,nationality=%s,idproof=%s,idnumber=%s where Ref=%s",(       
                                                                                                                        self.var_first_name.get(),
                                                                                                                        self.var_last_name.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_mobile.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_postcode.get(),
                                                                                                                        self.var_natinality.get(),
                                                                                                                        self.var_idproof.get(),
                                                                                                                        self.var_id_number.get(),
                                                                                                                        self.var_ref.get(),         
                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","Coustomer details has been updated successfully.",parent=self.root)
        
    def delete_data(self):
        mdelete=messagebox.askyesno("Motel Reservation System","Do you want to delete this customer?",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_data(self):
        #self.var_ref.set(""),
        self.var_first_name.set(""),
        self.var_last_name.set(""),
        #self.var_gender.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_address.set(""),
        self.var_postcode.set("") 
        #self.var_natinality.set(""),
        #self.var_idproof.set(""),
        self.var_id_number.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def serach(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
            for i in rows:
                self.cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()

