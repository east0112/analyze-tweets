from logging import getLogger, StreamHandler, DEBUG

class LogStraem:
    #ログ設定取得
    def get_logger():
        logger = getLogger(__name__)
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        logger.setLevel(DEBUG)
        logger.addHandler(handler)
        logger.propagate = False
        return logger
