from logging import getLogger, StreamHandler, INFO, FileHandler
from datetime import datetime

class LogStraem:
    #ログ設定取得
    def get_logger(hashtag):
        logger = getLogger(__name__)
        #ログのファイル出力設定
        file_handler = FileHandler('./log/' + '{0:%Y-%m-%d_}'.format(datetime.now()) + hashtag + '.log')
        logger.addHandler(file_handler)
        #ログのコンソール出力設定
        stream_handler = StreamHandler()
        stream_handler.setLevel(INFO)
        logger.setLevel(INFO)
        logger.addHandler(stream_handler)
        logger.propagate = False
        return logger
