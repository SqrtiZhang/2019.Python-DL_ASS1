import sys
import string
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from Form import Ui_Weather
from weather import weather
from airquality import airquality

#此类用于将api数据传送到图形化界面
class MyPyQt(QtWidgets.QWidget,Ui_Weather):
    def __init__(self):
        super(MyPyQt,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Weather Query")#改变窗口名
        self.setWindowIcon(QIcon('title.jpg'))#改变图标
        self.__weather = weather()#私有变量 天气
        self.__airqu=airquality()#私有变量 空气质量
        self.setStyleSheet('''QLineEdit{color:white;background:transparent;border:1px solid gray; 
                                border-radius:10px;padding:2px 4px;font-weight:1000;}
                              QPushButton{color:white;border:1px solid gray; border-radius:10px;padding:2px 4px；
                                font-weight:1000;font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}
                              QLabel{color:white;border-radius:10px;padding:2px 4px; font-size:18px;
                                font-weight:500;font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}
                              QTextEdit{color:white;background:transparent;border:1px solid gray;
                                font-weight:1000; border-radius:10px;padding:2px 4px;}
                              ''')#用QSS美化ui
        self.setWindowOpacity(0.95)  # 设置窗口透明度

        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(),
                             QtGui.QBrush(QtGui.QPixmap("E:/study/spring.2019/python/lab/lab1/background1.png")))
        self.setPalette(window_pale)#设置背景图
        #以下对特殊控件美化
        self.label_2.setStyleSheet(
            """QLabel{border:None;color:white;font-size:25px;font-weight:500;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}""")
        self.label_3.setStyleSheet(
            """QLabel{border:None;color:white;font-size:21px;font-weight:500;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}""")
        self.label.setStyleSheet(
            """QLabel{border:None;color:white;font-size:25px;font-weight:500;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}""")
        self.label_8.setStyleSheet(
            """QLabel{border:None;color:white;font-size:25px;font-weight:500;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}""")
        self.label_19.setStyleSheet(
            """QLabel{border:None;color:white;font-size:25px;font-weight:500;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}""")
        self.label_13.setStyleSheet(
            """QLabel{border:None;color:white;font-size:25px;font-weight:500;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}""")
        self.label_22.setStyleSheet(
            """QLabel{border:None;color:white;font-size:25px;font-weight:500;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}""")

    #此函数用于请求正常时输出数据
    def printfnormal(self,res,air):
        self.sktemp.setText(res["result"]["sk"]["temp"])
        self.skwd.setText(res["result"]["sk"]["wind_direction"])
        self.skwf.setText(res["result"]["sk"]["wind_strength"])
        self.skhum.setText(res["result"]["sk"]["humidity"])
        self.todtemp.setText(res["result"]["today"]["temperature"])
        self.todwd.setText(res["result"]["today"]["wind"])
        self.todw.setText(res["result"]["today"]["weather"])
        self.dressindex.setText(res["result"]["today"]["dressing_index"])
        self.dress_ad.setText(res["result"]["today"]["dressing_advice"])
        self.uvindex.setText(res["result"]["today"]["uv_index"])
        self.washindex.setText(res["result"]["today"]["wash_index"])
        self.travelindex.setText(res["result"]["today"]["travel_index"])
        self.exindex.setText(res["result"]["today"]["exercise_index"])
        it=list(res["result"]["future"].keys())#对字典提取键
        self.date1.setText(res["result"]["future"][it[0]]["date"])
        self.date1t.setText(res["result"]["future"][it[0]]["temperature"])
        self.date1w.setText(res["result"]["future"][it[0]]["wind"])
        self.date2.setText(res["result"]["future"][it[1]]["date"])
        self.date2t.setText(res["result"]["future"][it[1]]["temperature"])
        self.date2w.setText(res["result"]["future"][it[1]]["wind"])
        self.date3.setText(res["result"]["future"][it[2]]["date"])
        self.date3t.setText(res["result"]["future"][it[2]]["temperature"])
        self.date3w.setText(res["result"]["future"][it[2]]["wind"])
        self.date4.setText(res["result"]["future"][it[3]]["date"])
        self.date4t.setText(res["result"]["future"][it[3]]["temperature"])
        self.date4w.setText(res["result"]["future"][it[3]]["wind"])
        self.date5.setText(res["result"]["future"][it[4]]["date"])
        self.date5t.setText(res["result"]["future"][it[4]]["temperature"])
        self.date5w.setText(res["result"]["future"][it[4]]["wind"])
        self.date6.setText(res["result"]["future"][it[5]]["date"])
        self.date6t.setText(res["result"]["future"][it[5]]["temperature"])
        self.date6w.setText(res["result"]["future"][it[5]]["wind"])
        self.date7.setText(res["result"]["future"][it[6]]["date"])
        self.date7t.setText(res["result"]["future"][it[6]]["temperature"])
        self.date7w.setText(res["result"]["future"][it[6]]["wind"])
        #以下是空气质量
        self.PM25.setText(air["result"][0]["PM2.5"])
        self.AQI.setText(air["result"][0]["AQI"])
        self.QUA.setText(air["result"][0]["quality"])
        self.PM10.setText(air["result"][0]["PM10"])
        self.CO.setText(air["result"][0]["CO"])
        self.NO2.setText(air["result"][0]["NO2"])
        self.O3.setText(air["result"][0]["O3"])
        self.SO2.setText(air["result"][0]["SO2"])
        self.time.setText(air["result"][0]["time"])

    #此函数处理请求失败时的输出
    def printferror(self,reason):
        self.sktemp.setText("N/A")
        self.skwd.setText("N/A")
        self.skwf.setText("N/A")
        self.skhum.setText("N/A")
        self.todtemp.setText("N/A")
        self.todwd.setText("N/A")
        self.todw.setText("N/A")
        self.dressindex.setText("N/A")
        self.dress_ad.setText("N/A")
        self.uvindex.setText("N/A")
        self.washindex.setText("N/A")
        self.travelindex.setText("N/A")
        self.exindex.setText("N/A")
        self.date1.setText("N/A")
        self.date1t.setText("N/A")
        self.date1w.setText("N/A")
        self.date2.setText("N/A")
        self.date2t.setText("N/A")
        self.date2w.setText("N/A")
        self.date3.setText("N/A")
        self.date3t.setText("N/A")
        self.date3w.setText("N/A")
        self.date4.setText("N/A")
        self.date4t.setText("N/A")
        self.date4w.setText("N/A")
        self.date5.setText("N/A")
        self.date5t.setText("N/A")
        self.date5w.setText("N/A")
        self.date6.setText("N/A")
        self.date6t.setText("N/A")
        self.date6w.setText("N/A")
        self.date7.setText("N/A")
        self.date7t.setText("N/A")
        self.date7w.setText("N/A")
        self.PM25.setText("N/A")
        self.AQI.setText("N/A")
        self.QUA.setText("N/A")
        self.PM10.setText("N/A")
        self.CO.setText("N/A")
        self.NO2.setText("N/A")
        self.O3.setText("N/A")
        self.SO2.setText("N/A")
        self.time.setText("N/A")
        QMessageBox.warning(self,"Error!","<font color='black'>%s</font>"%reason)#弹出消息

    #此函数响应鼠标点击城市查询
    def push_butn_city(self):
        CityName=self.CityName.text()
        res_city=self.__weather.RequestCityLoc(CityName,"Get")
        res_air=self.__airqu.RequestAir(CityName,"Get")

        if res_city and res_air:
            error_code_wea = res_city["error_code"]
            error_code_air=res_air["error_code"]
            if error_code_wea == 0 and  error_code_air==0:#异常情况判断
                self.printfnormal(res_city,res_air)#如果正常
            else:
                self.printferror(res_city["reason"]) if error_code_wea else self.printferror(res_air["reason"])
        else:
            QMessageBox.warning(self, "Error!", "<font color='black'>request error</font>")

    #响应gps查询
    def push_butn_gps(self):
        lat = self.lat.text()
        lon=self.lon.text()
        res_city = self.__weather.RequestGPS(lon,lat,"Get")
        if res_city:
            error_code = res_city["error_code"]#异常情况判断
            if error_code == 0:
                CityName=res_city["result"]["today"]["city"]#从天气查询api接口获得城市名字传送给空气质量查询寻接口
                res_air = self.__airqu.RequestAir(CityName, "Get")
                if res_air:
                    error_code=res_air["error_code"]
                    if error_code==0:
                        self.printfnormal(res_city,res_air)
                    else:
                        self.printferror(res_air["reason"])
                else:
                    QMessageBox.warning(self, "Error!", "<font color='black'>request error</font>")
            else:
                self.printferror(res_city["reason"])
        else:
            QMessageBox.warning(self, "Error!", "<font color='black'>request error</font>")

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQt()
    my_pyqt_form.show()
    sys.exit(app.exec_())
