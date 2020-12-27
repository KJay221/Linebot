import os
import sys
import json

import requests
from bs4 import BeautifulSoup
import cairosvg
import pyimgur
from dotenv import load_dotenv
import urllib.request

import flex_message

load_dotenv()


imgur_key = os.getenv("IMGUR_KEY", None)
if imgur_key is None:
    print("Specify IMGUR_KEY as environment variable.")
    sys.exit(1)

#index chart generate and change flex_message img
def get_index_chart(index, index_chart_range):
    #get svg url
    chart_url_str = ""
    if index == "道瓊工業指數":
        if index_chart_range == "當日價格":
            chart_url_str = "https://app.quotemedia.com/quotetools/getChart?webmasterId=500&chcon=off&chfrmon=off&chbgch=ffffff&chbg=ffffff&chgrd=cccccc&chbdr=cccccc&chxyc=666666&chln=00578e&chdon=off&chfill=eeeeee&chfill2=0071BB&symbol=DJI&chscale=1d&chton=off&chwid=435&chhig=261&chtype=Mountain&chlowwh=10&chfnts=10&svg=true&lang=en&locale=en"
        elif index_chart_range == "五日價格":
            chart_url_str = "https://app.quotemedia.com/quotetools/getChart?webmasterId=500&chcon=off&chfrmon=off&chbgch=ffffff&chbg=ffffff&chgrd=cccccc&chbdr=cccccc&chxyc=666666&chln=00578e&chdon=off&chfill=eeeeee&chfill2=0071BB&symbol=DJI&chscale=5d&chton=off&chwid=435&chhig=261&chtype=Mountain&chlowwh=10&chfnts=10&svg=true&lang=en&locale=en"
        elif index_chart_range == "近一個月價格":
            chart_url_str = "https://app.quotemedia.com/quotetools/getChart?webmasterId=500&chcon=off&chfrmon=off&chbgch=ffffff&chbg=ffffff&chgrd=cccccc&chbdr=cccccc&chxyc=666666&chln=00578e&chdon=off&chfill=eeeeee&chfill2=0071BB&symbol=DJI&chscale=1m&chton=off&chwid=435&chhig=261&chtype=Mountain&chlowwh=10&chfnts=10&svg=true&lang=en&locale=en"
        elif index_chart_range == "近一年價格":
            chart_url_str = "https://app.quotemedia.com/quotetools/getChart?webmasterId=500&chcon=off&chfrmon=off&chbgch=ffffff&chbg=ffffff&chgrd=cccccc&chbdr=cccccc&chxyc=666666&chln=00578e&chdon=off&chfill=eeeeee&chfill2=0071BB&symbol=DJI&chscale=1y&chton=off&chwid=435&chhig=261&chtype=Mountain&chlowwh=10&chfnts=10&svg=true&lang=en&locale=en"
    elif index == "標普500指數":
        if index_chart_range == "當日價格":
            chart_url_str = "https://app.quotemedia.com/quotetools/getChart?webmasterId=500&chcon=off&chfrmon=off&chbgch=ffffff&chbg=ffffff&chgrd=cccccc&chbdr=cccccc&chxyc=666666&chln=00578e&chdon=off&chfill=eeeeee&chfill2=0071BB&symbol=%5ESPX&chscale=1d&chton=off&chwid=435&chhig=261&chtype=Mountain&chlowwh=10&chfnts=10&svg=true&lang=en&locale=en"
        elif index_chart_range == "五日價格":
            chart_url_str = "https://app.quotemedia.com/quotetools/getChart?webmasterId=500&chcon=off&chfrmon=off&chbgch=ffffff&chbg=ffffff&chgrd=cccccc&chbdr=cccccc&chxyc=666666&chln=00578e&chdon=off&chfill=eeeeee&chfill2=0071BB&symbol=%5ESPX&chscale=5d&chton=off&chwid=435&chhig=261&chtype=Mountain&chlowwh=10&chfnts=10&svg=true&lang=en&locale=en"
        elif index_chart_range == "近一個月價格":
            chart_url_str = "https://app.quotemedia.com/quotetools/getChart?webmasterId=500&chcon=off&chfrmon=off&chbgch=ffffff&chbg=ffffff&chgrd=cccccc&chbdr=cccccc&chxyc=666666&chln=00578e&chdon=off&chfill=eeeeee&chfill2=0071BB&symbol=%5ESPX&chscale=1m&chton=off&chwid=435&chhig=261&chtype=Mountain&chlowwh=10&chfnts=10&svg=true&lang=en&locale=en"
        elif index_chart_range == "近一年價格":
            chart_url_str = "https://app.quotemedia.com/quotetools/getChart?webmasterId=500&chcon=off&chfrmon=off&chbgch=ffffff&chbg=ffffff&chgrd=cccccc&chbdr=cccccc&chxyc=666666&chln=00578e&chdon=off&chfill=eeeeee&chfill2=0071BB&symbol=%5ESPX&chscale=1y&chton=off&chwid=435&chhig=261&chtype=Mountain&chlowwh=10&chfnts=10&svg=true&lang=en&locale=en"
    elif index == "那斯達克指數":
        if index_chart_range == "當日價格":
            chart_url_str = "https://app.quotemedia.com/quotetools/getChart?webmasterId=500&chcon=off&chfrmon=off&chbgch=ffffff&chbg=ffffff&chgrd=cccccc&chbdr=cccccc&chxyc=666666&chln=00578e&chdon=off&chfill=eeeeee&chfill2=0071BB&symbol=%5ENDX&chscale=1d&chton=off&chwid=435&chhig=261&chtype=Mountain&chlowwh=10&chfnts=10&svg=true&lang=en&locale=en"
        elif index_chart_range == "五日價格":
            chart_url_str = "https://app.quotemedia.com/quotetools/getChart?webmasterId=500&chcon=off&chfrmon=off&chbgch=ffffff&chbg=ffffff&chgrd=cccccc&chbdr=cccccc&chxyc=666666&chln=00578e&chdon=off&chfill=eeeeee&chfill2=0071BB&symbol=%5ENDX&chscale=5d&chton=off&chwid=435&chhig=261&chtype=Mountain&chlowwh=10&chfnts=10&svg=true&lang=en&locale=en"
        elif index_chart_range == "近一個月價格":
            chart_url_str = "https://app.quotemedia.com/quotetools/getChart?webmasterId=500&chcon=off&chfrmon=off&chbgch=ffffff&chbg=ffffff&chgrd=cccccc&chbdr=cccccc&chxyc=666666&chln=00578e&chdon=off&chfill=eeeeee&chfill2=0071BB&symbol=%5ENDX&chscale=1m&chton=off&chwid=435&chhig=261&chtype=Mountain&chlowwh=10&chfnts=10&svg=true&lang=en&locale=en"
        elif index_chart_range == "近一年價格":
            chart_url_str = "https://app.quotemedia.com/quotetools/getChart?webmasterId=500&chcon=off&chfrmon=off&chbgch=ffffff&chbg=ffffff&chgrd=cccccc&chbdr=cccccc&chxyc=666666&chln=00578e&chdon=off&chfill=eeeeee&chfill2=0071BB&symbol=%5ENDX&chscale=1y&chton=off&chwid=435&chhig=261&chtype=Mountain&chlowwh=10&chfnts=10&svg=true&lang=en&locale=en"

    # get svg chart from internet
    chart_request = requests.get(chart_url_str)
    chart_svg = open("./img/chart.svg", "w")
    chart_string = str(chart_request.text)
    chart_svg.write(chart_string)
    chart_svg.close()
    cairosvg.svg2png(url="./img/chart.svg", write_to="./img/chart.png")

    # upload to imgur and get url
    client_ID = imgur_key
    img_path = "./img/chart.png"
    im = pyimgur.Imgur(client_ID)
    uploaded_image = im.upload_image(path=img_path, title="upload")

    #change display img
    flex_message.index_chart["body"]["contents"][2]["url"] = uploaded_image.link

#change TW_now style and content
def change_TW_now():
    text_request = urllib.request.urlopen("https://invest.cnyes.com/index/TWS/TSE01")
    soup = BeautifulSoup(text_request,"html.parser")
    final_price = soup.find("div",class_="jsx-2941083017 info-lp")
    amplitude = soup.find("div",class_="jsx-2941083017 change-net")
    up_down = soup.find("div",class_="jsx-2941083017 change-percent")
    flex_message.index_TW_now["body"]["contents"][2]["contents"][1]["text"] = final_price.text
    flex_message.index_TW_now["body"]["contents"][3]["contents"][1]["text"] = amplitude.text
    flex_message.index_TW_now["body"]["contents"][4]["contents"][1]["text"] = up_down.text
    if amplitude.text[0] == "+":
        flex_message.index_TW_now["body"]["contents"][2]["contents"][1]["color"] = "#ff0000"
        flex_message.index_TW_now["body"]["contents"][3]["contents"][1]["color"] = "#ff0000"
        flex_message.index_TW_now["body"]["contents"][4]["contents"][1]["color"] = "#ff0000"
    elif amplitude.text[0] == "-":
        flex_message.index_TW_now["body"]["contents"][2]["contents"][1]["color"] = "#00e038"
        flex_message.index_TW_now["body"]["contents"][3]["contents"][1]["color"] = "#00e038"
        flex_message.index_TW_now["body"]["contents"][4]["contents"][1]["color"] = "#00e038"
    else:
        flex_message.index_TW_now["body"]["contents"][2]["contents"][1]["color"] = "#ffea00"
        flex_message.index_TW_now["body"]["contents"][3]["contents"][1]["color"] = "#ffea00"
        flex_message.index_TW_now["body"]["contents"][4]["contents"][1]["color"] = "#ffea00"

#change TW_history style and content
def change_TW_history():
    text_request = urllib.request.urlopen("https://www.taiwanindex.com.tw/index/index/t00")
    soup = BeautifulSoup(text_request,"html.parser")
    rate = soup.find_all("td")
    stop = 0
    number = 2
    for t in rate:
        if stop == 15 or stop == 17 or stop == 19 or stop == 21 or stop == 23 or stop == 25:
            text = t.text
            flex_message.index_TW_history["body"]["contents"][number]["contents"][1]["text"] = text
            if text[0] == "-":
                flex_message.index_TW_history["body"]["contents"][number]["contents"][1]["color"] = "#00e038"
            else:
                flex_message.index_TW_history["body"]["contents"][number]["contents"][1]["color"] = "#ff0000"
            number+=2
        stop+=1

def show_fsm_link():
    # upload to imgur and get url
    client_ID = imgur_key
    img_path = "./img/fsm.png"
    im = pyimgur.Imgur(client_ID)
    uploaded_image = im.upload_image(path=img_path, title="upload")
    return uploaded_image.link

def find_stock(stock):
    for index in range(1,32):
        url_c=""
        if index == 7 or index == 13 or index == 19:
            continue
        else:
            if index < 10:
                url_c = "0"+str(index)
            else:
                url_c = str(index)
        list_request = urllib.request.urlopen("https://www.cnyes.com/twstock/index2real.aspx?stockType=T&groupId="+url_c+"&stitle=")
        data = list_request.read().decode('utf-8')
        soup = BeautifulSoup(data,"html.parser")
        n_text = soup.find_all("a",href = "/twstock/profile/"+stock+".htm")
        if n_text:
            output = []
            for s in n_text:
                output.append(s.string)
            return output
        s_text = soup.find_all("a")
        for content in s_text:
            if stock == content.string:
                number1 = content["href"]
                number2 = number1.split('/')
                number3 = number2[3].split(".")
                output = [number3[0],stock]
                return output
    return False

def change_stock_now(stock_number):
    text_request = urllib.request.urlopen("https://invest.cnyes.com/twstock/tws/"+stock_number)
    soup = BeautifulSoup(text_request,"html.parser")
    stock_now_info = soup.find("div",class_="jsx-2941083017 info-lp")
    flex_message.stock_now["body"]["contents"][1]["contents"][1]["text"] = stock_now_info.string
    stock_now_info = soup.find("div",class_="jsx-2941083017 change-net")
    flex_message.stock_now["body"]["contents"][2]["contents"][1]["text"] = stock_now_info.string
    if stock_now_info.string[0] == "+":
        flex_message.stock_now["body"]["contents"][1]["contents"][1]["color"] = "#ff0000"
        flex_message.stock_now["body"]["contents"][2]["contents"][1]["color"] = "#ff0000"
        flex_message.stock_now["body"]["contents"][3]["contents"][1]["color"] = "#ff0000"
    elif stock_now_info.string[0] == "-":
        flex_message.stock_now["body"]["contents"][1]["contents"][1]["color"] = "#00e038"
        flex_message.stock_now["body"]["contents"][2]["contents"][1]["color"] = "#00e038"
        flex_message.stock_now["body"]["contents"][3]["contents"][1]["color"] = "#00e038"
    else:
        flex_message.stock_now["body"]["contents"][1]["contents"][1]["color"] = "#ffea00"
        flex_message.stock_now["body"]["contents"][2]["contents"][1]["color"] = "#ffea00"
        flex_message.stock_now["body"]["contents"][3]["contents"][1]["color"] = "#ffea00"
    stock_now_info = soup.find("div",class_="jsx-2941083017 change-percent")
    flex_message.stock_now["body"]["contents"][3]["contents"][1]["text"] = stock_now_info.string
    stock_now_info = soup.find_all("div",class_="jsx-2687283247 jsx-1763002358 block-value block-value--")
    flex_message.stock_now["body"]["contents"][4]["contents"][1]["text"] = stock_now_info[0].string
    flex_message.stock_now["body"]["contents"][5]["contents"][1]["text"] = stock_now_info[1].string
    flex_message.stock_now["body"]["contents"][6]["contents"][1]["text"] = stock_now_info[2].string
    stock_now_info = soup.find_all("p",class_="jsx-2963066371 jsx-556393929")
    flex_message.stock_now["body"]["contents"][7]["contents"][1]["contents"][0]["text"] = stock_now_info[2].string
    flex_message.stock_now["body"]["contents"][7]["contents"][1]["contents"][1]["text"] = stock_now_info[3].string

def change_stock_history(stock_number):
    text_request = urllib.request.urlopen("https://ws.api.cnyes.com/ws/api/v1/quote/quotes/TWS%3A"+stock_number+"%3ASTOCK?column=J")
    raw_data = text_request.read()
    encoding = text_request.info().get_content_charset('utf8')
    data = json.loads(raw_data.decode(encoding))
    flex_message.stock_history["body"]["contents"][2]["contents"][1]["text"] = str(data["data"][0]["7952"])
    flex_message.stock_history["body"]["contents"][4]["contents"][1]["text"] = str(data["data"][0]["3380"])
    flex_message.stock_history["body"]["contents"][6]["contents"][1]["text"] = str(data["data"][0]["3378"])
    flex_message.stock_history["body"]["contents"][8]["contents"][1]["text"] = str(data["data"][0]["3379"])
    flex_message.stock_history["body"]["contents"][10]["contents"][1]["text"] = str(data["data"][0]["3381"])
    flex_message.stock_history["body"]["contents"][12]["contents"][1]["text"] = str(data["data"][0]["200050"])
    for number in range(1,7):
        color = flex_message.stock_history["body"]["contents"][number*2]["contents"][1]["text"][0]
        if color == "-":
            flex_message.stock_history["body"]["contents"][number*2]["contents"][1]["color"] = "#00e038" 
        else:
            flex_message.stock_history["body"]["contents"][number*2]["contents"][1]["color"] = "#ff0000" 


