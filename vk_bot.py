from dotenv import load_dotenv
import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

load_dotenv()
token = os.getenv('token')

chat_id = 145869859

def send_msg(message, user_id=chat_id):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id':0})

# API-ключ созданный ранее
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
# longpoll = VkLongPoll(vk)

# # Основной цикл
# for event in longpoll.listen():
#     # Если пришло новое сообщение
#     if event.type == VkEventType.MESSAGE_NEW:
#         # Если оно имеет метку для меня( то есть бота)
#         if event.to_me:
#             # Сообщение от пользователя
#             request = event.text
#             # Каменная логика ответа
#             if request == "привет":
#                 write_msg(event.user_id, "Хай")
