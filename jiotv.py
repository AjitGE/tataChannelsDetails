import requests;
import json;

global allChannels
url= "https://jtv69.nayeem-parvez.workers.dev/bpk-tv/$ToReplace/Fallback/index.m3u8"
m3ustr = ''
with open("jiodata.json", "r") as savedChannelDetailInFile:
    savedChannels = json.load(savedChannelDetailInFile)
allchannels=savedChannels

for channelList in allchannels:
        channelUrlId=channelList['logoUrl'].split('https://jiotv.catchup.cdn.jio.com/dare_images/images/')[1].replace('.png','')
        m3ustr += "#EXTINF:-1 "
        m3ustr += "tvg-id="+ "\"" + str(channelList['channel_id']) + "\" " + "group-title=" + "\"" + channelList['channelCategoryId'] + "\" " "tvg-logo=\""+str(channelList['logoUrl']) + "\"," + channelList['channel_name'] + "\n"+ url.replace("$ToReplace",channelUrlId+'_MOB')+"\n\n"


with open("allChannelPlaylist.m3u", "w") as allChannelPlaylistFile:
        allChannelPlaylistFile.write(m3ustr)
