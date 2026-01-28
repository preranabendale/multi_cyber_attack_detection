from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

root = tk.Tk()
root.title("GUI")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

# image2 = Image.open('bg1.jpg')

# image2 = image2.resize((w, h), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)


# background_label = tk.Label(root, image=background_image)
# background_label.image = background_image



# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Malware Predication using ML", font=('times', 35,' bold '), height=1, width=62,bg="violet Red",fg="Black")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++




def Model_Training():
    data = pd.read_csv("cybersecurity_attacks_updated - Copy.csv")
    print(data.head())


    """One Hot Encoding"""

    # le = LabelEncoder()
    # data['SourceIPAddress'] = le.fit_transform(data['SourceIPAddress'])
    # print(data['SourceIPAddress'])

    # data['DestinationIPAddress'] = le.fit_transform(data['DestinationIPAddress'])
    # data['SourcePort'] = le.fit_transform(data['SourcePort'])
    # data['DestinationPort'] = le.fit_transform(data['DestinationPort'])
    # data['Protocol'] = le.fit_transform(data['Protocol'])
    # data['PacketLength'] = le.fit_transform(data['PacketLength'])
    # data['PacketType'] = le.fit_transform(data['PacketType'])
    # data['TrafficType'] = le.fit_transform(data['TrafficType'])
    # data['Alerts_Warnings'] = le.fit_transform(data['Alerts_Warnings'])
    # data['SeverityLevel'] = le.fit_transform(data['SeverityLevel'])
    # data['LogSource'] = le.fit_transform(data['LogSource'])
   
   
    """Feature Selection => Manual"""
    x = data.drop(['SourceIPAddress','DestinationIPAddress','AttackType'], axis=1)
    ##data = data.dropna()
    print(type(x))
    y = data['AttackType']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=1234)

    from sklearn.svm import SVC
    from sklearn.ensemble import RandomForestClassifier

    svcclassifier = RandomForestClassifier()
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as training_MODELr.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"training_MODELr.joblib")
    print("Model saved as training_MODELr.joblib")



def call_file():
    import Check_predict
    Check_predict.Train()


def window():
    root.destroy()


button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model Training", command=Model_Training, width=15, height=2)
button3.place(x=5, y=170)

button4 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Cyber_Attack_Detection", command=call_file, width=15, height=2)
button4.place(x=5, y=250)

exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=5, y=330)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''