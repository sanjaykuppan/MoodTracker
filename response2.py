from tkinter import Tk,Button,PhotoImage
from pymongo import MongoClient
import datetime

class response2:
    def adddata(self):
        #try:
        client=MongoClient('localhost',27017)
        db=client.data
        response=db.response
        self.details = {'time':self.time,
                        'date':self.date,
                        'mood':self.SUBJECT}
        response.insert_one(self.details)
        self.display.destroy()
        #except:
        #    print('failed')
        #    self.display.destroy()
        
    def disp(self):        
        def sethappy():
            self.SUBJECT = "Happy"
            self.adddata()
        def setneutral():
            self.SUBJECT = "Neutral"
            self.adddata()
        def setsad():
            self.SUBJECT = "Sad"
            self.adddata()
        def setangry():
            self.SUBJECT = "Angry"
            self.adddata()
        self.display=Tk()
        self.display.geometry("750x200")
        button1=Button(self.display,command = sethappy)
        button2=Button(self.display,command = setneutral)
        button3=Button(self.display,command = setsad)
        button4=Button(self.display,command = setangry)
        photo1=PhotoImage(file="happy.png")
        photo2=PhotoImage(file="neutral.png")
        photo3=PhotoImage(file="sad.png")
        photo4=PhotoImage(file="angry.png")
        button1.config(image=photo1,width="150",height="150")
        button1.pack()
        button1.place(x=20,y=20)
        button2.config(image=photo2,width="150",height="150")
        button2.pack()
        button2.place(x=200,y=20)
        button3.config(image=photo3,width="150",height="150")
        button3.pack()
        button3.place(x=380,y=20)
        button4.config(image=photo4,width="150",height="150")
        button4.pack()
        button4.place(x=550,y=20)
        self.display.mainloop()
    def __init__(self):
        self.date=datetime.datetime.now().strftime('%x') #mm/dd/yy
        self.time=datetime.datetime.now().strftime('%X') #H:M:S
        self.disp()

r=response2()

