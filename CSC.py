from matplotlib import pyplot as plt
from ExcelData import *
from secret import *

def cross_section_creator(value: int, profile_list: list):
        profile_dict = profile_dict_constructor(profile_list, value)
        if value > 0:
                plt.clf()
        plt.title(f'Cross Section {value}')
        plt.xlabel('Chainage (m)')
        plt.ylabel('Level (m)')
        x = profile_dict[value]['Chainage']
        y = profile_dict[value]['X']
        plt.plot(x, y)
        plt.savefig(f'{PNG_PATH}//Cross Section {value}.png')

for value in profile_set:
        cross_section_creator(value, profile_list)