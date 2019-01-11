# Classified
## Step1
假設一銀行正在考慮是否借貸金錢給予他人，銀行可能會考慮以下幾種條件  
1. 該人信用  
2. 該人是否名下有財產  
3. 借貸金額大小  
4. 工作是否穩定  
我們利用這些條件，建構出以下的決策樹  
![image](https://github.com/williamchangTW/Classified/blob/master/original.png)  
利用亂數，隨機生成不同條件的資料集，並利用已知的決策樹，對資料進行lable。  
亂數的產生，資料的標記實作於data.py  
## Step2
利用DT.py訓練模型，並且只取4/5的資料進行訓練，1/5的資料將用來進行驗證  
## Step3
將DT.py訓練完成的模型視覺化  
![image](https://github.com/williamchangTW/Classified/blob/master/DT.jpg)  
## Step4
可以觀察到的決策樹的改變，造成了判斷變得更為複雜，由於訓練出來的決策樹，是基於資料來進行判斷與建構的，與基於規則建構的決策樹就有可能會產生不同的建構，另外，資料的分布也有可能影響決策樹的建構。  
