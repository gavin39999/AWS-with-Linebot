# AWS-with-Linebot


在AWS上用Linebot 實現severless

在AWS上運用Lambda+API Gateway 實現Line機器人的實作

# Line Developers
首先 在Line Developers log in 自己的Line帳號 如果沒有請去註冊一個

![image](https://user-images.githubusercontent.com/108290249/180767598-11c792d5-9e97-40b0-b70a-cdc5e506d77d.png)

先命名provider

![image](https://user-images.githubusercontent.com/108290249/180767944-db7773e2-dc41-4b00-8cb2-e1eb8820a865.png)

Create a new channel 選擇Messaging API

![image](https://user-images.githubusercontent.com/108290249/180768306-0bd5d9cd-a4ab-4a6f-9807-9b18ed875499.png)

在Create 項目將基本訊息填上

![image](https://user-images.githubusercontent.com/108290249/180777137-c7f383e1-86df-4a92-b062-95b4aacda34c.png)

# Channel access token&Channel secret

找到Channel access token與Channel secret 這兩個會是一連串的數字與英文的亂碼

![image](https://user-images.githubusercontent.com/108290249/180769347-2f73a001-0f6d-4a50-af08-82091ff89252.png)

![image](https://user-images.githubusercontent.com/108290249/180769439-7f3fd9ce-a8ab-4dca-9d1f-f161ffe260c3.png)

# Webhook Setting

在Webhook Setting部分中須將Webhook打開

![image](https://user-images.githubusercontent.com/108290249/180769855-a7037fb1-26a6-41d5-b8d5-52336dd31bc7.png)

# 架構

初始的架構會是由 User傳遞訊息給Line機器人 機器人接收到訊息觸發API Gateway再觸發到Lambda處理程式碼

![image](https://user-images.githubusercontent.com/108290249/180770040-b690a408-800f-4327-88e1-f09a7c46b40b.png)

# Lambda

Create 一個 Lambda function 會是以python為主

![image](https://user-images.githubusercontent.com/108290249/180777276-405e14ba-dbdc-4e76-b78a-853e4afab92b.png)

# Environment variables

找到Environment variables 並填上前面步驟的Channel access token與Channel secret

![image](https://user-images.githubusercontent.com/108290249/180773029-18dd9f36-eacf-4391-ab9b-9f984b950284.png)

# General configuration

General configuration 把Timeout調整到5分鐘

![image](https://user-images.githubusercontent.com/108290249/180773249-060680b5-6bb6-4fcd-8729-1d404f3e4463.png)

# API Gateway 

Create 一個 API Gateway 選擇Rest API 取名隨意

![image](https://user-images.githubusercontent.com/108290249/180773841-1a7846b3-7540-40e2-a798-09bc83705ace.png)


# Layer

在選擇Layer時不選擇AWS內建提供的python版本 選擇自己上傳一個layer

![image](https://user-images.githubusercontent.com/108290249/180773994-d2a30f38-ce38-408b-a0d3-5ac375fc5bc6.png)

# 串接

之後將API Gateway的endpoint與 line developers的webhook URL 串接起來

![image](https://user-images.githubusercontent.com/108290249/180774224-2211ea92-68a8-4434-a850-05ecfee921da.png)

# 測試

將程式碼上傳與LINE 機器人頁面打開 在聊天室中輸入文字會回復HI訊息

![image](https://user-images.githubusercontent.com/108290249/180774582-2869c7a0-d9ea-438f-a731-08ba5366604d.png)

完成!!!
