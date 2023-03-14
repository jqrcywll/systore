import sys
sys.path.append('..')
from utils.ShowapiRequest import ShowapiRequest

def queryBarcode(barcode):
    r = ShowapiRequest("http://route.showapi.com/66-22",
                       "1334896", "25a869faa233420cb94e49a3749753d9")
    r.addBodyPara("code", barcode)
    res = r.post()
    print(res.text)  # 返回信息

queryBarcode("6921734944573")