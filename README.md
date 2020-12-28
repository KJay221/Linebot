# 股票小幫手
>2020 TOC Final Project(Linebot)
## 基本資訊
### Bot basic ID：@800szswu

### QR code：
![QR code](https://i.imgur.com/waTO8Tl.png)
---
### 創作理念
因為網路上的股票資訊都非常雜亂，所以做了一個查詢股票資訊的工具，裡面可以查台股的一些基本資訊及美國具指標性的三個指數，另外也有分析各股資訊給予買賣的建議

## 操作使用
首先用上述資訊加入Line好友(股票小幫手)

<img width="300" alt="portfolio_view" src="https://i.imgur.com/nGFLbdY.png">

接著輸入start開始，因為後端只有一個程式在跑，若有人已經使用start開始，則輸入menu回到功能選單

### 開始使用
<img width="300" alt="picture" src="https://i.imgur.com/PBBRdtH.jpg">

在功能選單中可以選擇直接開始使用，或者是查詢fsm圖，另外點擊github按鈕則可直接連接到此repository

開始後可選擇指數查詢或台股查詢

### 指數查詢
- 美股指數可看不同區間走勢
- 台股大盤指數可看即時資訊及歷史績效

#### 台股大盤指數
<img width="500" alt="picture" src="https://i.imgur.com/jehw9a7.jpg">

#### 美股指數
<img width="500" alt="picture" src="https://i.imgur.com/U6nH1FV.jpg">

### 台股查詢
- 請先輸入上市公司名稱或代碼
- 提供即時資訊，歷史績效及推薦程度
- <font color=#ff0000>注意！！只提供上市公司股票查詢，上櫃公司及ETF等資訊則不提供</font>

#### 即時資訊
<img width="500" alt="picture" src="https://i.imgur.com/0Vi1cIv.jpg">

#### 推薦程度
<img width="500" alt="picture" src="https://i.imgur.com/I3ZiqLp.jpg">

#### 推薦程度如何產生
- 短期投資：考慮當日內外盤比，近期三大法人買賣超，近期與大盤績效的差值
- 長期投資：考慮本益比，長期與大盤績效的差值
- 推薦程度分三種：買進、持有、賣出
- 此推薦純屬參考用，請謹慎使用：）

#### 請依照指示操作或隨便輸入文字看當下狀態如何操作

## 程式說明
首先將project clone下來
### 開發環境

#### 用pipenv建置python環境
```
pipenv install #自動安裝所需套件
pipenv shell #進入環境
```

#### 使用transitions撰寫狀態機
fsm圖
![picture](https://i.imgur.com/gcJlSPB.png)

#### 環境變數設定

在專案根目錄創建.env檔
```
LINE_CHANNEL_SECRET=****************
LINE_CHANNEL_ACCESS_TOKEN=****************
PORT=****
IMGUR_KEY=****************
```

#### 開啟本地端伺服器
```
python3 app.py #開啟本地端伺服器
```
#### 使用ngrok將local server轉到public
[ngrok](https://ngrok.com/)官網有詳細使用教學

#### Webhook settings
到[Line developer](https://developers.line.biz/en/)設定Webhook URL

## Reference
 [葉家彣／成功大學電機系109](https://github.com/vickyyeh/Linebot)  
 [Template Code for TOC Project 2020](https://github.com/NCKU-CCS/TOC-Project-2020)  
 資訊參考-[Mr. Market 市場先生](https://rich01.com/)  
 
 >made by [KJay221](https://github.com/KJay221)  
 >[說明文件](https://hackmd.io/zRgJNF5eQgunq8gQof-OWg?view)
