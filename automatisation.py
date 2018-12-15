"""
	Function that saves the sublime build output into a txt file.
	Requirements: Having the build output on another window
"""
from pywinauto.application import Application
from pywinauto import keyboard
import pyperclip
from win10toast import ToastNotifier as Notifier
import time
import os
from datetime import datetime

def developpment(window_name,filename,save_dir="./SublimeSaveTemp",minimize=False,notification=False):

	notif = Notifier()

	#Warns the user 2 seconds before the saving if activated
	if notification: 
		notif.show_toast("File \"{}\" saving in 3 seconds".format(window_name),"Please stop typing/clicking",duration=3)

	app = Application().connect(path=r"C:\Program Files (x86)\Sublime Text 3\sublime_text.exe")
	first_window = str(app.windows()[0]).split("'")[1]

	app_dialog = app.top_window()

	#Gets window focus if needed
	if app_dialog.has_keyboard_focus() == False:
		app_dialog.minimize()
		app_dialog.restore()

	#Saves everything
	if find_tab(app,window_name):

		save_to_file(save_dir,filename,get_text())

		if notification:
			notif.show_toast("File \"{}\" saved".format(window_name),"Go on and have fun!",threaded=True,duration=2)

		if find_tab(app,first_window) == False: #Returns to the first tab
			print("ERROR: Could not return to the previous window")

		if minimize:
			app_dialog.minimize()
	else:
		print("ERROR: Could not save the file: \"{}\" not found".format(window_name))


#Saving text into a txt file
def save_to_file(save_dir,filename,text):

	header = "\n ====== Sublime Autosaver ====== Time: {} \n".format(datetime.now())	#Appears at the beginning of the file

	try:												#Test if the path's good
		new_file = open(save_dir +"\\"+ filename + ".txt","a") #Appends at the end of the file if already exists
	except FileNotFoundError:							#If the path doesn't exist

		if not os.path.exists("./SublimeSaveTemp"):		#Creates the directory
   			os.makedirs("./SublimeSaveTemp")

		new_file = open("./SublimeSaveTemp/" + filename + ".txt","a")

	new_file.write(header)
	new_file.write(text)
	new_file.close()

#Select,copy and returns the text
def get_text():
	content = pyperclip.paste() 				#Gets clipboard's content before the action

	keyboard.SendKeys("^A")
	keyboard.SendKeys("^C")						#Copy everything
	text_to_file = pyperclip.paste()			#Clipboard's content to variable

	pyperclip.copy(content)						#Gets what it had before

	return text_to_file

#Finds a tab by it's approximated name
def find_tab(app,name):
	current_window = ""
	starting_window = str(app.windows()[0]).split("'")[1]

	#Passes on every tabs until it finds it /or/ gets back to the starts
	while current_window != starting_window:
		keyboard.SendKeys('^{PGDN}') 								#Changing tab
		current_window = str(app.windows()[0]).split("'")[1].lower() #Get window's name

		if current_window.find(name.lower()) > -1:
			return True

	return False
