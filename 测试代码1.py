import json
import datetime
time = str(datetime.datetime.now())
lyb = [["吴豆豆","统一祖国 振兴中华",time[:-10]]]
print(lyb)
with open("lyb_json.json","w") as f:
    json.dump(lyb,f)
    