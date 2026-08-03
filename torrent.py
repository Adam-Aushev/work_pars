from urllib.parse import unquote, quote
import requests
from bs4 import BeautifulSoup
from save_site import save_site, save_file
from site_params import *
import unicodedata


def rutor(keywords):
    host = 'https://rutor.info/'
    args = 'search/0/0/000/2/'
    url = f'{host}{args}{quote(keywords)}'
    info = []
    soup = save_site(url, headers=headers)
    soup = soup.find(id='index')
    soup = soup.find('table')  # type: ignore
    film_line = soup.find_all(True, {'class':['gai', 'tum']}) # type: ignore
    # film_line.append(soup.find_all(class_='tum'))
    if film_line:
        for each in film_line:
            dict_info = {}
            each_info = each.find('td').next.next # type: ignore
            dict_info['link'] = f"https:{each_info.find(class_='downgif').get('href')}" #type: ignore
            each_info = each_info.find(class_='downgif').next.next.next.next.next # type: ignore
            dict_info['text'] = each_info.text # type: ignore
            dict_info['size'] = unicodedata.normalize('NFKC', each.find_all(align='right')[-1].text)
            dict_info['seed'] = unicodedata.normalize('NFKC', each.find(align='center').find(class_='green').text) # type: ignore
            # dict_info['size'] = unquote(each.find_all(align='right')[-1].text, encoding='ISO 8859‑1')
            # dict_info['link'] = f'{host}{each_info.get('href')[1:]}'
            info.append(dict_info.copy())
    print(info)
    return info


def kinozal(words):
    host = 'https://kinozal.tv/browse.php?s='
    params = '&g=0&c=0&v=0&d=0&w=0&t=1&f=0'
    keywords = quote(words, encoding='Windows‑1251')
    url = f'{host}{keywords}{params}'
    soup = save_site(url)
    films = soup.find(class_='t_peer')
    if films != None:
        films = films.find_all(class_='bg')
        each_info = {}
        info_list = []
        for each in films:
            each_info['link'] = f"https://kinozal.tv{each.find('a').get('href')}" # type: ignore
            each_info['name'] = each.find('a').text # type: ignore
            each_info['size'] = each.find_all(class_ = 's')[1].text
            each_info['seeds'] = each.find(class_='sl_s').text # type: ignore
            info_list.append(each_info.copy())
        for each in info_list:
            print(each['name'], each['seeds'])
        return info_list
    else:
        print(soup.text)
        return None

def kinozal_each(link):
    soup = save_site(link)
    file_link = soup.find(class_='mn1_content').find(class_='w100p') # type: ignore
    file_link = file_link.find('a').get('href') # type: ignore
    file_link = f'https://kinozal.tv/{file_link}'
    print(link)
    save_file(file_link, # type: ignore
               headers=headers,
               cookies=cookies,
               params=params,
                source='./')
if __name__ == "__main__":
    rutor('drama')
