from matplotlib import pyplot as plt
from ExcelData import *
from secret import PNG_PATH

#Reads the information from the excel files specified in secret.py using the read_excel function found in ExcelData.py
first_df = pd.read_excel(FIRST_SECRET_PATH, engine='openpyxl')
first_profile_list = first_df.values.tolist()
second_df = pd.read_excel(SECOND_SECRET_PATH, engine='openpyxl')
second_profile_list = second_df.values.tolist()

#Function that produces cross sections from the data found in the excel files.
def cross_section_creator(value: int, first_profile_list: list, second_profile_list: list):
        """
        Parameters:
        -----------
        value: int
                value of a profile in the profile_set
        profile_list: list
                list of lists containing every row in the excel file

        Notes
        -----
        Does not return anything, but produces a graph utilising matplotlib for all profiles in the profile list.
        """
        first_profile_dict = profile_dict_constructor(first_profile_list, value)
        second_profile_dict = profile_dict_constructor(second_profile_list, value)

        plt.clf() #Clears matplotlib frame so that each cross section produced is not overlain with data from previous cross sections. 

        plt.figure(figsize=(15, 10))
        plt.title(f'Cross Section {value}')
        plt.xlabel('Chainage (m)')
        plt.ylabel('Level (m)')

        #Takes the relevant values from the profile dictionaries to create list objects containing the values relevant for the x and y positions of each plot.
        first_x = first_profile_dict[value]['Chainage']
        first_y = first_profile_dict[value]['Z']
        second_x = second_profile_dict[value]['Chainage']
        second_y = second_profile_dict[value]['Z']

        plt.minorticks_on() #Plots the minor ticks in between the major ticks
        plt.plot(first_x, first_y, label = 'Waterhouse Cross Section') #Plots a line using values from the first profile list (The first data frame)
        plt.plot(second_x, second_y, label = 'Ramboll Cross Section') #Plots a line using values from the second profile list (The second data frame)   
        plt.fill_between(second_x, -0.74, 1.54, color='b', alpha=0.1, label="mean water range") #Plots the mean water range
        plt.subplot().set_aspect('equal') #Ensures a natural scale
        plt.legend() #Creates the legend for regions displayed on the graph
        plt.savefig(f'{PNG_PATH}//Cross Section {value}.pdf') #Saves the resulting graph to the specified filepath. Changing the file suffix (eg .pdf/.png) changes the format of the file.



for value in profile_set:       #profile_set found in ExcelData.py. Value represents each item inside the profile set.
        cross_section_creator(value, first_profile_list, second_profile_list) #runs the csc function repeatedly for the number of values in the profile set.