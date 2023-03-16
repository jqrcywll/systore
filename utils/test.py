from ShowapiRequest import ShowapiRequest

def queryBarcode(barcode):
    r = ShowapiRequest("http://route.showapi.com/66-22",
                       "1358388", "99d416b664a44615b76c41b24f650ef1")
    r.addBodyPara("code", barcode)
    res = r.post()
    print(res.text)  # 返回信息

queryBarcode("6921734944573")