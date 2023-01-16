import requests
import os
import json
import settings
import re
import emoji

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = settings.bt

search_url = "https://api.twitter.com/2/tweets/search/recent"

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    # r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def get_tweet():
    param = input("検索キーワードを入力してね→") + " -is:retweet -has:mentions"
    # Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
    # expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
    query_params = {'query':param,'tweet.fields': 'text','max_results' : 10}
    # print(query_params)
    json_response = connect_to_endpoint(search_url, query_params)
    json_dumps = json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False)
    print(json_response)
    print(json_dumps)

    f = open('test.json','w')
    json.dump(json_response, f, indent=4, sort_keys=True, ensure_ascii=False)
    return json_response

def json_extract(data):
    f = open('test.json','r')
    json_tweet = json.load(f)
    list = []
    for i in range(10):
        json_text = json_tweet["data"][i]["text"]
        list.append(json_text)
    print(list)

def shape_text(list):
    for i, t in text_data(list):
        # URLの削除
        list[i] = re.sub('[ 　]https://t\.co/[a-zA-Z0-9]+', '', t)
        # ユーザー名の削除
        list[i] = re.sub('[ 　]?@[a-zA-Z0-9_]+[ 　]', '', t)
        # 絵文字の除去
        list[i] = data[i].apply(lambda x: remove_emoji(x))
        # ハッシュタグの削除
        list[i] = re.sub('#.+ ', '', t)
        liat[i] = re.sub('＃.+ ', '', t)
        # 全角スペース、タブ、改行を削除
        list[i] = re.sub(r"[\u3000\t\n]", "", t)
    return list

def remove_emoji(text):
    return emoji.get_emoji_regexp().sub(u'', text)

if __name__ == "__main__":
    data = get_tweet()
    json_extract(data)
    shape_text(list)
    print(list)
