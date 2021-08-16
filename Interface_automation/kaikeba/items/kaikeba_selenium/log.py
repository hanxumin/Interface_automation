# 日志生成器
# 日志的配置函数
import logging.handlers


def basic_log_config():
    # 1.创建日志器
    logger = logging.getLogger()
    # 2.设置日志级别
    logger.setLevel(level=logging.INFO)
    # 3.创建处理器
    ls = logging.StreamHandler()
    lht = logging.handlers.TimedRotatingFileHandler(filename="./Log/uitest.log",
                                                    when="midnight",interval=1,backupCount=2)
    # 4.创建格式化器
    formatter = logging.Formatter(fmt=
                                  "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 给处理器添加格式化器
    ls.setFormatter(formatter)
    lht.setFormatter(formatter)
    # 给日志器添加处理器
    logger.addHandler(ls)
    logger.addHandler(lht)