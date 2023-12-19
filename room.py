from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from time import strptime
from datetime import datetime

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Motel Reservation System")
        self.root.geometry("1295x550+230+220")

        #variable
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailabel=StringVar()
        self.var_meal=StringVar()
        self.var_nooofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        #Title
        lb1_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lb1_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = Image.open("/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/logo.jpg")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbimage = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbimage.place(x=5, y=2, width=100, height=40)

        #LabelFrame
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new roman", 16, "bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        # labes snd entries

        lbl_cust_contact = Label(labelframeleft,text="Customer Contact",font=("times new roman", 14, "bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_Contact= ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("times new roman", 15, "bold"),width=25)
        enty_Contact.grid(row=0,column=1,sticky=W)

        #Fetch data Button

        btnfetchdata=Button(labelframeleft,text="GET DATA",command=self.Fetch_cotact,font=("times new roman", 10, "bold"),bg="black",fg="gold",width=7)
        btnfetchdata.place(x=347,y=4)

        # Check_in Date

        check_in_date = Label(labelframeleft,text="Check_in Date:",font=("times new roman", 14, "bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date= ttk.Entry(labelframeleft,textvariable=self.var_checkin,font=("times new roman", 15, "bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        # Check_out Date

        check_out_date = Label(labelframeleft,text="Check_out Date:",font=("times new roman", 14, "bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)

        txtcheck_out_date= ttk.Entry(labelframeleft,textvariable=self.var_checkout,font=("times new roman", 15, "bold"),width=29)
        txtcheck_out_date.grid(row=2,column=1)

        # Room Type

        room_type = Label(labelframeleft,text="Room Type:",font=("times new roman", 14, "bold"),padx=2,pady=6)
        room_type.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select `Room Type` from details")
        ide= my_cursor.fetchall()

        combo_room_type=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("times new roman", 15, "bold"),width=27,state="readonly")
        combo_room_type["value"]= ide
        combo_room_type.current(0)
        combo_room_type.grid(row=3,column=1)

        # Available room

        room_ava= Label(labelframeleft,text="Available Room:",font=("times new roman", 14, "bold"),padx=2,pady=6)
        room_ava.grid(row=4,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows= my_cursor.fetchall()

        combo_room_no=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailabel,font=("times new roman", 15, "bold"),width=27,state="readonly")
        combo_room_no["value"]= rows
        combo_room_no.current(0)
        combo_room_no.grid(row=4,column=1)

        #Meal

        lb_meal= Label(labelframeleft,text="Meal:",font=("times new roman", 14, "bold"),padx=2,pady=6)
        lb_meal.grid(row=5,column=0,sticky=W)

        txt_lb_meal= ttk.Entry(labelframeleft,textvariable=self.var_meal,font=("times new roman", 15, "bold"),width=29)
        txt_lb_meal.grid(row=5,column=1)

        #No of days

        lb_days= Label(labelframeleft,text="No  of Days:",font=("times new roman", 14, "bold"),padx=2,pady=6)
        lb_days.grid(row=6,column=0,sticky=W)

        txt_lb_days= ttk.Entry(labelframeleft,textvariable=self.var_nooofdays,font=("times new roman", 15, "bold"),width=29)
        txt_lb_days.grid(row=6,column=1)

        #Paid Tax

        lbl_paid_tax= Label(labelframeleft,text="Paid tax:",font=("times new roman", 14, "bold"),padx=2,pady=6)
        lbl_paid_tax.grid(row=7,column=0,sticky=W)

        txt_paid_tax= ttk.Entry(labelframeleft,textvariable=self.var_paidtax,font=("times new roman", 15, "bold"),width=29)
        txt_paid_tax.grid(row=7,column=1)

        #Sub Total

        lbl_sub_total= Label(labelframeleft,text="Sub Total:",font=("times new roman", 14, "bold"),padx=2,pady=6)
        lbl_sub_total.grid(row=8,column=0,sticky=W)

        txt_sub_total= ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,font=("times new roman", 15, "bold"),width=29)
        txt_sub_total.grid(row=8,column=1)

        #Total Cost

        lbl_total_cost= Label(labelframeleft,text="Total Cost:",font=("times new roman", 14, "bold"),padx=2,pady=6)
        lbl_total_cost.grid(row=9,column=0,sticky=W)

        txt_total_cost= ttk.Entry(labelframeleft,textvariable=self.var_total,font=("times new roman", 15, "bold"),width=29)
        txt_total_cost.grid(row=9,column=1)

        #Bill Button
        btnbill=Button(labelframeleft,text="BILL",command=self.total,font=("times new roman", 14, "bold"),bg="black",fg="gold",width=9)
        btnbill.grid(row=10,column=0,padx=1,sticky=W)

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

        #Rightside Image
        img3 = Image.open("/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/bed.jpg")
        img3 = img3.resize((540,230), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbimage = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lbimage.place(x=750, y=55, width=540, height=230)

        #Table Frame Search system
        table_frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman", 16, "bold"),padx=2,)
        table_frame.place(x=435,y=280,width=860,height=260)

        lblsearchby = Label(table_frame,text="Search By:",font=("times new roman", 15, "bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("times new roman", 15, "bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","Room")
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
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","roomavailable","meal","noofdays"),
                                             xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check_in Date")
        self.room_table.heading("checkout",text="Check_out Date")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="No Of Days")

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #ADD Room data
    def add_data(self):
        if self.var_contact.get()== "" or self.var_checkin.get() == "":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values (%s, %s, %s, %s, %s, %s, %s)", (
                                                                            self.var_contact.get(),
                                                                            self.var_checkin.get(),
                                                                            self.var_checkout.get(),
                                                                            self.var_roomtype.get(),
                                                                            self.var_roomavailabel.get(),
                                                                            self.var_meal.get(),
                                                                            self.var_nooofdays.get()
                                                                        ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning", f"Something went wrong: {str(e)}", parent=self.root)
    
    #Fetch Room data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows= my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_row= self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailabel.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_nooofdays.set(row[6])

    #Update room data
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE room SET checkin=%s, checkout=%s, roomtype=%s, roomavailable=%s, meal=%s, noofdays=%s WHERE contact=%s", (
                                                                                                        self.var_checkin.get(),
                                                                                                        self.var_checkout.get(),
                                                                                                        self.var_roomtype.get(),
                                                                                                        self.var_roomavailabel.get(),
                                                                                                        self.var_meal.get(),
                                                                                                        self.var_nooofdays.get(),
                                                                                                        self.var_contact.get()
                                                                                                    ))


            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","Room details has been updated successfully.",parent=self.root)
    
    #delete room data
    def delete_data(self):
        mdelete=messagebox.askyesno("Motel Reservation System","Do you want to delete this room?",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #reset room data
    def reset_data(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailabel.set(""),
        self.var_meal.set(""),
        self.var_nooofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
    

    #All data fetch
    def Fetch_cotact(self):
        if self.var_contact.get() == "" :
            messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
        else:
            #name
            conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
            my_cursor=conn.cursor()
            query=("select firstname from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","This number is not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=290,height=180)

                lblName=Label(showDataframe,text="Name:",font=("times new roman",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lbl.place(x=90,y=0)

                lblName=Label(showDataframe,text="Name:",font=("times new roman",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lbl.place(x=90,y=0)

                #Gender
                conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
                my_cursor=conn.cursor()
                query=("select gender from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgender=Label(showDataframe,text="Gender:",font=("times new roman",12,"bold"))
                lblgender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lbl2.place(x=90,y=30)

                #Email
                conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
                my_cursor=conn.cursor()
                query=("select email from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgender=Label(showDataframe,text="Email:",font=("times new roman",12,"bold"))
                lblgender.place(x=0,y=60)

                lbl2=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lbl2.place(x=90,y=60)

                #Nationality
                conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
                my_cursor=conn.cursor()
                query=("select nationality from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgender=Label(showDataframe,text="Nationality:",font=("times new roman",12,"bold"))
                lblgender.place(x=0,y=90)

                lbl2=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lbl2.place(x=90,y=90)

                #Address
                conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
                my_cursor=conn.cursor()
                query=("select address from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgender=Label(showDataframe,text="Address:",font=("times new roman",12,"bold"))
                lblgender.place(x=0,y=120)

                lbl2=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lbl2.place(x=90,y=120)

    #Serach system for room 
    def serach(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #Billing system for room
    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%m/%d/%Y")
        outDate = datetime.strptime(outDate, "%m/%d/%Y")
        self.var_nooofdays.set(abs(outDate - inDate).days)

        if self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Single":
            q1 = float(50)
            q2 = float(150)
            q3 = float(self.var_nooofdays.get())  # Convert to float
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "$" + str("%.2f" % ((q5)* 0.1))
            ST = "$" + str("%.2f" % ((q5)))
            TT = "$" + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
       
        elif self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single":
            q1 = float(100)
            q2 = float(150)
            q3 = float(self.var_nooofdays.get())  # Convert to float
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "$" + str("%.2f" % ((q5)* 0.1))
            ST = "$" + str("%.2f" % ((q5)))
            TT = "$" + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
        elif self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single":
            q1 = float(100)
            q2 = float(150)
            q3 = float(self.var_nooofdays.get())  # Convert to float
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "$" + str("%.2f" % ((q5)* 0.1))
            ST = "$" + str("%.2f" % ((q5)))
            TT = "$" + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == "Berakfast" and self.var_roomtype.get() == "Double":
            q1 = float(50)
            q2 = float(250)
            q3 = float(self.var_nooofdays.get())  # Convert to float
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "$" + str("%.2f" % ((q5)* 0.1))
            ST = "$" + str("%.2f" % ((q5)))
            TT = "$" + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Double":
            q1 = float(100)
            q2 = float(250)
            q3 = float(self.var_nooofdays.get())  # Convert to float
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "$" + str("%.2f" % ((q5)* 0.1))
            ST = "$" + str("%.2f" % ((q5)))
            TT = "$" + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double":
            q1 = float(100)
            q2 = float(250)
            q3 = float(self.var_nooofdays.get())  # Convert to float
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "$" + str("%.2f" % ((q5)* 0.1))
            ST = "$" + str("%.2f" % ((q5)))
            TT = "$" + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == "Berakfast" and self.var_roomtype.get() == "Business Suits":
            q1 = float(50)
            q2 = float(700)
            q3 = float(self.var_nooofdays.get())  # Convert to float
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "$" + str("%.2f" % ((q5)* 0.1))
            ST = "$" + str("%.2f" % ((q5)))
            TT = "$" + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Business Suits":
            q1 = float(100)
            q2 = float(700)
            q3 = float(self.var_nooofdays.get())  # Convert to float
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "$" + str("%.2f" % ((q5)* 0.1))
            ST = "$" + str("%.2f" % ((q5)))
            TT = "$" + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Business Suits":
            q1 = float(100)
            q2 = float(700)
            q3 = float(self.var_nooofdays.get())  # Convert to float
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "$" + str("%.2f" % ((q5)* 0.1))
            ST = "$" + str("%.2f" % ((q5)))
            TT = "$" + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()