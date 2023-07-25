import pandas as pd
from secret import FIRST_SECRET_PATH, SECOND_SECRET_PATH

df = pd.read_excel(FIRST_SECRET_PATH, engine='openpyxl') #Reads the excel file and stores it in a the dataframe (df) variable.
profile_set = set(df['Profile']) #Creates a set containing the cross section 'names'.
#When this was made cross sections were produced to mimic those found in the 2014 Ramboll data as such there is no need to create multiple profile sets as
#they both have the same number of points for the same number of cross sections.

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

    profile_dict = {value: {'Z':[], 'Chainage': []}} #Creates a nested dictionary with two keys and an empty list object as the values.
    for point_profile in profile_list: #For every point in the excel file (Basically every row in excel file)
        if point_profile[0] == list(profile_dict.keys())[0]: #Check if the point profile is part of the cross section currently under construction.
            profile_dict[value]['Z'].append(point_profile[3]) #Z values in the point profile are found at index 3. Appends these values to the list value in the nested dictionary key value pair.
            profile_dict[value]['Chainage'].append(point_profile[5]) #Chainage values in the point profile are found at index 5. Appends these values to the list value in the nested dictionary key value pair.
    
    return profile_dict #Returns the dictionary once it has been completed.
