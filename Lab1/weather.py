import json
from urllib import parse
from urllib import request
from urllib.request import urlopen

#天气api接口
class weather():
    def __init__(self):
          self.__appkey="4a1e38a63ef132cfd0de382d4b4b9338"

    def RequestCitySupp(self,m="GET"):#获得支持城市，但这个没有用到
        url = "http://v.juhe.cn/weather/citys"
        params = {
            "key": self.__appkey,
            "dtype": "",
        }
        params = parse.urlencode(params).encode('utf-8')
        req = request.Request(url, params)
        response = urlopen(req)
        content = response.read()
        res = json.loads(content)
        return res

    def RequestWeatherKind(self, m="GET"):#获得天气id对应情况
        url = "http://v.juhe.cn/weather/uni"
        params = {
            "key": self.__appkey,
            "dtype": "",
        }
        params = parse.urlencode(params).encode('utf-8')
        req = request.Request(url, params)
        response = urlopen(req)
        content = response.read()
        res = json.loads(content)
        return res

    def RequestGPS(self, lon, lat, m="GET"):#gps请求
        url = "http://v.juhe.cn/weather/geo"
        params = {
            "key": self.__appkey,
            "lon": lon,
            "lat": lat,
            "dtype": "json",
        }
        params = parse.urlencode(params).encode('utf-8')
        req = request.Request(url, params)
        response = urlopen(req)
        content = response.read()
        res = json.loads(content)
        return res

    def RequestCityLoc(self, cityname, m="GET"):#城市查询
        url = "http://v.juhe.cn/weather/index"
        req = request.Request(("%s?cityname=%s&key=%s") % (url, parse.quote(cityname), self.__appkey))
        response = urlopen(req)
        content = response.read()
        res = json.loads(content)
        return res
