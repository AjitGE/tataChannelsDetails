import requests;
import json;

global allChannels
url= "https://cricfy.nayeemparvez-jtv.workers.dev/bpk-tv/$ToReplace/Fallback/index.m3u8"
m3ustr = '#EXTM3U x-tvg-url="https://raw.githubusercontent.com/mitthu786/tvepg/main/jiotv/epg.xml.gz"\n\n'
with open("jiodata.json", "r") as savedChannelDetailInFile:
    savedChannels = json.load(savedChannelDetailInFile)
allchannels=savedChannels

for channelList in allchannels:
        m3ustr += "#EXTINF:-1 "
        m3ustr += "tvg-id="+ "\"" + str(channelList['channel_id']) + "\" " + "group-title=" + "\"" + channelList['channelCategoryId'] + "\" " "tvg-logo=\""+str(channelList['logoUrl']) + "\"," + channelList['channel_name'] + "\n"+ url.replace("$ToReplace",'_'.join(channelList['channel_name'].split(" ")))+"\n\n"


with open("allChannelPlaylist.m3u", "w") as allChannelPlaylistFile:
        allChannelPlaylistFile.write(m3ustr)