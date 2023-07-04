import pandas as pd
from secret import SECRET_PATH

df = pd.read_excel(SECRET_PATH, engine='openpyxl')

profile_list = df.values.tolist()
profile_set = set(df['Profile'])
for value in profile_set:
    profile_dict = {value: {'X':[], 'Chainage': []}}
    for point_profile in profile_list:
        if point_profile[0] == list(profile_dict.keys())[0]:
            profile_dict[value]['X'].append(point_profile[3])
            profile_dict[value]['Chainage'].append(point_profile[5])
    print(profile_dict)
