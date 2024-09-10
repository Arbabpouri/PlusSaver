from telethon import Button
from typing import List, Tuple, Iterable
from config import BotConfig
from ..database import Session, Configs, engine, Channel

# region TextButton

class TextButtonsString:
    
    START_COMMAND = "/start"
    RULES_COMMAND = "/rules"
    HELP_COMMAND = "/help"
    CONTACT_US_COMMAND = "/contacts_us"
    DONATE = "/donate"
    CREATOR = "/creator"


class TextButtons:
    pass

    # START_MENU = (
        
    #     (
    #         Button.text(text=TextButtonsString.MY_ACCOUNT, resize=True, single_use=True),
    #         # Button.text(text=TextButtonsString.WITHDRAW, resize=True, single_use=True),
    #     ),
    #     (
    #         Button.text(text=TextButtonsString.DEPOSIT_PANEL, resize=True, single_use=True),
    #     ),
    #     (
    #         Button.text(text=TextButtonsString.HELP, resize=True, single_use=False),
    #         Button.text(text=TextButtonsString.RULES, resize=True, single_use=True),
    #     ),
    #     (
    #         Button.text(text=TextButtonsString.CONTACT_US, resize=True, single_use=False),
    #     ),
    # )


# endregion

# region InlineButton

class InlineButtonsData:
    BOT_STATS = "BOT_STATS"
    ADMIN_SETTING_PANEL = "ADMIN_SETTING_PANEL"
    USER_SETTING_PANEL = "USER_SETTING_PANEL"
    CHANNEL_PANEL = "CHANNEL_PANEL"
    SEND_PANEL = "SEND_PANEL"
    CHANGE_CONFIGS = "CHANGE_CONFIGS"
    ADD_ADMIN = "ADD_ADMIN"
    DELETE_ADMIN = "DELETE_ADMIN"
    SHOW_ADMINS = "SHOW_ADMIN"
    ADD_CHANNEL = "ADD_CHANNEL"
    DELETE_CHANNEL = "DELETE_CHANNEL_"
    SEND_TO_USER = "SEND_TO_USER"
    SEND_TO_USERS = "SEND_TO_USERS"
    BAN_USER = "BAN_USER"
    UNBAN_USER = "UNBAN_USER"
    SHOW_USER_INFO = "SHOW_USER_INFO"
    CHANGE_RULES_TEXT = "CHANGE_RULES_TEXT"
    CHANGE_HELP_TEXT = "CHANGE_HELP_TEXT"
    CHANGE_TRUST_CHANNEL = "CHANGE_TRUST_CHANNEL"
    JOINED_IN_CHANNEL = "JOINED_CHANNEL"
    BACK_TO_ADMIN = "BACK_TO_ADMIN"
    DONWLOAD_RESOLUTION = "DONWLOAD_RESOLUTION_"
    download_resulotion = lambda resolution: f"{InlineButtonsData.DONWLOAD_RESOLUTION}{resolution}"
    delete_channel = lambda channel_id: f"{InlineButtonsData.DELETE_CHANNEL}{channel_id}"
    

class InlineButtonString:
    BOT_STATS = "👥|امار ربات|👥"
    ADMIN_SETTING_PANEL = "👨🏻‍💻|مدیریت ادمین|🧑🏻‍💻"
    USER_SETTING_PANEL = "👀|مدیریت کاربران|👀"
    CHANNEL_PANEL = "🔐|مدیریت کانال ها|🔐"
    SEND_PANEL = "📨|بخش ارسال|📨"
    CHANGE_CONFIGS = "⚙️|تنظیمات|⚙️"
    ADD_ADMIN = "➕| افزودن ادمین"
    DELETE_ADMIN = "➖| حذف ادمین"
    SHOW_ADMINS = "👁| مشاهده ادمین ها"
    ADD_CHANNEL = "➕| افزودن کانال"
    DELETE_CHANNEL = "➖| حذف کانال"
    SEND_TO_USER = "✍🏻|پیام به کاربر|👤"
    SEND_TO_USERS = "✍🏻|پیام به کاربران|👥"
    BAN_USER = "❌| بن کردن کاربر"
    UNBAN_USER = "✅|  انبن کردن کاربر"
    SHOW_USER_INFO = "👀| مشخصات کاربر"
    CHANGE_RULES_TEXT = "⚙️| تغییر متن قوانین"
    CHANGE_HELP_TEXT = "⚙️| تغییر متن راهنما"
    CHANGE_TRUST_CHANNEL = "⚙️| تغییر کانال اعتماد"
    JOINED_IN_CHANNEL = "تایید عضویت ✅"
    BACK_TO_ADMIN = "📍 | بازگشت"
    MUSIC = "- Music"
    
    resolution = lambda resolution: f"V {resolution}"


class InlineButtons:

    BACK_TO_ADMIN = (
        Button.inline(text=InlineButtonString.BACK_TO_ADMIN, data=InlineButtonsData.BACK_TO_ADMIN),
    )

    ADMIN_PANEL = (
        (
            Button.inline(text=InlineButtonString.BOT_STATS, data=InlineButtonsData.BOT_STATS),
        ),
        (
            Button.inline(text=InlineButtonString.ADMIN_SETTING_PANEL, data=InlineButtonsData.ADMIN_SETTING_PANEL),
            Button.inline(text=InlineButtonString.USER_SETTING_PANEL, data=InlineButtonsData.USER_SETTING_PANEL)
        ),
        (
            Button.inline(text=InlineButtonString.SEND_PANEL, data=InlineButtonsData.SEND_PANEL),
            Button.inline(text=InlineButtonString.CHANNEL_PANEL, data=InlineButtonsData.CHANNEL_PANEL)
        ),
        (
            Button.inline(text=InlineButtonString.CHANGE_CONFIGS, data=InlineButtonsData.CHANGE_CONFIGS),
        ),
    )

    ADMIN_SETTING = (
        (
            Button.inline(text=InlineButtonString.ADD_ADMIN, data=InlineButtonsData.ADD_ADMIN),
            Button.inline(text=InlineButtonString.DELETE_ADMIN, data=InlineButtonsData.DELETE_ADMIN)
        ),
        (
            Button.inline(text=InlineButtonString.SHOW_ADMINS, data=InlineButtonsData.SHOW_ADMINS),
        ),
        BACK_TO_ADMIN
    )

    USER_SETTING = (
        (
            Button.inline(text=InlineButtonString.BAN_USER, data=InlineButtonsData.BAN_USER),
            Button.inline(text=InlineButtonString.UNBAN_USER, data=InlineButtonsData.UNBAN_USER),
        ),
        (
            Button.inline(text=InlineButtonString.SHOW_USER_INFO, data=InlineButtonsData.SHOW_USER_INFO),
        ),
        BACK_TO_ADMIN
    )

    SEND_PANEL = (
        (
            Button.inline(text=InlineButtonString.SEND_TO_USER, data=InlineButtonsData.SEND_TO_USER),
            Button.inline(text=InlineButtonString.SEND_TO_USERS, data=InlineButtonsData.SEND_TO_USERS)
        ),
        BACK_TO_ADMIN
    )

    CONFIGS_PANEL = (
        (
            Button.inline(text=InlineButtonString.CHANGE_RULES_TEXT, data=InlineButtonsData.CHANGE_RULES_TEXT),
        ),
        (
            Button.inline(text=InlineButtonString.CHANGE_HELP_TEXT, data=InlineButtonsData.CHANGE_HELP_TEXT),
        ),
        (
            Button.inline(text=InlineButtonString.CHANGE_TRUST_CHANNEL, data=InlineButtonsData.CHANGE_TRUST_CHANNEL),
        ),
        BACK_TO_ADMIN
    )

    CHECK_JOINED = (
        Button.inline(text=InlineButtonString.JOINED_IN_CHANNEL, data=InlineButtonsData.JOINED_IN_CHANNEL),
    )

    @staticmethod
    def channels_panel(channels: Iterable[Channel]) -> List[Tuple[Channel]]:
        
        buttons = []

        for channel in channels:
            buttons.append(
                (
                    Button.inline(text=InlineButtonString.DELETE_CHANNEL, data=InlineButtonsData.delete_channel(channel.channel_id)),
                    Button.url(text=channel.channel_name, url=channel.channel_url),
                )
            )

        buttons.append(
            (
                Button.inline(text=InlineButtonString.ADD_CHANNEL, data=InlineButtonsData.ADD_CHANNEL),
            )
        )
        buttons.append(InlineButtons.BACK_TO_ADMIN)

        return buttons
        
        
    @staticmethod
    def select_resolution() -> List[Tuple[Button]]:
        """This function for select video resolutions or music

        Returns:
            List[Tuple[Button]]: a list from telethon buttons
        """
        buttons = []
        
        
        return buttons

# endregion

# region UrlButton


class UrlButtonString:
    CONTACT_US = "✍🏻| Message to admin |✍🏻"
    HELP_CHANNEL = "⁉| Support channel |⁉"
    ADD_TO_GROUP = "➕| Add To Group |➕"


class UrlButtons:
    
    
    CONTACT_US = (
        (
            Button.url(text=UrlButtonString.CONTACT_US, url=f"t.me/{BotConfig.SUPPORT_USERNAME}"),
        ),
    )

    ADD_TO_GROUP = (
        (
            Button.url(text=UrlButtonString.ADD_TO_GROUP, url=f"https://t.me/{BotConfig.BOT_USERNAME}?startgroup=add"),
        ),
    )

    @staticmethod
    def trust_channel() -> Tuple[Tuple[Button]]:
        with Session(engine) as session:
            info = session.query(Configs).first()
        
        return (
            (
                Button.url(text=UrlButtonString.HELP_CHANNEL, url=info.support_channel_url)
            ),
        )
    

    @staticmethod
    def channels_locked(channels: Iterable[Channel]) -> List[Tuple[Button]]:
        
        buttons = []

        for channel in channels:
            
            try:
                buttons.append((Button.url(text=channel.channel_name, url=channel.channel_url),))
            except Exception as e:
                print(e)

        buttons.append(InlineButtons.CHECK_JOINED)

        return buttons


# endregion
