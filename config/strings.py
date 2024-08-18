from typing import Iterable
from modules.database import User, Channel
from modules.handlers.buttons import TextButtonsString
from .config import BotConfig


class Strings:

    ADMIN_PANEL = "💢 به پنل ادمین خوش آمدید"
    CONTACT_US = "💬 Message To Admin 👇"
    SELECT = "⭕️ یک مورد را انتخاب کنید👇"
    BACKED = "🔙 بازگشتید"
    NEW_UPDATE = "💭 در اپدیت های بعدی اضافه میشود"
    CANCEL =  "📍 برای کنسل کردن از /cancel استفاده کنید"
    CANCELED = "❤ عملیات با موفقیت کنسل شد"
    DELETED = "❌ با موفقیت حذف شد"
    ADDED = "✅ با موفقیت اضافه شد"
    NO_YOU = "⛔ نمیتوانید روی خود کاری کنید"
    IS_CREATOR = "⛔ ایشان سازنده ربات است"
    USER_EXIST = "👤 این شخص در لیست وجود دارد"
    USER_NOT_EXIST = "👤 این شخص در لیست وجود ندارد, دقت کنید"
    ENTER_USER_ID = f"🔢 لطفا ایدی عددی را ارسال کنید\n\n{CANCEL}"
    ENTER_TEXT = f"📜 لطفا متن را ارسال کنید : \n\n{CANCEL}"
    ENTER_VALUE = f"📊 لطفا مقدار را وارد کنید : \n\n{CANCEL}"
    ADD_CHANNEL = f"📌 لطفا ابتدا ربات را در کانال ادمین کرده و سپس یک پیام از کانال برای ربات فورارد کنید \n\n {CANCEL}"
    ENTER_URL = f"🔑 لطفا لینک را ارسال کنید : \n\n{CANCEL}"
    PLEASE_START_BOT = "⚠ باید اول ربات را استارت کند"
    ENTER_NUMBER = "⛔ فقط مقدار عددی وارد کنید ⛔"
    BOT_NOT_ADMIN = "🤖 ربات ادمین نیست"
    ERROR = "⁉💔 مشکلی پیش امد لطفا مجدد تلاش کنید و اگر چندمین بار است این پیام را میبینید به برنامه نویس گزارش کنید"
    UPDATED = "💥 اپدیت شد"
    TEXT_IS_LONG = "❌ تعداد کاراکتر های ارسالی زیاد است لطفا کوتاه تر کنید"
    ENTER_MESSAGE = "💎 لطفا پیام خود را ارسال کنید"
    SENDING = "📌 درحال ارسال . . ."
    CHANNEL_ALREADY_EXIST = "⚠ این کانال وجود دارد لطفا کانال دیگری را ارسال کنید"
    JOIN_TO_CHANNELS = "⚠ برای فعالیت در ربات باید عضو کانال های زیر بشوید"
    CREATOR = f"👨‍💻 - https://t.me/{BotConfig.SUPPORT_USERNAME}"
    DONATE = f"❤ come to my pv {TextButtonsString.CONTACT_US_COMMAND}"

    START_MENU = (
        "🤖 Hi, I'm a fast downloader of videos and audios from Instagram, TikTok, YouTube, Likee and Pinterest.\n\n"

        "To download, send the video or audio link: 🔻\n\n"

        "(Now I can also upload media in groups, you need me in your group for that)\n\n"
    )

    @staticmethod
    def bot_stats(users: int, channels: int) -> str:
        return (
            f"🫂 | کاربران : {users}\n"
            f"🔐 | کانال های قفل شده : {channels}\n"
        )
    
    @staticmethod
    def show_admins(admins: Iterable[User]) -> str:
        message = "👥 ادمین ها : \n\n"
        for index, admin in enumerate(admins):
            message += f"👤 <b>{index}</b> - <code>{admin.user_id}</code> \n"

        return message
    
    @staticmethod
    def message_sended(success_num: int) -> str:
        return f"👥 پیام شما با موفقیت برای {success_num} نفر ارسال شد"
    
    @staticmethod
    def channel_deleted(channel: Channel) -> str:
        return (
            "📌 کانال به مشخصات زیر به خاطر حذف ربات از ادمین ها دیلیت شد\n\n"
            f"🔸 id : {channel.channel_id}\n"
            f"🔸 title : {channel.channel_name}\n"
            f"🔸 url : {channel.channel_url}\n"
        )
