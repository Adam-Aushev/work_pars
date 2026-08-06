import os
import subprocess
from time import sleep

def get_cmd(code):
    line_list = []
    process = subprocess.Popen(code, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
    for line in process.stdout: # type: ignore
        line_list.append(line)
    return line_list

def dow_tor(path):
    get_file = f"scp   server1:./torrent/{path}  ./torrent/"
    os.system(get_file)
    print(get_file)
    tor_dow = f' aria2c torrent/{path} -d "downloads" --seed-time=0'
    os.system(tor_dow)

if __name__ == "__main__":
    while True:
        get_file = f"ssh   server1  'ls ./torrent/'"
        tfiles_list = get_cmd(get_file)
        with open('tor_list.txt', 'r', encoding='utf-8') as tor_list:
            tor_list = tor_list.readlines()
        for each in tfiles_list:
            if each not in tor_list:
                print(each, tor_list)
                with open('tor_list.txt', 'w', encoding='utf-8') as write_tor:
                    write_tor.write(f'{each}\n')
                print('start download')
                dow_tor(each.strip())
        print(tfiles_list)
        sleep(5)