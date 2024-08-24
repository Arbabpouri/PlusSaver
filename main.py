from sys import argv
import os
from telethon.events import NewMessage, CallbackQuery
from modules import NewMessageHandlers, CallBackQueryHandlers, client, NewMessageGetInformationsHandlers
from sqlalchemy import exc
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

if __name__ == '__main__':

    try:
        check_db()
        main()
    except Exception as e:
        print("error in run bot: ", e)
        