import pandas as pd
from secret import TT_SECRET_PATH, R_SECRET_PATH

df = pd.read_excel(TT_SECRET_PATH, engine='openpyxl')
profile_set = set(df['Profile'])

def profile_dict_constructor(profile_list: list, value: int) -> dict:
    """
    Parameters
    ----------
    profile_list: list
        list of lists containing every row in the excel file
    value: int
        value of a profile in the profile_set

    Returns
    -------
        Function returns a dictionary of containing the chainage and z values for every point of a certain profile.
        The profile is determined by the value parameter.
    """

    profile_dict = {value: {'Z':[], 'Chainage': []}}
    for point_profile in profile_list:
        if point_profile[0] == list(profile_dict.keys())[0]:
            profile_dict[value]['Z'].append(point_profile[3])
            profile_dict[value]['Chainage'].append(point_profile[5])
    
    return profile_dict
