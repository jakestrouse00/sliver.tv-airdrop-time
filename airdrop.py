import requests


def getDrop():
    r = requests.get('https://airdrop-manager.appspot.com/campaign/next') # make the get request
    startTime = r.json()['body']['campaigns'][0]['start_time'] # the droptime of the airdrop in Epoch
    prizes = r.json()['body']['campaigns'][0]['prizes'] # a list of all the prize ID's
    prizesm = []
    # apending the prizes to a new list
    for item in prizes:
        prizesm.append(item)
    return prizesm, startTime


drop = getDrop()
prizes = drop[0]
startTime = drop[1]

print(f"The airdrop starts at {startTime}")
print(f"The prize ID's are: {prizes}")
