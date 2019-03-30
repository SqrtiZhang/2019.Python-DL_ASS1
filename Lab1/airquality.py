import json
from urllib import parse
from urllib import request
from urllib.request import urlopen

#空气质量api接口
class airquality():
    def __init__(self):
          self.__appkey="d50035b978c107c673bd525d21c80a94"

    def RequestAir(self,cityname,m="GET"):
        url = "http://web.juhe.cn:8080/environment/air/pm"
        req = request.Request(("%s?city=%s&key=%s") % (url, parse.quote(cityname), self.__appkey))
        response = urlopen(req)
        content = response.read()
        res = json.loads(content)
        return res
