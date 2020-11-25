#!/usr/bin/env python3

from os import listdir
import tkinter as tk
import time
import threading
# from gpiozero import Servo

class Cat_Feeder(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Cat Feeder')
        self.minsize(480, 320)
        self.maxsize(480, 320)
        self.overrideredirect(True)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.background_image=tk.PhotoImage(file=r'wallpaper.png')
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.grid(row=0, column=0)

        self.clock_label = tk.Label(self, font='ariel 40', bg='#d9c5e0', fg='#94b395')
        self.clock_label.place(relx=0.4,rely=0.01)

        self.cameraImage = tk.PhotoImage(file=r"camera.png")
        self.camera_Button = tk.Button(self, text='Camera', image = self.cameraImage, bg='#d9c5e0', command=lambda : self.launchCamera )
        self.camera_Button.place(relx=0.76,rely=0.018)

        self.bfeedNow = tk.Button(self, text='Feed Now', font='ariel 20', command=lambda: feedNow() )
        self.bfeedNow.place(relx=0.68, rely=0.8)

        self.bexit = tk.Button(self, text='Exit', font='ariel 20', command=lambda: self.destroy() )
        self.bexit.place(relx=0.08, rely=0.8)

        self.feed_times()
        self.get_saved_info()
        self.display_Time()
        self.mainloop()

    def get_saved_info(self):
        if 'saved_info' not in listdir():
            with open('saved_info.txt', 'w') as f:
                f.writelines(['9:30\n', '20:00\n', 'None\n'])
        with open("saved_info.txt", 'r') as f:
            self.savedFeedTime1 = f.readline().replace('\n','')
            self.savedFeedTime2 = f.readline().replace('\n','')
            self.savedFeedTime3 = f.readline().replace('\n','')
        self.sfeed_Time1.set(self.savedFeedTime1)
        self.sfeed_Time2.set(self.savedFeedTime2)
        self.sfeed_Time3.set(self.savedFeedTime3)
    
    def display_Time(self):
        check = time.strftime('%S')
        if int(check) % 2 == 0:
            currentTime = time.strftime('%H:%M')
        else:
            currentTime = time.strftime('%H %M')
        self.clock_label['text'] = currentTime

        alarmTime = time.strftime('%H:%M')
        if alarmTime + check == self.sfeed_Time1.get() + '00' or alarmTime + check == self.sfeed_Time2.get() + '00' or alarmTime + check == self.sfeed_Time3.get() + '00':
            try:
                self.feedNow()
            except:
                print("opps something bad happened")
            
        self.after(1000, self.display_Time)
    
    def feed_times(self):
        self.sfeed_Time1 = tk.StringVar()
        self.bfeed_Time1 = tk.Button(self, textvariable=self.sfeed_Time1, font='ariel 20', command=lambda: self.changeFeedTime('Button1'))
        self.bfeed_Time1.place(relx=0.05, rely=0.15)

        self.sfeed_Time2 = tk.StringVar()
        self.bfeed_Time2 = tk.Button(self, textvariable=self.sfeed_Time2, font='ariel 20', command=lambda: self.changeFeedTime('Button2'))
        self.bfeed_Time2.place(relx=0.05, rely=0.35)

        self.sfeed_Time3 = tk.StringVar()
        self.bfeed_Time3 = tk.Button(self, textvariable=self.sfeed_Time3, font='ariel 20', command=lambda: self.changeFeedTime('Button3'))
        self.bfeed_Time3.place(relx=0.05, rely=0.55)

    def writeChanges(self):
        def doIt2():
            with open('saved_info.txt', 'w') as info:
                info.write(self.sfeed_Time1.get()+'\n')
                info.write(self.sfeed_Time2.get()+'\n')
                info.write(self.sfeed_Time3.get()+'\n')
        self.t1 = threading.Thread(target=doIt2)
        self.t1.start()

    def changeFeedTime(self, selectedButton):
        self.selectTime(selectedButton)
        self.bfeed_Time1.update_idletasks()
        self.bfeed_Time2.update_idletasks()
        self.bfeed_Time3.update_idletasks()
    
    def selectTime(self, selectedButton):
        self.upper_window = tk.Tk()
        self.upper_window.title('Cat Feeder')
        self.upper_window.configure(bg='#C2B8C3')
        self.upper_window.minsize(480, 320)
        self.upper_window.maxsize(480, 320)
        self.upper_window.overrideredirect(True)
        self.upper_window.geometry("{0}x{1}+0+0".format(self.upper_window.winfo_screenwidth(), self.upper_window.winfo_screenheight()))
        self.hour = tk.Spinbox(self.upper_window, from_=-1, to=23,wrap=True, width=4, state="readonly", font='ariel 80', bg='#C2B8C3')
        self.min = tk.Spinbox(self.upper_window, from_=0,to=59,wrap=True, width=4, state="readonly", font='ariel 80', bg='#C2B8C3')
        self.hour.place(relx=.20, rely=.01)
        self.min.place(relx=.20, rely=.40)
        self.save_button = tk.Button(self.upper_window, font='ariel 22', text='Okay', command= lambda: self.saveAndDestroy(selectedButton) )
        self.save_button.place(relx=.3, rely=.80)
        self.cancel_button = tk.Button(self.upper_window, font='ariel 22', text='Cancel', command= lambda: self.upper_window.destroy() )
        self.cancel_button.place(relx=.5, rely=.80)
        self.upper_window.mainloop()

    def saveAndDestroy(self, selectedButton):
            newFeedTime = "{}:{}".format( self.hour.get(), self.min.get() )
            if int(self.min.get()) < 10:
                newFeedTime = "{}:0{}".format( self.hour.get(), self.min.get() )
            if int(self.hour.get()) < 10:
                newFeedTime = "0{}:{}".format( self.hour.get(), self.min.get() )
            if int(self.hour.get()) < 10 and int(self.min.get()) < 10:
                newFeedTime = "0{}:0{}".format( self.hour.get(), self.min.get() )
            if int(self.hour.get()) == -1:
                newFeedTime = 'None'

            if selectedButton == "Button1":
                self.sfeed_Time1.set( newFeedTime )
            if selectedButton == "Button2":
                self.sfeed_Time2.set( newFeedTime )
            if selectedButton == "Button3":
                self.sfeed_Time3.set( newFeedTime )

            self.writeChanges()
            self.upper_window.destroy()

    def feedNow(self):
        # print('kitty has been fed!') # change to log feed time here or email it for fun.
        def doIt3():
            try:
                exec(open("Lfeed_Cats.py").read())
                exec(open("Rfeed_Cats.py").read())
            except Exception as e:
                with open('failedToFeed.txt', 'w') as info:
                    info.write('something went wrong with the servo')
                    info.write(str(e))
        t2 = threading.Thread(target=doIt3)
        t2.start()
    
    def launch_camera(self):
        pass

if __name__ == '__main__':
    Cat_Feeder()

