from pbf.utils import MetaData
from pbf.setup import logger
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


# 在插件被装载时调用
def _enter():  # 如不需要可以删除
    logger.info("Test PBF Plugin loaded")

# 在插件被卸载时调用
def _exit():  # 如不需要可以删除
    logger.info("Test PBF Plugin unloaded")
# 关于`_enter`与`_exit`函数的更多信息，请参见文档


# 插件开放给其他插件调用的接口
class Api:  # 如不需要可以删除
    @staticmethod
    def foo():  # 可以在其他插件中通过 `pbf.pluginsManager.require("this_plugin_name").foo()` 调用
        return "bar"


@Command(name="test", description="test command")  # 注册指令，匹配消息文本开头的"test"
def testCommand(event: Event):
    logger.info(f"test command was called: {event}")
    # do something
    logger.info(
        Msg("恭喜！\n当你收到这条消息，意味着PBFNext的全部基本功能已经测试通过，具备生产运行条件。", event=event).send())
    # 这是发送一条消息，Msg类是基于Client类的封装，具体使用请见文档


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
