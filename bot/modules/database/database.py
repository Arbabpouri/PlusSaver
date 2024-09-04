from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session, backref
from sqlalchemy import String, ForeignKey, create_engine, Integer, Text
from typing import List
from config import BotConfig


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class User(Base):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(unique=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    is_ban: Mapped[bool] = mapped_column(default=False)


class Channel(Base):
    __tablename__ = "channels"
    channel_id: Mapped[int] = mapped_column(unique=True)
    channel_name: Mapped[str] = mapped_column(String(300))
    channel_url: Mapped[str] = mapped_column(String(350))


class Configs(Base):
    __tablename__ = "configs"
    support_channel_url: Mapped[str] = mapped_column(String(300), default=BotConfig.DEFULT_SUPPORT_CHANNEL_URL)
    trust_text: Mapped[str] = mapped_column(Text(BotConfig.TEXT_LONG), default=BotConfig.DEFULT_HELP_TEXT)
    rules_text: Mapped[str] = mapped_column(Text(BotConfig.TEXT_LONG), default=BotConfig.DEFULT_RULES_TEXT)

    

class Media(Base):
    __tablename__ = "medias"
    media_downloaded_url: Mapped[str] = mapped_column(String(length=500))
    message_id: Mapped[int]
    channel_id: Mapped[int]


engine = create_engine("sqlite:///database.db", echo=False, pool_size=60, max_overflow=35, pool_timeout=120.0)


def create_table() -> None:
    Base.metadata.create_all(bind=engine)


def defult_data() -> None:

    with Session(bind=engine) as session:

        for admin in BotConfig.DEFULT_ADMINS_USER_ID:
            session.add(User(user_id=admin, is_admin=True))

        configs = Configs()

        session.add_all([configs, ])
        session.commit()
