"""
	Function that saves the sublime build output into a txt file.
	Requirements: Having the build output on another window
"""
from pywinauto.application import Application
from pywinauto import keyboard
import pyperclip
from win10toast import ToastNotifier as Notifier
import time

def developpment(window_name,save_dir,filename,minimize_after_op=False,notification=False):

	notif = Notifier()

	if notification: #Warns the user 2 seconds before the saving
		notif.show_toast("File \"{}\" saving in 2 seconds".format(window_name),"Please stop typing/clicking")
		time.sleep(2)

	app = Application().connect(path=r"C:\Program Files (x86)\Sublime Text 3\sublime_text.exe")
	first_window = str(app.windows()[0]).split("'")[1]

	app_dialog = app.top_window()

	#Gets window focus
	app_dialog.minimize()
	app_dialog.restore()

	#Save into a txt file
	if find_tab(app,window_name):

		save_to_file(save_dir,filename,get_text())

		if notification:
			notif.show_toast("File \"{}\" saved".format(window_name),"Go on and have fun!")

		if find_tab(app,first_window) == False: #Returns to the first tab
			print("ERROR: Could not return to the previous window")

		if minimize_after_op:
			app_dialog.minimize()
	else:
		print("ERROR: Could not save the file: \"{}\" not found".format(window_name))




#Saving text into a txt file
def save_to_file(save_dir,filename,text):
	new_file = open(save_dir +"\\"+ filename + ".txt","w")
	new_file.write(text)
	new_file.close()

#Select,copy and returns the text
def get_text():
	keyboard.SendKeys("^A")
	keyboard.SendKeys("^C")						#Copy everything
	text_to_file = pyperclip.paste()			#Clipboard's content to variable

	return text_to_file

#Finds a tab by it's approximated name
def find_tab(app,name):
	current_window = ""
	starting_window = str(app.windows()[0]).split("'")[1]

	#Passes on every tabs until it finds it /or/ gets back to the starts
	while current_window != starting_window:
		keyboard.SendKeys('^{PGDN}') #Changing tab
		current_window = str(app.windows()[0]).split("'")[1] #Get window's name

		if current_window.find(name) > -1:
			return True

	return False
