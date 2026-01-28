def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd
    from tkinter import ttk 
    from PIL import Image , ImageTk  


    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("Predict")
    root.configure(background="deeppink4")
    
    
   
    SourcePort = tk.IntVar()
    DestinationPort = tk.IntVar()
    Protocol = tk.StringVar()
    PacketLength = tk.IntVar()
    PacketType = tk.StringVar()
    TrafficType = tk.StringVar()
    Alerts_Warnings = tk.StringVar()
    SeverityLevel= tk.StringVar()
    LogSource = tk.StringVar()
    
    
    #===================================================================================================================
    def Detect():
        e1=SourcePort.get()
        print(e1)
        e2=DestinationPort.get()
        print(e2)
        e3=Protocol.get()
        print(e3)
        if e3=='UDP':
            e3=0
        elif e3=='ICMP':
            e3=1
        else:
            e3=2
        #print(type(e3))
        e4=PacketLength.get()
        print(e4)
        e5=PacketType.get()
        print(e5)
        if e5=='Control':
            e5=0
        else:
            e5=1
        e25=TrafficType.get()
        print(e5)
        if e25=='HTTP':
            e25=0
        elif e25=='DNS':
            e25=1
        else:
            e25=2
        e6=Alerts_Warnings.get()
        print(e6)
        if e6=='Alert Triggered':
            e6=0

        e7=SeverityLevel.get()
        print(e7)
        if e7=='High':
            e7=0
        elif e7=='Medium':
            e7=1
        else:
            e7=2
        e8=LogSource.get()
        print(e8)
        if e8=='Firewall':
            e8=0
        else:
            e8=1

        

        
        
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load('training_MODELr.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5,e25, e6, e7, e8]])
        print(v)
        if v[0]==0:
            print("DDoS")
            yes = tk.Label(root,text="DDoS Attack Detect",background="red",foreground="white",font=('times', 20, ' bold '),width=25)
            yes.place(x=600,y=570)
                     
        elif v[0]==1:
            print("Intrusion")
            no = tk.Label(root, text="Intrusion Attack Detect", background="red", foreground="white",font=('times', 20, ' bold '),width=25)
            no.place(x=600, y=570)
        else:
            print("Malware")
            no = tk.Label(root, text="Malware Attack Detect", background="red", foreground="white",font=('times', 20, ' bold '),width=25)
            no.place(x=600, y=570)

        
            
    #####For background Image
    image2 = Image.open('11.jpg')
    image2 = image2.resize((w,h), Image.LANCZOS)
    
    background_image = ImageTk.PhotoImage(image2)
    
    background_label = tk.Label(root, image=background_image)
    
    background_label.image = background_image
    
    background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
    
            
            
    #########################################################################################
         
    frame_alpr = tk.LabelFrame(root, text=" --Form-- ", width=800, height=700, bd=5, font=('times', 14, ' bold '),fg="white",bg="#812dd2")
    frame_alpr.grid(row=0, column=0, sticky='nw')
    frame_alpr.place(x=400, y=10)
    image_frame = Image.open('12.jpg')
    image_frame = image_frame.resize((800, 700), Image.LANCZOS)
    frame_background_image = ImageTk.PhotoImage(image_frame)
    background_label_frame = tk.Label(frame_alpr, image=frame_background_image)
    background_label_frame.image = frame_background_image
    background_label_frame.place(x=0, y=0)
       
    
    l=tk.Label(root, text="Cyber attack detection", font="ar 15 bold",bg="#812dd2")
    l.place(x=700,y=30)
    
    
    l1=tk.Label(frame_alpr,text="SourcePort",background="black",fg="orange",font=('times', 20, ' bold '),width=15)
    l1.place(x=50,y=30)
    tele_device=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=SourcePort)
    tele_device.place(x=550,y=30)

    l2=tk.Label(frame_alpr,text="DestinationPort",background="black",fg="orange",font=('times', 20, ' bold '),width=15)
    l2.place(x=50,y=80)
    tele_subscriber=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=DestinationPort)
    tele_subscriber.place(x=550,y=80)

    l3=tk.Label(frame_alpr,text="Protocol",background="black",fg="orange",font=('times', 20, ' bold '),width=15)
    l3.place(x=50,y=130)
    #abort=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Protocol)
    #abort.place(x=650,y=130)
    monthchoosen = ttk.Combobox(frame_alpr, width = 27, textvariable = Protocol)
    # Adding combobox drop down list
    monthchoosen['values'] = ('UDP',
                            'ICMP',
                            'TCP')
    monthchoosen.place(x=550,y=130)
    #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()
    
    l4=tk.Label(frame_alpr,text="PacketLength",background="black",fg="orange",font=('times', 20, ' bold '),width=15)
    l4.place(x=50,y=180)
    sendsms=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=PacketLength)
    sendsms.place(x=550,y=180)

    l5=tk.Label(frame_alpr,text="PacketType",background="black",fg="orange",font=('times', 20, ' bold '),width=15)
    l5.place(x=50,y=230)
    #delete_pack=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=PacketType)
    #delete_pack.place(x=650,y=230)
    monthchoosen = ttk.Combobox(frame_alpr, width = 27, textvariable = PacketType)
    # Adding combobox drop down list
    monthchoosen['values'] = ('Control',
                            'Data',
                        )
    monthchoosen.place(x=550,y=230)
    #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()

    l6=tk.Label(frame_alpr,text="TrafficType",background="black",fg="orange",font=('times', 20, ' bold '),width=15)
    l6.place(x=50,y=280)
    #phone_s=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=TrafficType)
    #phone_s.place(x=650,y=280)
    monthchoosen = ttk.Combobox(frame_alpr, width = 27, textvariable = TrafficType)
    # Adding combobox drop down list
    monthchoosen['values'] = ('HTTP',
                            'DNS',
                            'FTP'
                        )
    monthchoosen.place(x=550,y=280)
    #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()

    l7=tk.Label(frame_alpr,text="Alerts_Warnings",background="black",fg="orange",font=('times', 20, ' bold '),width=15)
    l7.place(x=50,y=330)
    #sms_received=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Alerts_Warnings)
    #sms_received.place(x=650,y=330)
    monthchoosen = ttk.Combobox(frame_alpr, width = 27, textvariable = Alerts_Warnings)
    # Adding combobox drop down list
    monthchoosen['values'] = ('Alert Triggered',
                            
                        )
    monthchoosen.place(x=550,y=330)
    #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()

    l8=tk.Label(frame_alpr,text="SeverityLevel",background="black",fg="orange",font=('times', 20, ' bold '),width=15)
    l8.place(x=50,y=380)
    #ljava=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=SeverityLevel)
    #ljava.place(x=650,y=380)
    monthchoosen = ttk.Combobox(frame_alpr, width = 27, textvariable = SeverityLevel)
    # Adding combobox drop down list
    monthchoosen['values'] = ('High',
                              'Medium',
                              'Low'
                            
                        )
    monthchoosen.place(x=550,y=380)
    #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()

    l9=tk.Label(frame_alpr,text="LogSource",background="black",fg="orange",font=('times', 20, ' bold '),width=15)
    l9.place(x=50,y=430)
    #readsms=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=LogSource)
    #readsms.place(x=650,y=430)
    monthchoosen = ttk.Combobox(frame_alpr, width = 27, textvariable = LogSource)
    # Adding combobox drop down list
    monthchoosen['values'] = ('Firewall',
                              'Server',
                             
                            
                        )
    monthchoosen.place(x=550,y=430)
    #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()

    
    
    button1 = tk.Button(frame_alpr,text="Submit",command=Detect,background="red",font=('times', 20, ' bold '),width=10)
    button1.place(x=300,y=600)


    root.mainloop()

Train()