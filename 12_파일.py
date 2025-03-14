import json

data = {'name':'홍길동','age':'22'}

with open('myinfo.json','w') as f:
    json.dump(data,f,indent=2,ensure_ascii=False)

with open('myinfo.json') as f:
    data = json.load(f)

print(type(data))
print(data)

# ----------------------------------
import pickle

data = {'name':'홍길동','age':'22'}

with open('myinfo.pickle','wb') as f:
    pickle.dump(data,f)

with open('myinfo.pickle','rb') as f:
    data = pickle.load(f)

print(type(data))
print(data)