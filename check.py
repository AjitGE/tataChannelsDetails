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
for channel in allchannelsnew:
    result[channel['channel_id']] = channel

for channelnew in channel_list:
  if channelnew['id'] in result:
        channelnew['channel_license_url']=result[channelnew['id']]['license_url']
        channelnew['channel_url'] = result[channelnew['id']]['manifest_url']
  else :
     print(channelnew['id'])

with open("allChannelsCheck.json", "w") as channel_list_file:
        json.dump(allchannelsnew, channel_list_file)
        channel_list_file.close()


