import requests;
import json;

global allChannels
with open("config.json", "r") as savedChannelDetailInFile:
    savedChannels = json.load(savedChannelDetailInFile)
allchannels=savedChannels

result = dict()
for channel in allchannels:
    result[channel['channel_id']] = channel


url = "https://tplayapi.code-crafters.app/321codecrafters/fetcher.json"
x = requests.get(url)
channel_list = x.json()['data']['channels']


for channel in channel_list:
  if channel['id'] in result:
    channel['logo_url']=result[channel['id']]['channel_logo']
    channel["genres"] = [result[channel['id']]['channel_genre']]

with open("allChannels.json", "w") as channel_list_file:
        json.dump(channel_list, channel_list_file)
        channel_list_file.close()


