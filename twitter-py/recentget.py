import requests
import os
import json
import settings

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = settings.bt

search_url = "https://api.twitter.com/2/tweets/search/recent"

def bearer_oauth(r):
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
    json_response = connect_to_endpoint(search_url, query_params)
    f = open('test.json','w')
    json.dump(json_response, f, indent=4, sort_keys=True, ensure_ascii=False)
    return json_response

# if __name__ == "__main__":
#     get_tweet()
#     context = json_extract()
#     print(shape_text(context))
