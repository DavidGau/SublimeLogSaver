"""
	Function that saves the sublime build output into a txt file.
	Requirements: Having the build output on another window
"""
from pywinauto.application import Application
from pywinauto import keyboard
import pyperclip
from win10toast import ToastNotifier as Notifier
import time

def developpment(save_dir,filename,minimize_after_op=False,notification=False):

	notif = Notifier()

	if notification: #If notifications are enabled, warn the user
		notif.show_toast("Log saving in 2 seconds","Please stop typing/clicking")
		time.sleep(2)

	
	window_found = False

	app = Application().connect(path=r"C:\Program Files (x86)\Sublime Text 3\sublime_text.exe")
	win = app.window(title_re=".*Build output*.")

	log_window = str(app.windows()[0])

	app_dialog = app.top_window()
	app_dialog.minimize()
	app_dialog.restore()


	current_window = ""
	
	#Passes on every tabs until it finds it
	while current_window != log_window:
		keyboard.SendKeys('^{PGDN}') #Changing tab
		current_window = str(app.windows()[0]) #Get window's name

		if current_window.find("Build output") > -1:
			window_found = True
			break


	#Save into a txt file
	if window_found:
		win.menu_select("Selection->Select All")	#Selecting the output's text
		keyboard.SendKeys("^A")
		keyboard.SendKeys("^C")						#Copy everything
		text_to_file = pyperclip.paste()			#Clipboard's content to variable
		
		#Saving it into a txt file
		new_file = open(save_dir +"\\"+ filename + ".txt","w")
		new_file.write(text_to_file)
		new_file.close()

		if minimize_after_op:
			app_dialog.minimize()

		if notification:
			notif.show_toast("Log saved","Go on and have fun!")

