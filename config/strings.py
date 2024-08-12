from typing import Iterable
from modules.database import User, Configs, Channel
from .config import BotConfig


class Strings:
    START_MENU = "🔹 سلام به ربات خوش اومدی, از منوی زیر انتخاب کن :"
    ADMIN_PANEL = "💢 به پنل ادمین خوش آمدید"
    CONTACT_US = "💬 تنها جهت پیگیری برداشتتان پیام دهید👇"
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
    # GET_PAY = f"💰 لطفا TXID تراکنش یا اسکرین شات ارسال را ارسال کنید و منتظر تایید باشید\n\n{CANCEL}"
    # WAIT_FOR_CHECK = "🔸 لطفا منتظر بمانید تا بررسی شود"
    # PAY_GETED = "📌 مدارک ارسالی شما دریافت شد منتظر پاسخ باشید"
    # PAY_NOT_GETED = "❌ مدرک دریافتی برای ادمین ارسال نشد لطفا از طریق پشتیبانی اقدام فرمایید"
    # REJECTED = "❌ رد شد"
    # PAY_REJECTED = "❌ درخواست شما توسط ادمین رد شد"
    # ACCPTED = "✅ قبول شد"
    # PAY_ACCEPTED = "✅ درخواست شما توسط ادمین قبول شد"
    # GET_PAY_AMOUNT = f"📍 لطفا مقداری رو که میخواید کاربر رو شارژ کنید وارد کنید\n\n{CANCEL}"
    # CHECK_PV = "پی ویو چک کن و مقدار رو وارد کنید عزیزمممم ❤"
    # NEED_REFERRAL = "❌ برای برداشت نیاز به 10 زیرمجموعه دارید"
    # ENTER_AMOUNT = f"📍 مقدار مبلغ را وارد کنید\n\n{CANCEL}"
    # BAD_AMOUNT = "🔸 مقدار ارسالی اشتباه است لطفا دقت کنید از موجودی خود بالاتر نباشد"
    # ENTER_WALLET = f"📜 لطفا ایدی ولت ترون خود را ارسال کنید\n\n{CANCEL}"
    # REQUEST_GETED = "✅ درخواست شما ارسال شد لطفا منتظر بمانید"
    # REQUEST_NOT_GETED = "❌ درخواست شما برای ادمین ارسال نشد لطفا این مشکل را به پشتیبانی گزارش دهید"
    # ENTER_TXID = f"💰 لطفا txid را وارد کنید : \n\n{CANCEL}"


    @staticmethod
    def bot_stats(users: int, channels: int) -> str:
        return (
            f"🫂 | کاربران : {users}\n"
            f"🔐 | کانال های قفل شده : {channels}\n"
        )
    
    @staticmethod
    def my_account(user: User) -> str:
        return (
            f"🔢 شناسه عددی : <code>{user.user_id}</code>\n\n"
            f"💳 موجودی شما : {user.balance:,} تومان\n\n"
            f"👥 تعداد زیر مجموعه های شما : {len(user.user_referrals)}"
        )
    
    @staticmethod
    def referral_banner(user_id: int, referral_info: Configs) -> str:
        return (
            "⚠️ با تاس🎲 انداختن پول در بیار!\n\n"

            "ربات زیر با تاس🎲 انداختن پول میده باورت میشه؟ :)\n\n"

            f"🎁 به کاربرای جدید هم {referral_info.entry_prize:,} تومان هدیه خوش آمدگویی میده از دستش نده 🥳👇\n\n"

            f"https://t.me/{BotConfig.BOT_USERNAME}/?start={user_id}"
        )
    
    @staticmethod
    def referral_reply(user: User, referral_info: Configs) -> str:
        return (
            f"⚠️ بنر بالا را برای دوستانتان ارسال کنید و به ازای هر شخصی که با لینک شما در ربات عضو شود {referral_info.referral_bonus:,} تومان اعتبار هدیه دریافت خواهید کرد.\n\n"

            f"👥 تعداد زیرمجموعه شما: {len(user.user_referrals)}"
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
    
    @staticmethod
    def referral_bonus(invited_user_id: int, amount: int) -> str:
        return (
            f"💰 کاربر عزیز شما زیر مجموعه جدید گرفتید به ایدی <code>{invited_user_id}</code> و مقدار {amount:,} به شما داده شد"
        )
    
    # @staticmethod
    # def deposit_request(user_id: int) -> str:
    #     return f"📍 کاربر با ایدی عددی {user_id} درخواست افزایش موجودی داده است\n{Strings.SELECT}"
    
    # @staticmethod
    # def withdraw_request(user_id: int, amount: int, wallet: str, txid: str | None = None) -> str:
    #     text  = (
    #         f"🔢 شناسه عددی کاربر : {user_id}\n"
    #         f"💳 مقدار : {amount:,}\n"
    #         f"📜 کیف پول : <code>{wallet}</code>\n"  
    #     )
    #     text += f"📩 شناسه پرداخت : {txid}" if txid else ""
    #     return text
    
    # @staticmethod
    # def send_crypto(wallet: str) -> str:
    #     return (
    #         "لطفا ابتدا مقدار مورد نیاز خود را به ادرس ولت زیر وارد کنید ✅\n"
    #         f"<code>{wallet}</code>\n"
    #         "💰 سپس لطفا TXID تراکنش یا اسکرین شات ارسال را ارسال کنید و منتظر تایید باشید"
    #     )
    