import requests;
import json;

global allChannels
with open("config.json", "r") as savedChannelDetailInFile:
    savedChannels = json.load(savedChannelDetailInFile)
allchannelsnew=savedChannels


url = "https://tplayapi.code-crafters.app/321codecrafters/fetcher.json"
x = requests.get(url)
channel_list = x.json()['data']['channels']

result = dict()
for channel in channel_list:
    result[channel['id']] = channel

for channelnew in allchannelsnew:
  if channelnew['channel_id'] in result:
        channelnew['channel_license_url']=result[channelnew['channel_id']]['license_url']
        channelnew['channel_url'] = result[channelnew['channel_id']]['manifest_url']

with open("allChannelsNew.json", "w") as channel_list_file:
        json.dump(allchannelsnew, channel_list_file)
        channel_list_file.close()


