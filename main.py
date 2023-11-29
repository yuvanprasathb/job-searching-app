from tkinter import*

tk=Tk()
tk.geometry("925x500")
tk.resizable(False,False)
tk.title("Hire Me Hub")
tk.config(bg="white")

        
            

img=PhotoImage(file="images\\Mobile Marketing-rafiki.png")
Label(tk,image=img,bg="white").place(x=20,y=10)
frame=Frame(tk,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text="Sign In",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=100,y=5)

#------------------------------------username-------------------------------

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
    #------------------------------------Button----------------------------------
Button(frame,width=39,pady=7,text="Sign In",bg="#57a1f8",fg="white",font=("Franklin Gothic Medium",11),border=0).place(x=25,y=204)

    #----------------------------------------------------------------------------

label=Label(frame,text="Dont Have An Account?",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
label.place(x=90,y=270)

sign_up=Button(frame,width=6,text="Sign Up",border=0,bg="white",cursor="hand2",fg="#57a1f8")
sign_up.place(x=230,y=270)

tk.mainloop()
