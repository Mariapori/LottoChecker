import requests
import datetime
import json
import os
year = datetime.date.today().year
week = "W" + str(datetime.date.today().isocalendar()[1])
thisweekandyear = str(year) + "-" + week
jsondata = requests.get("https://www.veikkaus.fi/api/draw-results/v1/games/LOTTO/draws/by-week/" + thisweekandyear)
data = json.loads(jsondata.content)

print("Vuosi: " + str(year))
print("Viikko: " + week.replace("W",""))
print("\r\n")
print("*** Viikon lottonumerot ***")
print("\r\n")
if len(data) > 0:
    for item in data[0]["results"][0]["primary"]:
        print("("+item+")", end=" ")
    print("\r\n")
    print("Lisänumero: " + "("+data[0]["results"][0]["secondary"][0]+")")
    print("Plus-numero: " + "("+data[0]["results"][0]["tertiary"][0]+")")
    print("\r\n")
else:   
    print("Tällä viikolla ei ole vielä arvottu lottoa.")
print("*** By Topias Mariapori ***")