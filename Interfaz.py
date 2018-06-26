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
		self.tk.bind("<F11>", self.toggle_fullscreen)
		self.tk.bind("<Escape>", self.end_fullscreen)
		self.tk.config(cursor="none")
		
		self.show_idle()
		
		t = Thread(target=self.listen_rfid)
		t.daemon = True
		t.start()
		
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
		
	def returnToIdle_fromPINentry(self):
		self.pin_entry_forget()
		self.show_idle()
		
	def returnToIdle_fromPINentered(self):
		self.PINresultLabel.grid_forget()
		self.show_idle()
		
	def returnToIdle_fromAccessGranted(self):
		GPIO.output(13,GPIO.LOW)
		self.SMSresultLabel.grid_forget()
		self.show_idle()
		
	def returnToIdle_fromSMSentry(self):
		self.PINresultLabel.grid_forget()
		self.smsDigitsLabel.grid_forget()
		count = 0
		while (count < 12):
			self.btn[count].grid_forget()
			count += 1
		self.show_idle()
		
	def	returnToIdle_fromSMSentered(self):
		self.SMSresultLabel.grid_forget()
		self.show_idle()
	
	def toggle_fullscreen(self, event=None):
		self.state = not self.state  # Just toggling the boolean
		self.tk.attributes("-fullscreen", self.state)
		return "break"

	def end_fullscreen(self, event=None):
		self.state = False
		self.tk.attributes("-fullscreen", False)
		return "break"
	
if __name__ == '__main__':
	w = Fullscreen_Window()
	w.tk.mainloop()
