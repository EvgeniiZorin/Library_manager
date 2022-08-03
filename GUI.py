from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile, askopenfilename
import os
import numpy as np, pandas as pd
from IPython.display import display
from tabulate import tabulate

# pyinstaller -w --icon=<iconName.ico> GUI_start.py

############################################################################
#####   Backend   ##########################################################
############################################################################

def dataset_process_basic(file_name):
	df = pd.read_csv(file_name, sep='\t')
	return df

def actions(file_name, action, *args):
	df = dataset_process_basic(file_name)
	if action == '1':
		win = Toplevel(window)
		# global categories_list
		# categories_list = Text(window, height=10, width=50)
		# categories_list.insert(1.0, df)
		# categories_list.grid(column=1, row=3)
		global categories_list
		categories_list = Text(win, height=30, width=100)
		categories_list.insert(1.0, tabulate(df, headers='keys', tablefmt='psql'))
		categories_list.grid(column=0, row=0)
	if action == '2':
		win = Toplevel(window)
		global text_window
		text_window = Text(win, height=30, width=100)
		df1 = df['Author name'].unique()
		print(df1)
		text_window.insert(1.0, df1)
		text_window.grid(column=0, row=0)
	if action == '3':
		print(args)
		win = Toplevel(window)
		# global text_window
		text_window = Text(win, height=30, width=100)
		df1 = df[df['Author name'] == args[0] ]
		text_window.insert(1.0, tabulate(df1, headers='keys', tablefmt='psql'))
		text_window.grid(column=0, row=0)



############################################################################
#####   GUI   ##############################################################
############################################################################

### Variables ###
version = '2.0.0'

#################


window = Tk()
window.title(f"Library ver {version}")


# EXIT button
exit_btn = Button(window, text='EXIT', command=window.quit)
exit_btn.grid(column=0, row=0, padx=50, pady=50)

browse_text = StringVar()

# SELECT FILE prompt
def open_file(pre_selected_file):
	if pre_selected_file == True:
		file='C:/Users/evgen/Desktop/Python/Library/Library_v2.0.0/Library.tsv'
	else:
		browse_text.set('loading...')
		file = askopenfilename(filetype=[("TSV file", "*.tsv")])
	#
	if file:
		window.geometry('900x500')
		Label(window, text=f"You have selected: {file}").grid(column=1, row=1)
		browse_text.set('Select File')
		#
		btn1 = Button(window, text='Print all books', command=lambda: actions(file, '1'))
		btn1.grid(column=1, row=2)
		#
		btn2 = Button(window, text='Print all authors', command=lambda: actions(file, '2'))
		btn2.grid(column=1, row=3)
		#
		e1 = Entry(window, width=10)
		e1.grid(column=2, row=4)
		btn3 = Button(window, text='Print all books by an author', command=lambda: actions(file, '3', e1.get()))
		btn3.grid(column=1, row=4)


#### FOR TESTING ONLY
# open_file(True)

# SELECT FILE button
browse_text = StringVar()
selectFile_btn = Button(window, textvariable=browse_text, command=lambda:open_file(False))
browse_text.set('Select File')
selectFile_btn.grid(column=0, row=1)

window.mainloop()