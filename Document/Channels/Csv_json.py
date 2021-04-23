import json
import csv

with open(r'H:\Channels\MRP_Pay_channel_v2.csv') as f:
    reader = csv.DictReader(f)
    channels_csv = [r for r in reader]

with open(r'H:\Channels\channels.json') as f:
    channels_json = json.loads(f.read())
    # json.dump(data, write_file)

print(channels_json[0]["channel_name"])
print(channels_csv[0]["channel_name"])

print(len(channels_csv))
print(len(channels_json))

for i in range(len(channels_csv)):
    channels_json[i]["channel_name"] = channels_csv[i]["channel_name"]
    channels_json[i]["channel_genre"] = channels_csv[i]["channel_genre"]
    channels_json[i]["channel_language"] = channels_csv[i]["channel_language"]
    channels_json[i]["channel_price"] = channels_csv[i]["channel_price"]
    channels_json[i]["channel_quality"] = channels_csv[i]["channel_quality"]

with open('channels_v1.json', 'w') as outfile:
    json.dump(channels_json, outfile)