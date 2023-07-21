from matplotlib import pyplot as plt
from ExcelData import *
from secret import PNG_PATH


TTdf = pd.read_excel(TT_SECRET_PATH, engine='openpyxl')
TTprofile_list = TTdf.values.tolist()
Rdf = pd.read_excel(R_SECRET_PATH, engine='openpyxl')
Rprofile_list = Rdf.values.tolist()

def cross_section_creator(value: int, TTprofile_list: list, Rprofile_list: list):
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
        TTprofile_dict = profile_dict_constructor(TTprofile_list, value)
        Rprofile_dict = profile_dict_constructor(Rprofile_list, value)
        if value > 0:
                plt.clf()
        plt.figure(figsize=(15, 10))
        plt.title(f'Cross Section {value}')
        plt.xlabel('Chainage (m)')
        plt.ylabel('Level (m)')
        TTx = TTprofile_dict[value]['Chainage']
        TTy = TTprofile_dict[value]['Z']
        Rx = Rprofile_dict[value]['Chainage']
        Ry = Rprofile_dict[value]['Z']
        ax = plt.subplot()
        plt.minorticks_on()
        plt.plot(Rx, Ry, label = 'Ramboll Cross Section')
        plt.plot(TTx, TTy, label = 'WA Cross Section')
        plt.fill_between(Rx, -0.74, 1.54, color='b', alpha=0.1, label="mean water range")
        ax.set_aspect('equal')
        plt.legend()
        plt.savefig(f'{PNG_PATH}//Cross Section {value}.pdf')



for value in profile_set:
        cross_section_creator(value, TTprofile_list, Rprofile_list)