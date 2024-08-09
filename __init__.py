from pbf.utils import MetaData
from pbf import logger
from pbf.utils.Register import Command, Message, Notice, Request, Meta
from pbf.controller.Data import Event
from pbf.controller.Client import Msg

# 插件元数据
meta_data = MetaData(
    name="pbf",
    version="0.1.0",
    versionCode=10,
    description="PBF Plugin",
    author="xzystudio",
    license="MIT",
    keywords=["pbf", "plugin"],
    readme="""
    # PBF Plugin
    hi
    """
)

# 在PBF启动时、插件被装载时调用
def _enter():
    logger.info("Test PBF Plugin loaded")

# 插件开放给其他插件调用的接口
class Api:
    @staticmethod
    def foo():  # 可以在其他插件中通过 `pbf.pluginsManager.require("this_plugin_name").foo()` 调用
        return "bar"


@Command(name="test", description="test command")  # 注册指令，匹配消息文本开头的"test"
def testCommand(event: Event):
    logger.info(f"test command was called: {event}")
    # do something
    logger.info(Msg("恭喜！\n当你收到这条消息，意味着PBFNext的全部基本功能已经测试通过，具备生产运行条件。", event=event).send())


@Message(name="message handler")  # 注册消息处理器，会处理所有消息
def messageHandler(event: Event):
    logger.info(f"message handler was called: {event}")
    # do something

@Notice(name="notice handler")  # 注册通知处理器，会处理所有通知
def noticeHandler(event: Event):
    logger.info(f"notice handler was called: {event}")
    # do something

@Request(name="request handler")  # 注册请求处理器，会处理所有请求
def requestHandler(event: Event):
    logger.info(f"request handler was called: {event}")
    # do something

@Meta(name="meta handler")  # 注册元数据处理器，会处理所有元数据
def metaHandler(event: Event):
    logger.info(f"meta handler was called: {event}")
    # do something
