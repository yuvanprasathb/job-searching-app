from tkinter import*

root=Tk()
root.geometry("925x600")
root.title("Hire Me Hub - Home")
root.resizable(False,False)

icon=PhotoImage(file="images\\Handshake.png")
root.iconphoto(False,icon)

#----------------------------------top frame-----------------------------------------------

def on_enter(e):
            search.delete(0,"end")
def on_leave(e):
        name=search.get()
        if name=="":
            search.insert(0,"Search")

frametop=Frame(root,bg="white",width=1000,border=0,height=60,pady=6)
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

#------------------------------------------------------------------------------------------
#----------------------------------------frame left----------------------------------------------------

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

#------------------------------------------------------------------------------------------------------------------

#--------------------------------frame center top--------------------------------------------------------------

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
phototxt=Label(framectop,text="Images",font=("arial",13),fg="black",bg="white")
phototxt.place(x=70,y=65)

videoimg=PhotoImage(file="images\\Video.png")
Label(framectop,bg="white",image=videoimg).place(x=180,y=60)
videotxt=Label(framectop,text="Videos",font=("arial",13),fg="black",bg="white")
videotxt.place(x=210,y=65)

eventimg=PhotoImage(file="images\\events.png")
Label(framectop,bg="white",image=eventimg).place(x=320,y=60)
eventtxt=Label(framectop,text="Images",font=("arial",13),fg="black",bg="white")
eventtxt.place(x=350,y=65)

articleimg=PhotoImage(file="images\\article.png")
Label(framectop,bg="white",image=articleimg).place(x=450,y=60)
articletxt=Label(framectop,text="Images",font=("arial",13),fg="black",bg="white")
articletxt.place(x=480,y=65)

#-------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------frame center down  -------------------------------------------------------

framecdown=Frame(root,width=560,height=500,bg="white")
framecdown.place(x=320,y=250)


Label(framecdown,text="Recommended for you",font=("Arial",20,"bold"),bg="white",fg="black").place(x=10,y=20)
Label(framecdown,text="Based on your profile and search history",font=("Microsoft Yahei UI Light",15),bg="white",fg="#dcdde1").place(x=10,y=50)

infosysimg=PhotoImage(file="images\\infosys.png")
Label(framecdown,image=infosysimg,bg="white").place(x=30,y=100)

infosyspos=Label(framecdown,text="Frontend Developer",font=("Arial",15,"bold"),bg="white",fg="black").place(x=150,y=95)
infosysdate=Label(framecdown,text="Chennai, India · 2 days ago",font=("Microsoft Yahei UI Light",12),bg="white",fg="#dcdde1").place(x=150,y=120)

Frame(framecdown,width=560,height=1,bg="black").place(x=0,y=160)

zohoimg=PhotoImage(file="images\\zoho.png")
Label(framecdown,image=zohoimg,bg="white").place(x=30,y=190)

zohopos=Label(framecdown,text="Frontend Developer (WFH)",font=("Arial",15,"bold"),bg="white",fg="black").place(x=150,y=180)
zohodate=Label(framecdown,text="Trichy, India · 5 days ago",font=("Microsoft Yahei UI Light",12),bg="white",fg="#dcdde1").place(x=150,y=205)

Frame(framecdown,width=560,height=1,bg="black").place(x=0,y=250)

tcsimg=PhotoImage(file="images\\tcs.png")
Label(framecdown,image=tcsimg,bg="white").place(x=30,y=280)

tcspos=Label(framecdown,text="Frontend Developer (WFH)",font=("Arial",15,"bold"),bg="white",fg="black").place(x=150,y=270)
tcsdate=Label(framecdown,text="Trichy, India · 5 days ago",font=("Microsoft Yahei UI Light",12),bg="white",fg="#dcdde1").place(x=150,y=295)



root.mainloop()


