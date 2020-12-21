import os
import sys

import requests
from bs4 import BeautifulSoup
import cairosvg
import pyimgur
from dotenv import load_dotenv

import flex_message

load_dotenv()

imgur_key = os.getenv("IMGUR_KEY", None)
if imgur_key is None:
    print("Specify IMGUR_KEY as environment variable.")
    sys.exit(1)

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
            
            
