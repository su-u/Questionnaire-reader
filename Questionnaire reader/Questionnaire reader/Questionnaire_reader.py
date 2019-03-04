import requests
import base64
import json
import configparser
import Logger

log = Logger.Logger()
GOOGLE_CLOUD_VISION_API_URL = 'https://vision.googleapis.com/v1/images:annotate?key='

def request_cloud_vison_api(image_base64, api_key):
    api_url = GOOGLE_CLOUD_VISION_API_URL + api_key
    req_body = json.dumps({
        "requests": [{
            "image": {
                "content": image_base64.decode("utf-8")
            },
            "features": [{
                # TEXT_DETECTION
                # DOCUMENT_TEXT_DETECTION
                "type": "TEXT_DETECTION",
               "maxResults": 10,
            }]
        }]
    })
    res = requests.post(api_url, data=req_body)
    return res.json()

def img_to_base64(filepath):
    with open(filepath, 'rb') as img:
        img_byte = img.read()
    return base64.b64encode(img_byte)

def main():
    log 
    API_KEY = ""
    inifile = configparser.ConfigParser()

    try:
        inifile.read("./config.ini", "utf-8")
    except:
        log.warn("cant load \"conig.ini\"")
    else:
        API_KEY = inifile.get("token", "GOOGLE_API_TOKEN")
        log.info("loaded \"config.ini\"")

    img_base64 = img_to_base64('./iroha.png')
    result = request_cloud_vison_api(img_base64, API_KEY)

    if("error" in result):
        print("{}".format(json.dumps(result, indent=4)))
    else:
        text_r = result["responses"][0]["fullTextAnnotation"]["text"]
        print(text_r)

if __name__ == "__main__":
    main()