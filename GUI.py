from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
#from CSC import cross_section_creator

def openFile():
    filedialog.askopenfilename()

#Creates a frame widget to hold the contents of the user interface
window = Tk()
window.title('Cross Section Creator')
mainframe = ttk.Frame(window, padding='4 4 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

#Creating Widgets


# first_df = pd.read_excel(first_button, engine='openpyxl')
# firstdf_list = first_df.values.tolist()
# second_df = pd.read_excel(second_button, engine='openpyxl')
# seconddf_list = second_df.values.tolist()

# for value in profile_set:
#         cross_section_creator(value, TTprofile_list, Rprofile_list)