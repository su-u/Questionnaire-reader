import requests
import base64
import json
import settings

GOOGLE_CLOUD_VISION_API_URL = 'https://vision.googleapis.com/v1/images:annotate?key='

API_KEY = settings.AP
#API_KEY = "AIzaSyB46NoyoqwjmTfpVLCabb1Tn_MAkoDsaj0"

# APIを呼び、認識結果をjson型で返す
def request_cloud_vison_api(image_base64):
    api_url = GOOGLE_CLOUD_VISION_API_URL + API_KEY
    req_body = json.dumps({
        'requests': [{
            'image': {
                'content': image_base64.decode('utf-8') # jsonに変換するためにstring型に変換する
            },
            'features': [{
                'type': 'TEXT_DETECTION', # ここを変更することで分析内容を変更できる
                'maxResults': 10,
            }]
        }]
    })
    res = requests.post(api_url, data=req_body)
    return res.json()

# 画像読み込み
def img_to_base64(filepath):
    with open(filepath, 'rb') as img:
        img_byte = img.read()
    return base64.b64encode(img_byte)

# 文字認識させたい画像を./img.pngとする
img_base64 = img_to_base64('./img.png')
result = request_cloud_vison_api(img_base64)

#認識した文字の位置など、すべての情報を出力
print("{}".format(json.dumps(result, indent=4)))

#認識した文字のみを出力
text_r = result["responses"][0]["fullTextAnnotation"]["text"]
print(text_r)