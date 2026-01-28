import tkinter  as tk 
from tkinter import * 


from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()
#root.geometry('500x500')
#root.title("Login Form")


#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("main")
#------------------Frame----------------------



#-------function------------------------

def reg():
    
##### tkinter window ######
    
    print("reg")
    from subprocess import call
    call(["python", "registration.py"])   



def login():
    
##### tkinter window ######
    
    print("log")
    from subprocess import call
    call(["python", "login.py"])   
    


def window():
    root.destroy()

#++++++++++++++++++++++++++++++++++++++++++++
# #####For background Image
image2 =Image.open('img.jpg')
image2 =image2.resize((w,h), Image.LANCZOS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


lbl = tk.Label(root, text="Cyber Attack Detection ", font=('times', 40,' bold '), height=2, width=50,bg="BLACK",fg="white")
lbl.place(x=0, y=0)

framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=400, height=300, bd=10, font=('times', 14, ' bold '),bg="#e2b0a8")
framed.grid(row=0, column=0, sticky='nw')
framed.place(x=100, y=250)
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
button1 = tk.Button(framed, text='Login Now',width=15,height=2,bd=5,bg='#45ba84',font=('times', 15, ' bold '),fg='white',command=login).place(x=100,y=20)
button1 = tk.Button(framed, text='Register',width=15,height=2,bd=5,bg='#45ba84',font=('times', 15, ' bold '),fg='white',command=reg).place(x=100,y=100)
exit = tk.Button(framed, text="Exit", command=window, width=15, height=2, bd=5,font=('times', 15, ' bold '),bg="red",fg="white").place(x=100, y=180)

root.mainloop()
