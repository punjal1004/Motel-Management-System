from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from time import strptime
from datetime import datetime

class RoomDetails:
    def __init__(self, root):
        self.root = root
        self.root.title("Motel Reservation System")
        self.root.geometry("1295x550+230+220")

        #Title
        lb1_title = Label(self.root, text="ROOM DETAILS", font=("times new roman", 18, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lb1_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = Image.open("/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/logo.jpg")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbimage = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbimage.place(x=5, y=2, width=100, height=40)

        #LabelFrame
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman", 16, "bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=520,height=350)

        # labes snd entries
        #Floor
        lbl_floor = Label(labelframeleft,text="Floor",font=("times new roman", 14, "bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        enty_floor= ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("times new roman", 15, "bold"),width=25)
        enty_floor.grid(row=0,column=1,sticky=W)

        #Room No
        lbl_RoomNo = Label(labelframeleft,text="Room No",font=("times new roman", 14, "bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_Roomno=StringVar()
        enty_RoomNo= ttk.Entry(labelframeleft,textvariable= self.var_Roomno,font=("times new roman", 15, "bold"),width=25)
        enty_RoomNo.grid(row=1,column=1,sticky=W)

        #Room Type
        lbl_RoomType = Label(labelframeleft,text="Room Type",font=("times new roman", 14, "bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_Roomtype=StringVar()
        enty_RoomType= ttk.Entry(labelframeleft,textvariable=self.var_Roomtype,font=("times new roman", 15, "bold"),width=25)
        enty_RoomType.grid(row=2,column=1,sticky=W)

        #Buttons

        btn_frame= Frame(labelframeleft,bd = 2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnadd=Button(btn_frame,text="ADD",command=self.add_data,font=("times new roman", 14, "bold"),bg="black",fg="gold",width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="UPDATE",command=self.update,font=("times new roman", 14, "bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="DELETE",command=self.delete_data,font=("times new roman", 14, "bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="RESET",command=self.reset_data,font=("times new roman", 14, "bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)

        #Table Frame
        table_frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman", 16, "bold"),padx=2,)
        table_frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(table_frame,columns=("floor","roomno","roomType"),
                                             xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomType",text="Room Type")

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #ADD Room data
    def add_data(self):
        if self.var_floor.get()== "" or self.var_Roomtype.get() == "":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values (%s, %s, %s)", (
                                                                            self.var_floor.get(),
                                                                            self.var_Roomno.get(),
                                                                            self.var_Roomtype.get()
                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning", f"Something went wrong: {str(e)}", parent=self.root)

    #Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0]),
        self.var_Roomno.set(row[1]),
        self.var_Roomtype.set(row[2])
    #Update room data
    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "Please enter Floor number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Punju@345", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE details SET floor=%s, `Room Type`=%s WHERE RoomNo=%s", (
                self.var_floor.get(),
                self.var_Roomtype.get(),
                self.var_Roomno.get()
            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update", "Room details have been updated successfully.", parent=self.root)

    #delete room data
    def delete_data(self):
        mdelete=messagebox.askyesno("Motel Reservation System","Do you want to delete this room?",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Punju@345",database="mydata")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_Roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #reset room data
    def reset_data(self):
        self.var_floor.set(""),
        self.var_Roomno.set(""),
        self.var_Roomtype.set("")
    
if __name__ == "__main__":
    root = Tk()
    obj = RoomDetails(root)
    root.mainloop()