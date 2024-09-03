import os
from telethon.events import NewMessage, CallbackQuery
from modules import NewMessageHandlers, CallBackQueryHandlers, client, NewMessageGetInformationsHandlers
from modules.handlers.rules import *
from modules.database import defult_data, create_table

def main():
    
    client.add_event_handler(callback=NewMessageHandlers.cancel, event=NewMessage())
    client.add_event_handler(callback=NewMessageGetInformationsHandlers.user, event=NewMessage(func=get_informations_user))
    client.add_event_handler(callback=NewMessageGetInformationsHandlers.admin, event=NewMessage(func=get_informations_admin))
    client.add_event_handler(callback=NewMessageHandlers.user, event=NewMessage(func=user_move_text))
    client.add_event_handler(callback=NewMessageHandlers.admin, event=NewMessage(func=admin_move_text))
    client.add_event_handler(callback=NewMessageHandlers.get_url, event=NewMessage())
    client.add_event_handler(callback=CallBackQueryHandlers.user, event=CallbackQuery(func=user_move_inline))
    client.add_event_handler(callback=CallBackQueryHandlers.admin, event=CallbackQuery(func=admin_move_inline))
    

    print("Bot Runned")
    client.run_until_disconnected()


def check_db() -> None:
    if not os.path.exists(r"./database.db"):
        create_table()
        defult_data()
        
def check_directory() -> None:
    if not os.path.exists(r"./download"):
        os.mkdir(r"./download")

    if not os.path.exists(r"./download/video"):
        os.mkdir(r"./download/video")
    
    if not os.path.exists(r"./download/music"):
        os.mkdir(r"./download/music")
    
    if not os.path.exists(r"./download/image"):
        os.mkdir(r"./download/image")

if __name__ == '__main__':

    try:
        check_directory()  # check directorys, if not exist, make a new one
        check_db()  # check db, if not exist, make a new one and add default data
        main()  # run bot
    except Exception as e:
        print("error in run bot: ", e)
        