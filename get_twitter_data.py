import sys
import tweepy
import configparser
from datetime import datetime
from janome.tokenizer import Tokenizer

#ログ設定
from logging import getLogger, StreamHandler, DEBUG
from log_stream import LogStraem
info_str = '[get_twitter_data info]：'

#形態素解析 関数
def analysis_word(tweets_data):
    output = []
    t = Tokenizer()
    for token in t.tokenize(''.join(tweets_data)):
        if token.part_of_speech.split(',')[0] in ["名詞"]:
            output.append(token.surface)
    return output


#メイン処理
#設定読込
inifile = configparser.ConfigParser()
inifile.read('../config.ini','UTF-8')
consumer_key = inifile.get('consumer', 'consumer_key')
consumer_secret = inifile.get('consumer', 'consumer_secret')
access_token = inifile.get('access', 'access_token')
access_secret = inifile.get('access', 'access_secret')
#ログ
logger = LogStraem.get_logger()

#１．引数の判定
#if not len(sys.argv) == 3:
if len(sys.argv) == 3:
    logger.debug(info_str + '引数の設定に誤りがあります。下記のフォーマットで設定して下さい。')
    logger.debug(info_str + 'python get_twitter_data "hashtag" "開始時間" "終了時間"')
    sys.exit()

#２．引数の受け取り
#hashtag = sys.argv[0]
#start_time = '{0:%Y-%m-%d_}'.format(datetime.now()) + sys.argv[1] +'_JST'
#end_time = '{0:%Y-%m-%d_}'.format(datetime.now()) + sys.argv[2] +'_jST'
#テスト用
hashtag = '#アッパレ173'
start_time = '2019-06-17_' + '23:15:00' +'_JST'
end_time = '2019-06-17_' + '23:30:00' +'_JST'

#３．API認証
logger.debug(info_str + 'Twitter API認証を開始します。')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)
logger.debug(info_str + 'Twitter API認証が完了しました。')

#４．ツイート取得
logger.debug(info_str + 'Twitter データ取得を開始します。')
tweets_data = []

#検索キーワードの設定
query = '{0} since:{1} until:{2}'
query = query.format(hashtag,start_time,end_time)
logger.debug(info_str + '検索キーワード ' + query)

exit_flag = True
exit_flag = False
loop_count = 0
max_id = 0
while exit_flag:
    #全件取得するまでループする
    loop_count += 1
    #logger.debug(info_str + '取得回数 ' + str(loop_count) + '回目')
    #データ取得　２回目以降は前回取得時のmax_idを検索条件に設定する
    if max_id == 0:
        search_results = api.search(q=query,count=100)
    else:
        search_results = api.search(q=query,count=100,max_id=max_id)

    logger.debug(info_str + '取得回数 ' + str(loop_count) + '回目　／　' + '取得件数 ' + str(len(search_results)) + '件')

    if len(search_results) == 0: break

    #ツイートデータを格納する
    for result in search_results:
        tweets_data.append(result.text)
        max_id = result.id
        #logger.debug(info_str + str(max_id))
        #logger.debug(info_str + result.text)
        #logger.debug(info_str + str(result.created_at))
    #if loop_count == 20: break

#形態素解析
analysed_tweets_data = analysis_word(tweets_data)

#ワードクラウド生成
font_path = 'irohamaru-Regular.ttf'

#生成した画像を保存

#結果をツイートする
