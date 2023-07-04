import pandas as pd
from secret import SECRET_PATH

df = pd.read_excel(SECRET_PATH, engine='openpyxl')

profile_list = df.values.tolist()
profile_set = set(df['Profile'])

def profile_dict_constructor(profile_list: list, profile_set: set, value: int) -> dict:
    profile_dict = {value: {'X':[], 'Chainage': []}}
    for point_profile in profile_list:
        if point_profile[0] == list(profile_dict.keys())[0]:
            profile_dict[value]['X'].append(point_profile[3])
            profile_dict[value]['Chainage'].append(point_profile[5])
    return profile_dict

for value in profile_set:
    print(profile_dict_constructor(profile_list, profile_set, value))