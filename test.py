import requests
import config

import tg
# res= tg.method('deleteWebhook',{'url':'https://runweb.temp.swtest.ru/tg/'})
# print(res.text)
# # print(res.text)
# # config.myapi='http://localhost:4000/api/'
res = requests.get(config.myapi+'setupdates',json={'update':'off','target':'all'})
print(res.json())
# res=requests.po   st(config.myapi+'bot_off',json={'id':1})
# # res=requests.get(config.myapi+'get_updates',json={'target':1})
# # print(res.json())