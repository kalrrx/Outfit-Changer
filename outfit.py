# Kalr 2019 Auto Outfit Changer.
import requests, time

session = requests.session()
session.cookies[".ROBLOSECURITY"] = '' # Put everything after the warning.

r = session.get('https://www.roblox.com/mobileapi/userinfo').json()
userid = r['UserID']
XSRFToken = (r.headers["X-CSRF-TOKEN"])

outfitlist = []

outfits = requests.get(f'https://avatar.roblox.com/v1/users/{userid}/outfits').json()
total = outfits['total']
for i in range(total):
    outfitlist.append(outfits['data'][i]['id'])
    
while True:
    try:
        for outfit in outfitlist:
            r = session.post('https://www.roblox.com/api/item.ashx?')
            d = session.post(f'https://avatar.roblox.com/v1/outfits/{outfit}/wear/', headers = {"X-CSRF-TOKEN":XSRFToken})
            print(d.json())
            print('Waiting 5 seconds')
            time.sleep(5)
    except Exception as e:
        print(e)
