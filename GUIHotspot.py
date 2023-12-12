#!/usr/bin/python3
# Name : MyHotspot
# Programmer : Cyber Root
from tkinter import *
from tkinter import messagebox
import os

box = Tk()
box.title("GUIHotspot")
box.iconbitmap("resources/Hotspot.ico")

main_frame = Frame(box)
main_frame.pack(fill=BOTH, expand=YES)





def clear_():
    txt_box.delete(0, END)


def start_():
    clear_()
    # messagebox.showinfo("Hotspot Enabler", "Starting Hotspot +++++++++")
    os.system("netsh wlan set hostednetwork mode=allow ssid=" + id_.get() + " key=" + key_.get())
    os.system("netsh wlan start hostednetwork > log/netsh.log")
    try:
        show = open("log/netsh.log", "r")
        for word in show:
            txt_box.insert(END, word)
    except:
        txt_box.insert(END, "Start Error")


def stop_():
    clear_()
    # messagebox.showinfo("Hotspot Enabler", "Stopping Hotspot +++++++++")
    os.system("netsh wlan stop hostednetwork > log/netsh.log")
    try:
        show = open("log/netsh.log", "r")
        for word in show:
            txt_box.insert(END, word)
    except:
        txt_box.insert(END, "Stop Error")


def refresh_():
    clear_()
    # messagebox.showinfo("Hotspot Enabler", "Refreshing Hotspot +++++++++")
    os.system("netsh wlan refresh hostednetwork key > log/netsh.log")
    try:
        show = open("log/netsh.log", "r")
        for word in show:
            txt_box.insert(END, word)
    except:
        txt_box.insert(END, "Refresh Error")


def show_():
    clear_()
    os.system("netsh wlan show all > log/netsh.log")
    try:
        show = open("log/netsh.log", "r")
        for word in show:
            txt_box.insert(END, word)
    except:
        txt_box.insert(END, "Show Error")


def exit_():
    messagebox.showinfo("Hotspot Enabler", "Exiting +++++++++")
    quit()


def cmd():
    clear_()
    if cmd_.get() == "cmd" or cmd_.get() == "CMD":
        cmd_.delete(0, END)
    elif cmd_.get() == "":
        txt_box.insert(END, "The syntax of the command is incorrect.")
    else:
        os.system(cmd_.get() + " > log/netsh.log")
        try:
            show = open("log/netsh.log", "r")
            for word in show:
                txt_box.insert(END, word)
        except:
            txt_box.insert(END, "Command Error")


frm_1 = Frame(main_frame)
frm_1.pack(side=TOP, expand=YES, fill=BOTH)

frm_2 = Frame(main_frame)
frm_2.pack(side=BOTTOM, expand=YES, fill=BOTH)

frm_7 = Frame(frm_1, bg="Grey")
frm_7.pack(side=LEFT, expand=YES, fill=BOTH)

frm_3 = Frame(frm_7)
frm_3.pack(side=TOP, expand=YES, fill=BOTH)

frm_4 = Frame(frm_7)
frm_4.pack(side=TOP, expand=YES, fill=BOTH)

frm_5 = Frame(frm_7)
frm_5.pack(side=TOP, expand=YES, fill=BOTH)

frm_6 = Frame(frm_1)
frm_6.pack(side=RIGHT, expand=YES, fill=BOTH)

frm_8 = Frame(frm_2, bg="Grey")
frm_8.pack(expand=YES)

lbl_1 = Label(frm_3, text=" SSID ", font=("Arial Bold", 10))
lbl_1.pack(side=LEFT, expand=YES)

lbl_2 = Label(frm_4, text=" KEY  ", font=("Arial Bold", 10))
lbl_2.pack(side=LEFT, expand=YES)


id_ = Entry(frm_3, width=50, bd=5)
id_.pack(side=RIGHT, expand=YES)

key_ = Entry(frm_4, width=50, bd=5, show="*")
key_.pack(side=RIGHT, expand=YES)

cmd_ = Entry(frm_5, width=50, bd=5)
cmd_.pack(side=RIGHT, expand=YES)

btn1 = Button(frm_6, text="START", font=("Arial Bold", 8), width=9, height=2, command=start_)
btn1.pack(side=TOP, expand=YES)

btn2 = Button(frm_6, text="SHOW ALL INFO", font=("Arial Bold", 8), width=15, height=2, command=show_)
btn2.pack(side=BOTTOM, expand=YES)

btn3 = Button(frm_6, text="REFRESH", font=("Arial Bold", 8), width=9, height=2, command=refresh_)
btn3.pack(side=LEFT, expand=YES)

btn4 = Button(frm_6, text="STOP", font=("Arial Bold", 8), width=9, height=2, command=stop_)
btn4.pack(side=RIGHT, expand=YES)

btn5 = Button(frm_6, text="EXIT", font=("Arial Bold", 8), width=9, height=2, command=exit_)
btn5.pack(pady=110, expand=YES)

btn6 = Button(frm_5, text="RUN CMD", font=("Arial", 8), width=8, command=cmd)
btn6.pack(side=LEFT, expand=YES)

scrollbar = Scrollbar(frm_8)
scrollbar.pack(side=RIGHT, fill=Y)

txt_box = Listbox(frm_8, yscrollcommand=scrollbar.set, width=120, height=25, bg="black", fg="green",
                  font=("Arial Bold", 9), selectmode=EXTENDED)
txt_box.pack(fill=BOTH)
scrollbar.config(command=txt_box.yview)

#box.config(menu=menubar)
box.geometry("800x700")
box.mainloop()
