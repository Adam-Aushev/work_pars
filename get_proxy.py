import requests
import os
import json
from dotenv import load_dotenv
from random import randint, choice

load_dotenv(dotenv_path="./.env")

def proxy(return_proxy=''):
    url = os.getenv('proxy_url')
    if not os.path.isfile('proxy_file.json'):
        respose = requests.get(url) # type: ignore
        proxy_dict = respose.text
        with open('proxy_file.json', 'w', encoding='utf-8') as proxy_file:
            json.dump(json.loads(proxy_dict), proxy_file, indent=4)
    with open('proxy_file.json', 'r', encoding='utf-8') as proxy_file:
        proxy_dict = json.loads(proxy_file.read())
    if return_proxy:
        proxy_num = [each for each in proxy_dict if each.isdigit()]
        for each in proxy_num:
            if proxy_dict[each]['name'] == return_proxy:
                if 'wrong_status' in proxy_dict[each]:
                    proxy_dict[each]['wrong_status'] = proxy_dict[each]['wrong_status'] +1
                else:
                    proxy_dict[each]['wrong_status'] = 0
            if 'wrong_status' in proxy_dict[each] and proxy_dict[each]['wrong_status'] > 4:
                del proxy_dict[each]
        
        with open('proxy_file.json', 'w', encoding='utf-8') as proxy_file:
            json.dump(proxy_dict, proxy_file, indent=4)
    proxy_num = [each for each in proxy_dict if each.isdigit()]
    return {proxy_dict[str(choice(proxy_num))]['type']: proxy_dict[str(choice(proxy_num))]['name']}