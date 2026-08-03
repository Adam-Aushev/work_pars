from dotenv import load_dotenv
import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from torrent import kinozal, kinozal_each, rutor
from save_site import save_file

load_dotenv()
token = os.getenv('token')
chat_id = 145869859

def write_msg(message, user_id=chat_id):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id':0})

# API-ключ созданный ранее
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
tor_list = []
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            # Сообщение от пользователя
            request = event.text
            # Каменная логика ответа
            if request == "привет":
                write_msg("Хай", event.user_id) # type: ignore

            elif 'https:' in request:
                os.system(f'ssh   root@94.159.114.147  "echo {request} >> files/youtube_links.txt"')
            elif 'torrent' in request.lower() or 'торрент' in request.lower():
                key_word = request[request.strip().find(' '):]
                tor_list = rutor(key_word)
                if tor_list:
                    tor_text = ''
                    for each in tor_list[:10]:
                        tor_text += f"{tor_list.index(each)}:... {each['size']} | seed - {each['seed']} ... \n{each['text']}\n"
                    if len(tor_text) < 9000:
                        write_msg(tor_text, event.user_id) # type: ignore
                    else:
                        write_msg("Слишком много результатов", event.user_id) # type: ignore
                else:
                    write_msg('найдено 0', event.user_id) # type: ignore
            elif request.isdigit() and tor_list:
                write_msg('Файл сохранен!', event.user_id) # type: ignore
                save_file(tor_list[int(request)]['link'], source='./torrent/', file_type='.torrent')
            else:
                write_msg("Не поняла вашего ответа...", event.user_id) # type: ignore