import pandas as pd
import json
import uuid
import hashlib
def create_uuid_from_string(val: str):
    hex_string = hashlib.md5(val.encode("UTF-8")).hexdigest()
    return uuid.UUID(hex=hex_string)

rename_schema = {
    "uuid": "uuid",
    "datapoint_id": "datapointId",
    "name": "datapointName",
    "esrs": "esrs",
    "dr": "disclosureRequirement",
    "dr_name": "drName",
    "dr_link": "drLink",
    "paragraph": "paragraph",
    "topic": "topic",
    "xbrl_data_type": "xbrlDataType",
    "dr_reporting_area": "reportingArea"
}

keep_cols = [
    "uuid", "datapointId", "datapointName", "esrs", "disclosureRequirement", "drName","drLink", "paragraph", "topic", "xbrlDataType", "reportingArea"
]

df = pd.read_json("esrs.json").rename(columns=rename_schema)
df = df[keep_cols]

# data_types_topic = df['esrs'].unique()
# for dt in data_types_topic:
#     print('"{}",'.format(dt))

new = df[['esrs', 'disclosureRequirement', 'drLink', 'topic', 'reportingArea', 'drName']]
new = new.groupby(['esrs', 'disclosureRequirement', 'drLink', 'topic', 'reportingArea', 'drName']).size().reset_index()

print(new)

new['uuid'] = new.apply(lambda x: create_uuid_from_string(x["disclosureRequirement"]), axis=1)
outjson = new[['uuid', 'esrs', 'disclosureRequirement', 'drLink', 'topic', 'reportingArea', 'drName']].to_json(orient="records", default_handler=str)
with open('drs-typed.json', 'w') as f:
    f.write(outjson)

