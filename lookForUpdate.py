import json
import urllib.request

data = json.load(open('C:\\Users\\Manuel\\Documents\\GitHub\\ws2812-over-artnet\\config.json'))
#print(data["version"])
if (data["ignoreUpdates"] == False):
    request_url = urllib.request.urlopen('https://xilef12000.github.io/versions.json')
    web = request_url.read()
    webStr = web.decode('UTF-8')
    webData = json.loads(webStr)
    #print(webData["Xilef12000"]["ws2812-over-artnet"])
    if (data["version"] != webData["Xilef12000"]["ws2812-over-artnet"]):
        print("There is a newer Version,\nwith Version-number " + webData["Xilef12000"]["ws2812-over-artnet"] + "\nYou are currently using Version " + data["version"])
    else:
        print("You are up to date\nYour Version is " + data["version"])