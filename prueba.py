#!/usr/bin/env python3
import sys
from threading import Thread
import threading

try:
	# python 2
	import Tkinter as tk
	import ttk
except ImportError:
	# python 3
	import tkinter as tk
	from tkinter import ttk



class Fullscreen_Window:
	
	global dbHost
	global dbName
	global dbUser
	global dbPass
	
	dbHost = 'localhost'
	dbName = 'DB_NAME'
	dbUser = 'USER'
	dbPass = 'PASSWORD'
	
	def __init__(self):
		self.tk = tk.Tk()
		self.tk.title("Three-Factor Authentication Security Door Lock")
		self.frame = tk.Frame(self.tk)
		self.frame.grid()
		self.tk.columnconfigure(0, weight=1)
		
		self.tk.attributes('-zoomed', True)
		self.tk.attributes('-fullscreen', True)
		self.state = True
		self.show_idle()
		
	def show_idle(self):
		self.welcomeLabel = ttk.Label(self.tk, text="Please Present\nYour Token")
		self.welcomeLabel.config(font='size, 20', justify='center', anchor='center')
		self.welcomeLabel.grid(sticky=tk.W+tk.E, pady=210)
	
	def pin_entry_forget(self):
		self.validUser.grid_forget()
		self.photoLabel.grid_forget()
		self.enterPINlabel.grid_forget()
		count = 0
		while (count < 12):
			self.btn[count].grid_forget()
			count += 1
		
	
if __name__ == '__main__':
	w = Fullscreen_Window()
	w.tk.mainloop()
