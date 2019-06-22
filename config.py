#configファイル
#2019/06/22 新規作成
import os
#-------------DATABSE-------------
class DataBaseConfig():
    #postgreSQL ユーザ名
    SQL_DATABASE_USER = 'postgres'
    #postgreSQL データベース名
    SQL_DATABASE_NAME = 'LoveLive_music'
    #postgreSQL パスワード
    SQL_DATABASE_PASS = 'll0630'
    #postgreSQL パスワード
    SQL_DATABASE_PORT = '5432'
    #postgreSQL ホスト
    SQL_DATABASE_HOST = 'localhost'
#-------------lyricCloud-------------
class LyricConfig():
    #フォントファイルパス
    PATH_LYRIC_FONT = 'irohamaru-Regular.ttf'
