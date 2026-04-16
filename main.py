from urllib.parse import unquote
import json
import os 
from bs4 import BeautifulSoup
import time 
import unicodedata
from dotenv import load_dotenv
from vk_bot import send_msg








def get_telechanel(channel, source_dir):
    scrape_line = f'snscrape --max-results 10 --jsonl telegram-channel {channel} > {source_dir}/{channel}.txt'
    os.system(scrape_line)
    print(channel, '- update list')
    info_list = []
    with open(f'{source_dir}/{channel}.txt', 'r', encoding='utf-8') as channel_file:
        for each in channel_file:
            url = json.loads(each)['url']
            content = unicodedata.normalize('NFKD', str(json.loads(each)['content']))
            info_list.append({'url':url, 'content':content})
    return info_list # type: ignore







if __name__ == "__main__":
    while True:
        send_msg('we_start')
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        channels = ['jobforjunior', 'pythonrabota', 'forpython', 'job_python',
                'runello_rus_python', 'devs_it', 'geekjobs']
        # channels = ['jobforjunior', 'pythonrabota']
        channels_list = []
        source_dir = os.path.join(os.path.dirname(__file__), 'source')
        os.mkdir(source_dir) if not os.path.isdir(source_dir) else 1
        for each in channels:
            channels_list += (get_telechanel(each, source_dir))
        info_base_file = 'info_base.json'
        
        local_base = []
        new_posts = []
        if os.path.isfile(info_base_file):
            with open(info_base_file, 'r', encoding='utf-8') as info_base:
                local_base = json.load(info_base)
        for each in channels_list:
            if each not in local_base:
                local_base.append(each)
                new_posts.append(each)
        with open(info_base_file, 'w', encoding='utf-8') as info_base:
            json.dump(local_base, info_base, ensure_ascii=False, indent=4)

        remote = ['remote', 'удален', 'удалённ']
        specific = ['python', 'ffmpeg', 'okko', 'kion', 'kinopoisk', 'intern', 'стаж']
        redflags = ['senior', 'серьер', 'middle', 'мидл']
        for each_post in new_posts:
            remote_verifi = any([True for each in remote if each in each_post['content'].lower()]) 
            specific_verifi = any([True for each in specific if each in each_post['content'].lower()]) 
            redflags_verifi = not any([True for each in redflags if each in each_post['content'].lower()]) 


            # print([True for each in 'seni' if each not in each_post['content'].lower()])
            # print(remote_verifi, specific_verifi, redflags_verifi)
            if all([remote_verifi, specific_verifi, redflags_verifi]):
                print(each_post)

                send_msg(f'{each_post["url"]} {each_post["content"]}')
        
        time.sleep(3600)