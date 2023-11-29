from tkinter import*
import ast

root=Tk()
root.title("Hire Me Hub")
root.geometry("925x500")
root.configure(bg="white")
root.resizable(False,False)


img= PhotoImage(file="images\\Connected world-rafiki.png")
Label(root,image=img,border=0,bg="white").place(x=10,y=10)

frame=Frame(root,width=350,height=390,bg="white")
frame.place(x=480,y=50)

heading=Label(frame,text="Sign Up",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
heading.place(x=120,y=5)

#-----------------------------------------------------------------------------
def on_enter(e):
            user.delete(0,"end")
def on_leave(e):
        name=user.get()
        if name=="":
            user.insert(0,"Username")

user=Entry(frame,width=25,fg="black",bd=0,bg="white",font=("Microsoft YaHei UI Light",11))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

#---------------------------------------------------------------------------
Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
#------------------------------------password-------------------------------

def on_enter(e):
    password.delete(0,"end")
def on_leave(e):
    name=password.get()
    if name=="":
        password.insert(0,"Password")               
password=Entry(frame,width=25,fg="black",bd=0,bg="white",font=("Microsoft YaHei UI Light",11))
password.place(x=30,y=150)
password.insert(0,"Password")
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>',on_leave)
#----------------------------------------------------------------------------
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
#----------------------------------------------------------------------------
def on_enter(e):
            confirm_password.delete(0,"end")
def on_leave(e):
        name=confirm_password.get()
        if name=="":
            confirm_password.insert(0,"Confirm Password")

confirm_password=Entry(frame,width=25,fg="black",bd=0,bg="white",font=("Microsoft YaHei UI Light",11))
confirm_password.place(x=30,y=220)
confirm_password.insert(0,"Confirm Password")
confirm_password.bind('<FocusIn>',on_enter)
confirm_password.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=247)

#------------------------------------Button----------------------------------
Button(frame,width=39,pady=7,text="Sign Up",command="signin",bg="#57a1f8",fg="white",font=("Franklin Gothic Medium",11),border=0).place(x=25,y=274)

#----------------------------------------------------------------------------

label=Label(frame,text="I Already Have An Account",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
label.place(x=90,y=330)

sign_in=Button(frame,width=6,text="Sign In",command=signin,border=0,bg="white",cursor="hand2",fg="#57a1f8")
sign_in.place(x=250,y=330)

root.mainloop()
