import os
import time
import random
from bs4 import BeautifulSoup
import requests
import get_proxy
import sys


def save_site(link, headers='', source='source', test=False): # return soup
    os.mkdir(source) if not os.path.isdir(source) else 1
    file_name = f"{link.split('/')[-2]}_{link.split('/')[-1]}.html"
    path = os.path.join(source, file_name)
    if ('test' in ''.join(sys.argv) or test) and os.path.isfile(path) :
        with open(path, 'r', encoding='utf-8') as site_file:
            site_file = site_file.read()
            soup = BeautifulSoup(site_file, 'lxml')
    else:
        print('geting response')
        time.sleep(random.uniform(0, 1))
        
        response = requests.get(link, 
                            #cookies=cookies,
                            headers=headers, # type: ignore
                            proxies=get_proxy.proxy())
        print(response.status_code)
        soup = BeautifulSoup(response.text, 'lxml')
        if 'test' in ''.join(sys.argv) or test:
            with open(path, 'w', encoding='utf-8') as site_file:
                    site_file.write(response.text)
    return soup   

# def save_site(link, headers, source='source'): # return soup
#     file_name = f"{link.split('/')[-2]}_{link.split('/')[-1]}.html"
#     path = os.path.join(source, file_name)
#     if 'test' in ''.join(sys.argv) and os.path.isfile(path):
#         with open(path, 'r', encoding='utf-8') as site_file:
#             site_file = site_file.read()
#             soup = BeautifulSoup(site_file, 'lxml')
#     else:
#         print('geting response')
#         time.sleep(random.uniform(0, 1))
        
#         response = requests.get(link, 
#                             #cookies=cookies,
#                             headers=headers,
#                             proxies=get_proxy.proxy())
#         print(response.status_code)
#         soup = BeautifulSoup(response.text, 'lxml')
#         with open(path, 'w', encoding='utf-8') as site_file:
#                 site_file.write(response.text)
#     return soup   


def save_file(link, headers={}, cookies={}, params={}, source='./', file_type=''):
    os.mkdir(source) if not os.path.isdir(source) else 1
    file_name = f'{os.path.split(link)[-1]}{file_type}'
    path = os.path.join(source, file_name)
    print(path)
    if 'test' in ''.join(sys.argv) and os.path.isfile(path):
        img = path
    else:
        time.sleep(random.uniform(0,1))
        img_response = requests.get(link, 
                            headers=headers, # type: ignore
                            proxies=get_proxy.proxy(),
                            cookies=cookies,
                            params=params)       # type: ignore
        with open(path, 'wb') as image:
            image.write(img_response.content)
        img = path
    return img