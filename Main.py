from tkinter import *
import tkinter as tk
import schedule
import time
from time import sleep
from subprocess import call
import tkinter.messagebox
import itertools
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from threading import *
import sys
import psutil
import os
import signal


App1 = tk.Tk()

CHROME_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
CHROMEDRIVER_PATH = 'chromedriver\chromedriver.exe'
WINDOW_SIZE = "1920, 1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH


def popup_bonus():
    root = Toplevel(background="#1A1A1A")
    large_font2 = ('Verdana', 12)
    root.title("Commands")
    w = 300     # popup window width
    h = 400     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = """

|This is Fake Youtube\n views generator|
---------------------------

This program refreshes \n a certain video \n link on Youtube and that \n creates fake views on the video.

---------------------------
Creator = Stefan Saran
---------------------------

---------------------------
Creation date: 
May 1st. 2020 - May 5th. 2020
---------------------------"""
    m += '\n'
    w = Label(root, text=m, width=120, height=20,
              background="#1A1A1A", foreground="white", font=large_font2)
    w.pack()

    root.transient(App1)
    root.grab_set()
    root.wait_window(root)
    try:
        root.resizable(False, False)
    except TclError:
        pass
    root.mainloop()


def center_window(width, height):
    screen_width = App1.winfo_screenwidth()
    screen_height = App1.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    App1.geometry('%dx%d+%d+%d' % (width, height, x, y))


def popup_bonus2():
    root = Toplevel(background="#1A1A1A")
    large_font2 = ('Verdana', 12)
    root.title("Commands")
    w = 300     # popup window width
    h = 400     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = """
-----------------------------------------
Entering Minimum 30 seconds\nafter every refresh, youtube \nwill count it as a view\n
Entering below 30 seconds, youtube\nwill mostly remove fake views.
Programm needs to be stoped \nand waited, to see the\nupdated views on the video
Fake views will need time\nto be updated on youtube video.
-----------------------------------------
Only Chrome web \nbrowser supported!
-----------------------------------------
"""
    m += '\n'
    w = Label(root, text=m, width=120, height=20,
              background="#1A1A1A", foreground="white", font=large_font2)
    w.pack()

    root.transient(App1)
    root.grab_set()
    root.wait_window(root)
    try:
        root.resizable(False, False)
    except TclError:
        pass
    root.mainloop()


refreshes = IntVar()
refreshes.set(0)


def website():
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                               chrome_options=chrome_options)
    browser.service.process  # is a Popen instance for the chromedriver process
    p = psutil.Process(browser.service.process.pid)
    for i in itertools.count():
        browser.get(youtube_entry.get())
        update1 = refreshes.get() + 1
        refreshes.set(update1)
        sleep(int(video_duration.get()))
        # a = browser.find_element_by_class_name(
        # 'style-scope ytd-video-primary-info-renderer').text
        #views = ""
        #views += a
        #slice1 = views[20:23].strip()
        # print(slice1)


class task_1(Thread):
    def run(self):
        appp = tk.Toplevel(background="#1A1A1A")
        appp.title("Refreshes")
        refresh_label = tk.Label(
            appp, width=30, height=3, bg="white", textvariable=str(refreshes))
        refresh_label.place(rely=0.4, relx=0.5, anchor="center")
        appp.geometry("220x100")
        appp_button = tk.Button(
            appp, width=10, text="Stop", command=lambda: exit(self))
        appp_button.pack(side="bottom")
        appp.resizable(False, False)
        center_window(220, 100)
        appp.protocol("WM_DELETE_WINDOW", App1.destroy)
        appp.mainloop()

    def exit(self):
        App1.destroy()

    def center_window(self, width, height):
        self.screen_width = App1.winfo_screenwidth()
        self.screen_height = App1.winfo_screenheight()

        # calculate position x and y coordinates
        self.x = (screen_width/2) - (width/2)
        self.y = (screen_height/2) - (height/2)
        run.appp.geometry('%dx%d+%d+%d' % (width, height, x, y))


class task_2(Thread):
    def run(self):
        website()


def callback():
    App1.withdraw()
    task_1().start()
    task_2().start()


test = False


def special():
    return "youtube" in youtube_entry.get()


def sadasd():
    return any(char.isdigit() for char in video_duration.get())


def warnings():
    if len(youtube_entry.get()) == 0 and len(video_duration.get()) > 0:
        tk.messagebox.showinfo("Error", "The link box cannot be empty!")
    elif len(youtube_entry.get()) > 0 and len(video_duration.get()) == 0:
        tk.messagebox.showinfo("Error", "The duration box cannot be empty!")
    elif len(youtube_entry.get()) == 0 and len(video_duration.get()) == 0 or youtube_entry.get() == "Insert the YouTube video link here" and video_duration.get() == "seconds after every refresh (max 60)":
        tk.messagebox.showerror("Error", "Boxes cannot be blank!")
    elif len(youtube_entry.get()) > 0 and sadasd() == False:
        tk.messagebox.showerror("Error", "Only numbers allowed!")
    elif special() == False:
        tk.messagebox.showerror("Error", "The link is not a youtube link")
    elif int(video_duration.get()) > 60:
        tk.messagebox.showerror(
            "Error", "The limit is 60 seconds after every refresh!")
    else:
        callback()


def add1(add1):
    if youtube_entry.get() == "Insert the YouTube video link here":
        youtube_entry.delete(0, END)
    else:
        pass


def add2(add2):
    if video_duration.get() == "seconds after every refresh (max 60)":
        video_duration.delete(0, END)
    else:
        pass


about_button = Button(App1, text="About", width=10, command=popup_bonus)
about_button.place(rely=0.03, relx=0.03)

start_button = Button(App1, text="Start", width=10, command=warnings)
start_button.place(rely=0.8, relx=0.4)

help_button = Button(App1, text="Help", width=10, command=popup_bonus2)
help_button.place(rely=0.03, relx=0.8)

App1.configure(bg="#1A1A1A")

center_window(500, 300)

large_font = ('Verdana', 17)
youtube_entry = tk.Entry(App1, font=large_font, width=28)
youtube_entry.place(rely=0.4, relx=0.5, anchor="center")
youtube_entry.configure(foreground="gray")


video_duration = tk.Entry(App1, width=35)
video_duration.place(rely=0.55, relx=0.5, anchor="center")
video_duration.insert(0, "seconds after every refresh (max 60)")
youtube_entry.insert(0, "Insert the YouTube video link here")
video_duration.bind("<Button-1>", add2)
youtube_entry.bind("<Button-1>", add1)
video_duration.configure(foreground="gray")

App1.resizable(False, False)
App1.mainloop()
