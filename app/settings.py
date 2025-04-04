import os
from msgspec import Struct, field
from msgspec import toml


class APIInfo(Struct):
    title: str
    version: str


class App(Struct):
    show_error_details: bool


class Site(Struct):
    copyright: str


class Database(Struct):
    database: str
    user: str
    password: str
    host: str
    port: int


class Settings(Struct):
    info: APIInfo
    app: App
    site: Site
    database: Database


_setting = None


def load_settings() -> Settings:
    global _setting
    if _setting:
        return _setting
    if os.path.exists("config.toml"):
        with open("config.toml") as f:
            _setting = toml.decode(f.read(), type=Settings)
    else:
        raise FileNotFoundError("config.toml 未找到, 请正确配置")
    return _setting
