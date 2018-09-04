from urllib import request, parse
import json

if __name__ == '__main__':

    # 实时翻译的接口，只能翻译英语到汉语
    req_url = 'http://fanyi.baidu.com/sug'
    Form_Data = {"kw": 'love'}

    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(req_url, data)
    html = response.read().decode('utf-8')

    print(html)
    # 可以看出html是一个json格式
    translate_results = json.loads(html)
    for item in translate_results['data']:
        for items in item:
            print(item[items])
