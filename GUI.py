from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
#from CSC import cross_section_creator

def openFile():
    filepaths = filedialog.askopenfilenames()
    print(filepaths)
    show_filepath(filepaths)
    first_button.config(text='Change xlsx file(s)')
    return filepaths

def show_filepath(filepaths: filedialog):
    if len(filepaths > 0):
        for file in filepaths:
            pass
        #file_label.config(text= text + f'')
    #file_label.config(text=f'')
    

def display_second_button():
    second_button = ttk.Button(master=mainframe, text='Open xlsx file', command=openFile)
    second_button.grid(row=0, column=0)

#Creates a frame widget to hold the contents of the user interface
window = Tk()
window.title('Cross Section Creator')
mainframe = ttk.Frame(window, padding='4 4 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
    

#Creating Widgets
first_button = ttk.Button(master=mainframe, text='Open first xlsx file', command=openFile)
first_button.grid(row=0, column=0)

file_label = Label(mainframe, text='')
file_label.grid(row=0, column=2)
#Check box for multiple files
check = IntVar()
multi_check = Checkbutton(mainframe, text='Is there a second excel file to add?', variable=check, command=display_second_button)
multi_check.grid(row=1, column=0)

window.mainloop()

# first_df = pd.read_excel(first_button, engine='openpyxl')
# firstdf_list = first_df.values.tolist()
# second_df = pd.read_excel(second_button, engine='openpyxl')
# seconddf_list = second_df.values.tolist()

# for value in profile_set:
#         cross_section_creator(value, TTprofile_list, Rprofile_list)