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
     if channel['id'] == "24":
        channel['manifest_url'] = "http://103.131.214.129:9985/stream/channelid/1974957513?ticket=C815D2D23BA56315B74A9234A551E2EABFC1AC91&profile=pass"
  if channel['id'] in result:
    channel['logo_url']=result[channel['id']]['channel_logo']
    channel["genres"] = [result[channel['id']]['channel_genre']]

with open("allChannels.json", "w") as channel_list_file:
        json.dump(channel_list, channel_list_file)
        channel_list_file.close()


