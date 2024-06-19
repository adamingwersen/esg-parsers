import pandas as pd
import json
import uuid
import hashlib

df = pd.read_json("esrs.json")
print(df.columns)

# categories to slice
## dr
## topic
## xbrl_data_type
## dr : dr_name
## dr : dr_reporting_area
## dr : dr_name : dr_reporting_area

# data_types_unique =  df['dr_link'].tolist()

# # print("DATA TYPES ->", len(data_types_unique))
# # for dt in data_types_unique:
# #     print('"{}"'.format(dt), " | ")


data_types_dr = df['dr'].unique()
# for dt in data_types_dr:
#     print('"{}",'.format(dt))

data_types_topic = df['topic'].unique()
# for dt in data_types_topic:
#     print('"{}",'.format(dt))

data_types_xbrl_type = df['xbrl_data_type'].unique()
# for dt in data_types_xbrl_type:
#     print('"{}",'.format(dt))

# data_types_dr_name = df[['dr', 'dr_name']].unique()
# for dt in data_types_dr_name:
#     print('"{}",'.format(dt))

print(df.groupby(['dr', 'dr_name']).size().reset_index())