
import requests

if __name__ == '__main__':
    # 实时翻译的接口，只能翻译英语到汉语
    # req_url = 'http://fanyi.baidu.com/sug'
    # Form_Data = {"kw": 'love'｝

    req_url = 'http://fanyi.baidu.com/transapi'
    Form_Data = {"query": 'love', 'from': 'en', 'to': 'de'}  # 英语翻译为德语

    translate_result = requests.post(req_url, Form_Data)
    result = translate_result.json()  # 转化为json格式
    print(result['data'][0]['dst'])

    # 简化为一行代码就是
    print(requests.post('http://fanyi.baidu.com/transapi',
                        data={"query": 'love', 'from': 'en', 'to': 'de'}).json()['data'][0]['dst'])
