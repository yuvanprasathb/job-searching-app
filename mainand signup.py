from tkinter import*
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import string

tk=Tk()
tk.geometry("925x500")
tk.resizable(False,False)
tk.title("Hire Me Hub")
tk.config(bg="white")

#############################################################################################################################################################################################

"""                                                                     MAIN      PAGE                                                                                                                """

############################################################################################################################################################################################

def main_page():
    
    root=Toplevel(tk)
    root.geometry("1540x780")
    root.title("Hire Me Hub - Home")
    root.resizable(False,False)

    icon=PhotoImage(file="images\\Handshake.png")
    root.iconphoto(False,icon)
#___________________________________________________________________________________________________________________________________________________________________________________________

#                                                                         DATA BASE    
#____________________________________________________________________________________________________________________________________________________________________________________________

    username=user.get()
    pass1=password.get()

    mysqldb = mysql.connector.connect(host="localhost",user="root",passwd="6379120712",database="hiremehub")
    mycursor=mysqldb.cursor()
    u=(username,)
    

    sql="SELECT password FROM info where username = %s"
    mycursor.execute(sql,u)

    myresult = mycursor.fetchone()

    check_pass=list(myresult)
    print(check_pass)
    checkpass1=[pass1]
    print(checkpass1)
    if (checkpass1==check_pass):


#___________________________________________________________________________________________________________________________________________________________________________________________

#                                                                           TOP FRAME
#____________________________________________________________________________________________________________________________________________________________________________________________



    

        def on_enter(e):
                    search.delete(0,"end")
        def on_leave(e):
                name=search.get()
                if name=="":
                    search.insert(0,"Search")

        frametop=Frame(root,bg="white",width=1540,border=0,height=60,pady=6)
        frametop.place(y=30)

        imgtop=PhotoImage(file="images\\Handshake.png")
        Label(frametop,image=imgtop,bg="white").place(x=50)

        search=Entry(frametop,bg="white",width=25,border=1,font=("Microsoft Yahei UI Light",15))
        search.insert(0,"Search")
        search.place(x=120,y=7)

        search.bind('<FocusIn>',on_enter)
        search.bind('<FocusOut>',on_leave)

        imghome=PhotoImage(file="images\\Home.png")
        Label(frametop,image=imghome,bg="white").place(x=500)
        hometext=Label(frametop,text="Home",font=("arial",11),bg="white",fg="black")
        hometext.place(x=495,y=32)


        imgpeople=PhotoImage(file="images\\People.png")
        Label(frametop,image=imgpeople,bg="white").place(x=590)
        peopletext=Label(frametop,text="Connections",font=("arial",11),bg="white",fg="black")
        peopletext.place(x=560,y=32)

        imgjob=PhotoImage(file="images\\Briefcase.png")
        Label(frametop,image=imgjob,bg="white").place(x=660)
        jobtext=Label(frametop,text="Jobs",font=("arial",11),bg="white",fg="black")
        jobtext.place(x=660,y=32)


        imgmsg=PhotoImage(file="images\\Chat Bubble.png")
        Label(frametop,image=imgmsg,bg="white").place(x=740)
        msgtext=Label(frametop,text="Messages",font=("arial",11),bg="white",fg="black")
        msgtext.place(x=720,y=32)


        imgnot=PhotoImage(file="images\\notifi.png")
        Label(frametop,image=imgnot,bg="white").place(x=830)
        nottext=Label(frametop,text="Notifications",font=("arial",11),bg="white",fg="black")
        nottext.place(x=810,y=32)


#___________________________________________________________________________________________________________________________________________________________________________________________

#                                                                        FRAME   LEFT
#____________________________________________________________________________________________________________________________________________________________________________________________
 

        frameleft=Frame(root,bg="white",width=250,height=450,border=0)
        frameleft.place(x=40,y=120)

        profile=PhotoImage(file="images\\icons8-customer-100.png")
        Label(frameleft,image=profile,border=0,bg="white").place(x=75,y=20)

        profilename=Label(frameleft,text="YUVAN PRASATH B",font=("arial",15),bg="white",fg="black")
        profilename.place(x=35,y=120)

        Frame(frameleft,width=295,height=1,bg="black").place(x=0,y=160)

        connections=Label(frameleft,text="Connections",font=("arial",13,"bold"),fg="#dcdde1",bg="white")
        connections.place(x=10,y=170)

        connections=Label(frameleft,text="Connect with alumni",font=("arial",11),fg="black",bg="white")
        connections.place(x=10,y=195)

        alumni=PhotoImage(file="images\\icons8-add-administrator-50 (1).png")
        Button(frameleft,image=alumni,border=0,bg="white").place(x=200,y=185)

        Frame(frameleft,width=295,height=1,bg="black").place(x=0,y=230)

        premium=Label(frameleft,text="Access exclusive tools&insights",font=("arial",13),fg="#dcdde1",bg="white")
        premium.place(x=10,y=240)

        premiumtxt=Label(frameleft,text="Try Premium for free",font=("arial",11),fg="black",bg="white")
        premiumtxt.place(x=40,y=265)

        premiumimg=PhotoImage(file="images\\premium.png")
        Label(frameleft,image=premiumimg,border=0,bg="white").place(x=10,y=265)

        Frame(frameleft,width=295,height=1,bg="black").place(x=0,y=300)

        myitems=Label(frameleft,text="My Items",font=("arial",11),fg="black",bg="white")
        myitems.place(x=40,y=310)

        myitemsimg=PhotoImage(file="images\\Bookmark.png")
        Label(frameleft,image=myitemsimg,border=0,bg="white").place(x=10,y=310)

        Frame(frameleft,width=295,height=1,bg="black").place(x=0,y=340)

        groupstxt=Label(frameleft,text="Groups",font=("arial",11),fg="#0097e6",bg="white")
        groupstxt.place(x=10,y=350)

        eventstxt=Label(frameleft,text="Events",font=("arial",11),fg="#0097e6",bg="white")
        eventstxt.place(x=10,y=380)

        followedhashtxt=Label(frameleft,text="Followed Hashtags",font=("arial",11),fg="#0097e6",bg="white")
        followedhashtxt.place(x=10,y=410)

        add=PhotoImage(file="images\\Add.png")
        Button(frameleft,image=add,border=0,bg="white").place(x=200,y=380)

#___________________________________________________________________________________________________________________________________________________________________________________________

#                                                                           LEFT DOWN FRAME
#____________________________________________________________________________________________________________________________________________________________________________________________

        frameleftdown=Frame(root,bg="white",width=250,height=150,border=0)
        frameleftdown.place(x=40,y=600)



#___________________________________________________________________________________________________________________________________________________________________________________________

#                                                                           CENTER TOP FRAME
#____________________________________________________________________________________________________________________________________________________________________________________________


        def on_enter(e):
                    postbar.delete(0,"end")
        def on_leave(e):
                name=postbar.get()
                if name=="":
                    postbar.insert(0,"Start a post")

        framectop=Frame(root,width=570,height=100,bg="white")
        framectop.place(x=320,y=120)

        profilephoto_ctop=PhotoImage(file="images\\icons8-customer-100 (1).png")
        Label(framectop,image=profilephoto_ctop,bg="white").place(x=10,y=0)

        postbar=Entry(framectop,bg="white",width=40,border=1,font=("Microsoft Yahei UI Light",15))
        postbar.insert(0,"Start a post")
        postbar.place(x=100,y=10)
        postbar.bind('<FocusIn>',on_enter)
        postbar.bind('<FocusOut>',on_leave)

        photoimg=PhotoImage(file="images\\photo.png")
        Label(framectop,bg="white",image=photoimg).place(x=40,y=60)
        phototxt=Button(framectop,text="Images",border=0,font=("arial",13),fg="black",bg="white")
        phototxt.place(x=70,y=65)

        videoimg=PhotoImage(file="images\\Video.png")
        Label(framectop,bg="white",image=videoimg).place(x=180,y=60)
        videotxt=Button(framectop,text="Videos",border=0,font=("arial",13),fg="black",bg="white")
        videotxt.place(x=210,y=65)

        eventimg=PhotoImage(file="images\\events.png")
        Label(framectop,bg="white",image=eventimg).place(x=320,y=60)
        eventtxt=Button(framectop,text="Events",border=0,font=("arial",13),fg="black",bg="white")
        eventtxt.place(x=350,y=65)

        articleimg=PhotoImage(file="images\\article.png")
        Label(framectop,bg="white",image=articleimg).place(x=450,y=60)
        articletxt=Button(framectop,text="Article",border=0,font=("arial",13),fg="black",bg="white")
        articletxt.place(x=480,y=65)

#___________________________________________________________________________________________________________________________________________________________________________________________

#                                                                           RIGHT FRAME
#____________________________________________________________________________________________________________________________________________________________________________________________

        framecleft=Frame(root,width=580,height=630,bg="#00a8ff")
        framecleft.place(x=920,y=120)

        notificationheaing=Label(framecleft,text="NOTIFICATIONS",font=("arial",20,"bold"),fg="white",bg="#00a8ff").place(x=200,y=30)

        Frame(framecleft,width=580,height=1,bg="black").place(x=0,y=80)

        Button(framecleft,text="All",bg="white",fg="black",width=10,font=("arial",11),border=1).place(x=30,y=100)

        Button(framecleft,text="My posts",bg="#7f8fa6",fg="black",width=10,font=("arial",11),border=1).place(x=150,y=100)

        Button(framecleft,text="Mentions",bg="#7f8fa6",fg="black",width=10,font=("arial",11),border=1).place(x=270,y=100)

        spotlightimg=PhotoImage(file="images\\Spotlight.png")
        Label(framecleft,bg="white",image=spotlightimg).place(x=30,y=160)
        l1=Label(framecleft,text='''What's driving today's youth to opt for entrepreneurship?
This expect shares his take.''',textalign=w,font=("arial",13),fg="black",bg="#00a8ff").place(x=70,y=170)


#___________________________________________________________________________________________________________________________________________________________________________________________

#                                                                           CENTER DOWN FRAME
#____________________________________________________________________________________________________________________________________________________________________________________________


        framecdown=Frame(root,width=570,height=500,bg="white")
        framecdown.place(x=320,y=250)
        
        Label(framecdown,text="Recommended for you",font=("Arial",20,"bold"),bg="white",fg="black").place(x=10,y=20)
        Label(framecdown,text="Based on your profile and search history",font=("Microsoft Yahei UI Light",15),bg="white",fg="#dcdde1").place(x=10,y=50)

        infosysimg=PhotoImage(file="images\\infosys.png")
        Label(framecdown,image=infosysimg,bg="white").place(x=30,y=100)

        infosyspos=Label(framecdown,text="Frontend Developer",font=("Arial",15,"bold"),bg="white",fg="black").place(x=150,y=95)
        infosysdate=Label(framecdown,text="Chennai, India · 2 days ago",font=("Microsoft Yahei UI Light",12),bg="white",fg="#dcdde1").place(x=150,y=120)

        Frame(framecdown,width=570,height=1,bg="black").place(x=0,y=160)

        zohoimg=PhotoImage(file="images\\zoho.png")
        Label(framecdown,image=zohoimg,bg="white").place(x=30,y=190)

        zohopos=Label(framecdown,text="Frontend Developer (WFH)",font=("Arial",15,"bold"),bg="white",fg="black").place(x=150,y=180)
        zohodate=Label(framecdown,text="Trichy, India · 5 days ago",font=("Microsoft Yahei UI Light",12),bg="white",fg="#dcdde1").place(x=150,y=205)

        Frame(framecdown,width=570,height=1,bg="black").place(x=0,y=250)

        tcsimg=PhotoImage(file="images\\tcs.png")
        Label(framecdown,image=tcsimg,bg="white").place(x=30,y=280)

        tcspos=Label(framecdown,text="Frontend Developer (WFH)",font=("Arial",15,"bold"),bg="white",fg="black").place(x=150,y=270)
        tcsdate=Label(framecdown,text="Trichy, India · 5 days ago",font=("Microsoft Yahei UI Light",12),bg="white",fg="#dcdde1").place(x=150,y=295)

    else:
        root.destroy()
        messagebox.showwarning("showwarning","Username or Password is Wrong")
        



    root.mainloop()





        
#############################################################################################################################################################################################

"""                                                                     SIGN UP      PAGE                                                                                                                """

############################################################################################################################################################################################            

def signup():
    
    
    root=Toplevel(tk)
    
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

    def data():

#___________________________________________________________________________________________________________________________________________________________________________________________

#                                                                           DATA BASE
#____________________________________________________________________________________________________________________________________________________________________________________________
        username=user.get()
        pass1=password.get()
        c_pass=confirm_password.get()
        mysqldb = mysql.connector.connect(host="localhost",user="root",passwd="6379120712",database="hiremehub")
        mycursor=mysqldb.cursor()
        mycursor.execute("SELECT username FROM info")
        myresult = mycursor.fetchall()
        checkuser=[]
        for x in myresult:
            checkuser=list(x)+checkuser
        check_user_entered=username
        print(checkuser)
        print(check_user_entered)
        if check_user_entered in checkuser:
            messagebox.showwarning("showwarning", "Username already taken")
            
            

        

        if(pass1==c_pass and ("@" in pass1 or "#" in pass1 or "$" in pass1 or "&" in pass1 or "!" in pass1 )):

        
            
                sql = "insert into info (username,password) values(%s,%s)"
                data = (username, pass1)
                mycursor.execute(sql, data)
                mysqldb.commit()
                messagebox.showinfo("showinfo", "Account Created")
                print("data saved")

        else:
                messagebox.showwarning("showwarning", "Use a Strong Password")
                
#___________________________________________________________________________________________________________________________________________________________________________________________

#                                                                                   USER NAME
#____________________________________________________________________________________________________________________________________________________________________________________________
        

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


    Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)


#___________________________________________________________________________________________________________________________________________________________________________________________

#                                                                                   PASSWORD
#____________________________________________________________________________________________________________________________________________________________________________________________
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

    Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

#___________________________________________________________________________________________________________________________________________________________________________________________

#                                                                               CONFIRM PASSWORD
#____________________________________________________________________________________________________________________________________________________________________________________________
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
    Button(frame,width=39,pady=7,text="Sign Up",command=data,bg="#57a1f8",fg="white",font=("Franklin Gothic Medium",11),border=0).place(x=25,y=274)

    #----------------------------------------------------------------------------

    label=Label(frame,text="I Already Have An Account",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
    label.place(x=90,y=330)

    sign_in=Button(frame,width=6,text="Sign In",border=0,bg="white",cursor="hand2",fg="#57a1f8")
    sign_in.place(x=250,y=330)

    root.mainloop()


    
############################################################################################################################################################################################

""""                                                                              SIGN IN PAGE                                                                                           """

############################################################################################################################################################################################    
    
img=PhotoImage(file="images\\Mobile Marketing-rafiki.png")
Label(tk,image=img,bg="white").place(x=20,y=10)

frame=Frame(tk,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text="Sign In",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=100,y=5)

#___________________________________________________________________________________________________________________________________________________________________________________________

#                                                                                   USERNAME
#____________________________________________________________________________________________________________________________________________________________________________________________

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


Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

#___________________________________________________________________________________________________________________________________________________________________________________________

#                                                                                   PASSWORD
#____________________________________________________________________________________________________________________________________________________________________________________________

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
Button(frame,width=39,pady=7,text="Sign In",bg="#57a1f8",fg="white",font=("Franklin Gothic Medium",11),command=main_page,border=0).place(x=25,y=204)

    #----------------------------------------------------------------------------

label=Label(frame,text="Dont Have An Account?",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
label.place(x=90,y=270)

sign_up=Button(frame,width=6,text="Sign Up",border=0,bg="white",command=signup,cursor="hand2",fg="#57a1f8")
sign_up.place(x=230,y=270)






tk.mainloop()
