import requests;
import json;

global allChannels
with open("config.json", "r") as savedChannelDetailInFile:
    savedChannels = json.load(savedChannelDetailInFile)
allchannels=savedChannels

result = dict()
for channel in allchannels:
    result[channel['channel_id']] = channel

url = "https://lust.toxicify.pro/api/toxicify.json"

payload = {}
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-IN,en-GB;q=0.9,en;q=0.8,en-US;q=0.7',
  'cache-control': 'max-age=0',
  'cookie': 'PHPSESSID=650b689001ff4c40802f8823a85fc2b3',
  'dnt': '1',
  'priority': 'u=0, i',
  'referer': 'https://web.telegram.org/',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response)
channel_list = response.json()['data']


for channel in channel_list:
  if channel['id'] in result:
    channel['logo_url']=result[channel['id']]['channel_logo']
    channel["genres"] = [result[channel['id']]['channel_genre']]

with open("allChannels.json", "w") as channel_list_file:
        json.dump(channel_list, channel_list_file)
        channel_list_file.close()