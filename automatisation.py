"""
	Fonction permettant de sauvegarder le Build Output dans un fichier txt.
"""
from pywinauto.application import Application
from pywinauto import keyboard
import pyperclip


def developpment(save_dir,filename,minimize_after_op):
	
	current_window = ""
	window_found = False

	app = Application().connect(path=r"C:\Program Files (x86)\Sublime Text 3\sublime_text.exe")
	win = app.window(title_re=".*Build output*.")

	first_window = str(app.windows()[0])
	
	app_dialog = app.top_window()
	app_dialog.minimize()
	app_dialog.restore()

	#Boucle sur tout les tabs pour trouver la bonne
	while current_window != first_window:

		keyboard.SendKeys('^{PGDN}') #Si pas directement sur la fenetre build output
		current_window = str(app.windows()[0]) #Nom de la window

		if current_window.find("Build output") > -1:
			window_found = True
			break


	#Enregistre le tout dans un txt
	if window_found:
		win.menu_select("Selection->Select All")	#Sélectionne tout le texte du output
		keyboard.SendKeys('^C')						#Copie le contenu
		text_to_file = pyperclip.paste()			#Contenu du copie dans la variable
		
		#Saving it into a txt file
		new_file = open(save_dir +"\\"+ filename + ".txt","w")
		new_file.write(text_to_file)
		new_file.close()

		if minimize_after_op:
			app_dialog.minimize()
		

