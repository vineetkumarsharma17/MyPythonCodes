from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1000x500+80+80")
        #===========variable=========
        self.uname=StringVar()
        self.pass_=StringVar()
        #==============All Images=============
        self.bg_icon=ImageTk.PhotoImage(file="images/bg.jpg")
        self.user_icon=ImageTk.PhotoImage(file="images/user.png")
        self.pass_icon=ImageTk.PhotoImage(file="images/pas.png")
        self.logo_icon=ImageTk.PhotoImage(file="images/logo.png")
        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        title=Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg="yellow",fg="red",relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=300,y=80)

        logolbl=Label(Login_Frame,image=self.logo_icon,bd=0)
        logolbl.grid(row=0,column=0,columnspan=2,pady=20)

        lbluser=Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"))
        lbluser.grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame,textvariable=self.uname,bd=5,relief=GROOVE)
        txtuser.grid(row=1,column=1,padx=20)

        lblpass=Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"))
        lblpass.grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(Login_Frame,textvariable=self.pass_,bd=5,relief=GROOVE).grid(row=2,column=1,padx=20)

        btn_log=Button(Login_Frame,text="Login",width=15,font=("times new roman",20,"bold"),bg="yellow",fg="red")
        btn_log.grid(row=3,column=0,columnspan=2,pady=10)
    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error All field are required")







root=Tk()
obj=Login_System(root)
root.mainloop()
