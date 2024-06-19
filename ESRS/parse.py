import pandas as pd
import json
import uuid
import hashlib

def create_uuid_from_string(val: str):
    hex_string = hashlib.md5(val.encode("UTF-8")).hexdigest()
    return uuid.UUID(hex=hex_string)

esrs_topics = ["General Disclosures", "Climate Change", "Pollution", "Water and Marine Resources", "Biodiversity and Ecosystems", "Resource Use and Circular Economy", "Own Workforce", "Workers in the Value Chain", "Affected Communities", "Consumers and End-users", "Business Conduct"]

file_path = 'esrs_data_points.xlsx'

renaming = {
    "ID": "datapoint_id", 
    "ESRS": "esrs", 
    "DR": "dr", 
    "Paragraph": "paragraph", 
    "Related AR ": "related_ar", 
    "Related AR": "related_ar",
    "Name": "name", 
    "Data Type": "data_type", 
    "Conditional or alternative DP": "conditional_or_alternative_dp", 
    "May \n[V]": "may_v", 
    """Appendix B - ESRS 2 \n(SFDR + PILLAR 3 + Benchmark + CL)""": "appendix_b", 
    "Appendix C - ESRS 1\nDPs subject to phasing-in provisions applicable to undertaking with less than 750 employees": "appendix_c_phase_in_750",
    "DPs to be disclosed in case of phased-in [Appendix C - ESRS 1]\nUndertaking less than 750 employees": "appendix_c_phase_in_750", 
    "Appendix C - ESRS 1\n[DPs subject to phased-in]\n": "appendix_c_phase_in_all",
    "Appendix C - ESRS 1\nDPs subject to phasing-in provisions applicable to all undertakings ": "appendix_c_phase_in_all"}

esrs_2 = pd.read_excel(file_path, sheet_name=1, skiprows=1).rename(columns=renaming)
esrs_2['uuid'] = esrs_2.apply(lambda x: create_uuid_from_string(x["datapoint_id"]), axis=1)
esrs_2["esrs_code"] = "esrs_2"

# esrs_2_mdr = pd.read_excel(file_path, sheet_name=2, skiprows=1).rename(columns=renaming)
# esrs_2_mdr['uuid'] = esrs_2_mdr.apply(lambda _: uuid.uuid4(), axis=1)
# esrs_2_mdr["esrs_code"] = "esrs_2_mdr"

esrs_e1 = pd.read_excel(file_path, sheet_name=3, skiprows=1).rename(columns=renaming)
esrs_e1['uuid'] = esrs_e1.apply(lambda x: create_uuid_from_string(x["datapoint_id"]), axis=1)
esrs_e1["esrs_code"] = "esrs_e1"

esrs_e2 = pd.read_excel(file_path, sheet_name=4, skiprows=1).rename(columns=renaming)
esrs_e2['uuid'] = esrs_e2.apply(lambda x: create_uuid_from_string(x["datapoint_id"]), axis=1)
esrs_e2["esrs_code"] = "esrs_e2"

esrs_e3 = pd.read_excel(file_path, sheet_name=5, skiprows=1).rename(columns=renaming)
esrs_e3['uuid'] = esrs_e3.apply(lambda x: create_uuid_from_string(x["datapoint_id"]), axis=1)
esrs_e3["esrs_code"] = "esrs_e3"

esrs_e4 = pd.read_excel(file_path, sheet_name=6, skiprows=1).rename(columns=renaming)
esrs_e4['uuid'] = esrs_e4.apply(lambda x: create_uuid_from_string(x["datapoint_id"]), axis=1)
esrs_e4["esrs_code"] = "esrs_e4"

esrs_e5 = pd.read_excel(file_path, sheet_name=7, skiprows=1).rename(columns=renaming)
esrs_e5['uuid'] = esrs_e5.apply(lambda x: create_uuid_from_string(x["datapoint_id"]), axis=1)
esrs_e5["esrs_code"] = "esrs_e5"

esrs_s1 = pd.read_excel(file_path, sheet_name=8, skiprows=1).rename(columns=renaming)
esrs_s1['uuid'] = esrs_s1.apply(lambda x: create_uuid_from_string(x["datapoint_id"]), axis=1)
esrs_s1["esrs_code"] = "esrs_s1"

esrs_s2 = pd.read_excel(file_path, sheet_name=9, skiprows=1).rename(columns=renaming)
esrs_s2['uuid'] = esrs_s2.apply(lambda x: create_uuid_from_string(x["datapoint_id"]), axis=1)
esrs_s2["esrs_code"] = "esrs_s2"

esrs_s3 = pd.read_excel(file_path, sheet_name=10, skiprows=1).rename(columns=renaming)
esrs_s3['uuid'] = esrs_s3.apply(lambda x: create_uuid_from_string(x["datapoint_id"]), axis=1)
esrs_s3["esrs_code"] = "esrs_s3"

esrs_s4 = pd.read_excel(file_path, sheet_name=11, skiprows=1).rename(columns=renaming)
esrs_s4['uuid'] = esrs_s4.apply(lambda x: create_uuid_from_string(x["datapoint_id"]), axis=1)
esrs_s4["esrs_code"] = "esrs_s4"

esrs_g1 = pd.read_excel(file_path, sheet_name=12, skiprows=1).rename(columns=renaming)
esrs_g1['uuid'] = esrs_g1.apply(lambda x: create_uuid_from_string(x["datapoint_id"]), axis=1)
esrs_g1["esrs_code"] = "esrs_g1"

#mdr omitted
all_esrs = [esrs_2, esrs_e1, esrs_e2, esrs_e3, esrs_e4, esrs_e5, esrs_s1, esrs_s2, esrs_s3, esrs_s4, esrs_g1]

df = pd.DataFrame({})

for i in range(len(all_esrs)):
    all_esrs[i]["topic"] = esrs_topics[i]
    df = df.append(all_esrs[i])

def assert_voluntary(key, x):
    if x == key:
        return True
    if x is None:
        return False
    else:
        return False
    
def get_phase_in_time(indicator, esrs_code):
    if indicator == True and esrs_code == "esrs_e4":
        return 2
    if indicator == True and esrs_code == "esrs_s1":
        return 1
    if indicator == True and esrs_code == "esrs_s2":
        return 2
    if indicator == True and esrs_code == "esrs_s3":
        return 2
    if indicator == True and esrs_code == "esrs_s4":
        return 2
    
df.reset_index(inplace=True)
df["paragraph"] = df["paragraph"].apply(lambda x: str(x))
df["appendix_c_phase_in_750"] = df["appendix_c_phase_in_750"].apply(lambda x: assert_voluntary("Y", x))
df["appendix_c_750_phase_in_years"] = df.apply(lambda x: get_phase_in_time(x["appendix_c_phase_in_750"], x["esrs_code"]), axis=1)
df["appendix_c_phase_in_all"] = df["appendix_c_phase_in_all"].apply(lambda x: assert_voluntary("Y", x))
df["may_v"] = df["may_v"].apply(lambda x: assert_voluntary("V", x))
df["data_type"] = df["data_type"].str.lower()
df["data_type"] = df["data_type"].str.strip()
df["dr"] = df["dr"].str.strip()


# print("Length", len(df))
# print("Unique", df.uuid.nunique())

def dt_to_xbrl(dt):
    try:
        r = dt.split("/")[0]
        if "table" in r:
            return "Table"
        if "narrative" in r:
            return "Narrative"
        if "mdr" in r:
            if "mdrp" or "mdr-p" in r:
                return "MDR-P"
            if "mdra" or "mdr-a" in r:
                return "MDR-A"
            if "mdrt" or "mdr-t" in r:
                return "MDR-T"
            if "mdr_no_t" in r:
                return "NO MDR-T"
        if "integer" in r:
            return "Integer"
        if "monetary" in r:
            return "Monetary"
        if "percent" in r:
            return "Percent"
        if "gyear" in r:
            return "Gyear"
        if "date" in r:
            return "Date"
        if "mass" in r:
            return "Mass"
        if "area" in r:
            return "Area"
        if "decimal" in r:
            return "Decimal"
        if "intensity" in r:
            return "Intensity"
        if "volume" in r:
            return "Volume"
        if "energy" in r:
            return "Energy"
        else:
            return dt
    except:
        return None



## Remove whitespace from 'dr' <---
with open("mapping.json", "r") as f:
    mapping = dict(json.load(f))

def dr_to_dr_name(dr):
    if "mdr" in dr: 
        return None
    return mapping[dr]["name"]

def dr_to_dr_link(dr):
    if "mdr" in dr: 
        return None
    return f'https://xbrl.efrag.org/e-esrs/esrs-set1-2023.html#{mapping[dr]["html_id"]}'

def dr_to_dr_reporting_area(dr):
    if "mdr" in dr: 
        return None
    return mapping[dr]["reporting_area"]



df["xbrl_data_type"] = df.apply(lambda x: dt_to_xbrl(x["data_type"]), axis=1)
df["dr_name"] = df.apply(lambda x: dr_to_dr_name(x["dr"]), axis=1)
df["dr_link"] = df.apply(lambda x: dr_to_dr_link(x["dr"]), axis=1)
df["dr_reporting_area"] = df.apply(lambda x: dr_to_dr_reporting_area(x["dr"]), axis=1)

# data_types_unique =  df['dr_link'].tolist()

# # print("DATA TYPES ->", len(data_types_unique))
# # for dt in data_types_unique:
# #     print('"{}"'.format(dt), " | ")

pd.set_option('display.max_columns', None)
print(df.head(5))

outjson = df.to_json(orient="records", default_handler=str)
with open('esrs.json', 'w') as f:
    f.write(outjson)
