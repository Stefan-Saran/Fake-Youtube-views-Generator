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


Generator = tk.Tk()
Generator.title("Fake Youtube Views Generator")

CHROME_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
CHROMEDRIVER_PATH = 'chromedriver\chromedriver.exe'
WINDOW_SIZE = "1920, 1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH


def Programm_info():
    Popup_info = Toplevel(background="#1A1A1A")
    large_font2 = ('Verdana', 12)
    Popup_info.title("Commands")
    width = 300
    height = 400
    screen_width = Popup_info.winfo_screenwidth()
    screen_height = Popup_info.winfo_screenheight()
    x = (screen_width - width)/2
    y = (screen_height - height)/2
    Popup_info.geometry('%dx%d+%d+%d' % (width, height, x, y))
    About_info = """
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
    About_info += '\n'
    about_label = Label(Popup_info, text=About_info, width=120, height=20,
                        background="#1A1A1A", foreground="white", font=large_font2)
    about_label.pack()

    Popup_info.transient(Generator)
    Popup_info.grab_set()
    Popup_info.wait_window(Popup_info)
    try:
        Popup_info.resizable(False, False)
    except TclError:
        pass
    Popup_info.mainloop()


def centering_window(width, height):
    screen_width = Generator.winfo_screenwidth()
    screen_height = Generator.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Generator.geometry('%dx%d+%d+%d' % (width, height, x, y))


def Programm_help():
    Popup_help = Toplevel(background="#1A1A1A")
    font_help = ('Verdana', 12)
    Popup_help.title("Commands")
    popup_width = 300     # popup window width
    popup_height = 400     # popup window height
    screen_width = Popup_help.winfo_screenwidth()
    screen_height = Popup_help.winfo_screenheight()
    x = (screen_width - popup_width)/2
    y = (screen_height - popup_height)/2
    Popup_help.geometry('%dx%d+%d+%d' % (popup_width, popup_height, x, y))
    Help_info = """
-----------------------------------------
Entering Minimum 30 seconds\nafter every refresh, youtube \nwill count it as a view.\n
Entering below 30 seconds, youtube\nwill mostly remove fake views.
Programm needs to be stoped \nand waited, to see the\nupdated views on the video.
Fake views will need time\nto be updated on youtube video.
-----------------------------------------
Only Chrome web \nbrowser supported!
-----------------------------------------
"""
    Help_info += '\n'
    popup_width = Label(Popup_help, text=Help_info, width=120, height=20,
                        background="#1A1A1A", foreground="white", font=font_help)
    popup_width.pack()

    Popup_help.transient(Generator)
    Popup_help.grab_set()
    Popup_help.wait_window(Popup_help)
    try:
        Popup_help.resizable(False, False)
    except TclError:
        pass
    Popup_help.mainloop()


refreshes = IntVar()
refreshes.set(0)


def error_popup():
    error_ocurred = tk.messagebox.showerror(
        "Error", "Random error ocurred")
    if error_ocurred:
        Generator.destroy()


def website():
    try:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                                   chrome_options=chrome_options)
        browser.service.process
        p = psutil.Process(browser.service.process.pid)
        for i in itertools.count():
            browser.get(youtube_entry.get())
            update1 = refreshes.get() + 1
            refreshes.set(update1)
            sleep(int(video_duration.get()))
    except:
        error_popup()


class Refresh_window(Thread):
    def run(self):
        refresh_counter = tk.Toplevel(background="#1A1A1A")
        refresh_counter.title("Refreshes")
        refresh_label = tk.Label(
            refresh_counter, width=30, height=3, bg="white", textvariable=str(refreshes))
        refresh_label.place(rely=0.4, relx=0.5, anchor="center")
        refresh_counter.geometry("220x100")
        refresh_button = tk.Button(
            refresh_counter, width=10, text="Stop", command=lambda: exit(self))
        refresh_button.pack(side="bottom")
        refresh_counter.resizable(False, False)
        refresh_counter.protocol("WM_DELETE_WINDOW", Generator.destroy)

        self.screen_width = Generator.winfo_screenwidth()
        self.screen_height = Generator.winfo_screenheight()

        # calculate position x and y coordinates
        self.x = (self.screen_width/2) - (220/2)
        self.y = (self.screen_height/2) - (100/2)
        refresh_counter.geometry('%dx%d+%d+%d' % (220, 100, self.x, self.y))

        refresh_counter.mainloop()

    def exit(self):
        Generator.destroy()


class running_website(Thread):
    def run(self):
        website()


def running_at_the_same_time():
    Generator.withdraw()
    Refresh_window().start()
    running_website().start()


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
        running_at_the_same_time()


def delete_youtube_entry_text(add1):
    if youtube_entry.get() == "Insert the YouTube video link here":
        youtube_entry.delete(0, END)
    else:
        pass


def delete_video_duration_text(add22):
    if video_duration.get() == "seconds after every refresh (max 60)":
        video_duration.delete(0, END)
    else:
        pass


about_button = Button(Generator, text="About", width=10, command=Programm_info)
about_button.place(rely=0.03, relx=0.03)

start_button = Button(Generator, text="Start", width=10, command=warnings)
start_button.place(rely=0.8, relx=0.4)

help_button = Button(Generator, text="Help", width=10, command=Programm_help)
help_button.place(rely=0.03, relx=0.8)

Generator.configure(bg="#1A1A1A")

centering_window(500, 300)

large_font = ('Verdana', 17)
youtube_entry = tk.Entry(Generator, font=large_font, width=28)
youtube_entry.place(rely=0.4, relx=0.5, anchor="center")
youtube_entry.configure(foreground="gray")


video_duration = tk.Entry(Generator, width=35)
video_duration.place(rely=0.55, relx=0.5, anchor="center")
video_duration.insert(0, "seconds after every refresh (max 60)")
youtube_entry.insert(0, "Insert the YouTube video link here")
video_duration.bind("<Button-1>", delete_video_duration_text)
youtube_entry.bind("<Button-1>", delete_youtube_entry_text)
video_duration.configure(foreground="gray")

Generator.resizable(False, False)
Generator.mainloop()
