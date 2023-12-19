from tkinter import*
from PIL import Image, ImageTk
from customer import Cust_Win 
from room import Roombooking
from details import RoomDetails

class MotelReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Motel Reservation System")
        self.root.geometry("1550x800+0+0")

        # 1st image
        img1 = Image.open("/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/h1.jpg")
        img1 = img1.resize((1550, 140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbimage = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lbimage.place(x=0, y=0, width=1550, height=140)

        # Logo
        img2 = Image.open("/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/logo.jpg")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbimage = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbimage.place(x=0, y=0, width=230, height=140)

        # Title
        lb1_title = Label(self.root, text="Motel Reservation System", font=("times new roman", 40, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lb1_title.place(x=0, y=140, width=1550, height=50)

        # Main Frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # Menu
        lb1_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lb1_menu.place(x=0, y=0, width=230)
        
        # Button Frame
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)
        
        cust_btn = Button(btn_frame, text="COUSTOMER", command=self.cust_details,width=27,height=2, font=("times new roman", 14, "bold"),
                  bg="black", fg="gold", bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOM",command=self.room_details,width=27,height=2, font=("times new roman", 14, "bold"),
                  bg="black", fg="gold", bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn = Button(btn_frame, text="DETAILS", command=self.roomdetails,width=27,height=2, font=("times new roman", 14, "bold"),
                  bg="black", fg="gold", bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        
        logout_btn = Button(btn_frame, text="LOGOUT", command=self.logout,width=27,height=2,font=("times new roman", 14, "bold"),
                  bg="black", fg="gold", bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

    # Right side image
        img3 = Image.open("/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/h2.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbimage1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lbimage1.place(x=225, y=0, width=1310, height=590)

    # down Images
        img4 = Image.open("/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/myh.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lbimage1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lbimage1.place(x=0, y=225, width=230, height=210)

        img5 = Image.open("/Users/punjalavadhiya/Desktop/Stevens/SSW 500/Project/Motel-Reservation-System/images/khana.jpg")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lbimage1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lbimage1.place(x=0, y=420, width=230, height=190)


    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app= Cust_Win(self.new_window )
    
    def room_details(self):
        self.new_window = Toplevel(self.root)
        self.app= Roombooking(self.new_window )

    def roomdetails(self):
        self.new_window = Toplevel(self.root)
        self.app= RoomDetails(self.new_window )

    def logout(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = MotelReservationSystem(root)
    root.mainloop()
