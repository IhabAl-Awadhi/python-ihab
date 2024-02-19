# Program to make a simple
# login screen

from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox as tkMessageBox
import sys
import os

root=tk.Tk()

# setting the windows size
root.geometry("800x800")

# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()


def run():
    os.system("python attendance.py")

btn = tk.Button(root, text="Attendance",command=run)
# defining a function that will
# get the name and password and
# print them on the screen
name_label2 = tk.Label(root, text = 'try a gain please ', font=('calibre',10, 'bold'))

def submit():

	name=name_var.get()
	password=passw_var.get()
	if name!="ihab" and password!="00000":
		#B = tkMessageBox.showinfo( "Hello", "Hello "+name)
		#B.pack()

		name_label2.pack()

	elif name=="ihab" and password=="00000":
		#B = tkMessageBox.showinfo( "Hello", "Hello "+name)
		#B.pack()
		name_label2.forget()
		name_label.forget()
		name_entry.forget()
		passw_label.forget()
		passw_entry.forget()
		sub_btn.forget()




		name_label1 = tk.Label(root, text = 'good morning '+name, font=('calibre',10, 'bold'))
		name_label1.pack()
		btn.pack()



		#C = tkMessageBox.showinfo( "Hello", "Hello this not fucking worng "+name)
		#C.pack()
		#phone = StringVar()

		#home = tk.Radiobutton(root, text='Home', variable=phone, value='home')
		#office = tk.Radiobutton(root, text='Office', variable=phone, value='office')
		#cell = tk.Radiobutton(root, text='Mobile', variable=phone, value='cell')
		#name_label.pack()
		#name_entry.pack()
		#passw_label.pack()
		#passw_entry.pack()
		#sub_btn.pack()



	name_var.set("")
	passw_var.set("")


# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

# creating a label for password
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))

# creating a entry for password
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = "*")

welcome_label = tk.Label(root, text = "welcome Mr:"+str(name_var), font = ('calibre',10,'bold'))
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)






# placing the label and entry in
# the required position using grid
# method
name_label.pack()
name_entry.pack()
passw_label.pack()
passw_entry.pack()
sub_btn.pack()

# performing an infinite loop
# for the window to display
root.mainloop()
S
