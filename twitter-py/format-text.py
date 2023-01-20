import json
import re
import csv
import recentget

def json_extract():
    f = open('test.json','r')
    json_tweet = json.load(f)
    context = []
    for i in range(10):
        json_text = json_tweet["data"][i]["text"]
        context.append(json_text)
    print(context)
    print("\n")
    return context

def shape_text(context):
    for i in range(10):
        # URLの削除
        context[i] = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', str(context[i]))
        # 絵文字の除去
        context[i] = context[i].encode('cp932',errors='ignore').decode('cp932')
        # ハッシュタグの削除
        context[i] = re.sub('#', '', str(context[i]))
        # context[i] = re.sub('＃.+ ', '', str(context))
        # 全角スペース、タブ、改行を削除
        context[i] = context[i].replace("\n", "")
        context[i] = context[i].replace("\u3000","")
        context[i] = context[i].replace("\t","")
        context[i] = context[i].replace("|","")
        context[i] = context[i].replace("<","")
        context[i] = context[i].replace(">","")
        context[i] = context[i].replace("/","")

    print(context)
    return context

def csv_write(context):
    r = open("hirosaki.csv","w")
    write_text = csv.writer(r,delimiter = "\n")
    write_text.writerow(["test"])
    write_text.writerow(context)
    # print(context)
    return

if __name__ == "__main__":
    recentget.get_tweet()
    text = json_extract()
    csv_write(shape_text(text))
