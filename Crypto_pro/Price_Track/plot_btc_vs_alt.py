import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates
from easygui import *
import datetime

#GUI: Text and Title
text = "Choose a currency to compare - Maximum amount 5"
titel = "Kryptoautomat"

#Reading CSV's
path = r"C:\Users\bennk\Documents\Programmierung\Pythonprogramms\Crypto_pro\Price_Track"
directory=[f for f in os.listdir(path) if f.endswith('.csv')]

crypto_df = pd.DataFrame(columns=["Cryptocurrency", "Price in USD", "Date"])

for file in directory:
    df = pd.read_csv(file, delimiter=";")
    crypto_df = crypto_df.append(df)

print(crypto_df)
date_changer = lambda row: datetime.datetime.strptime(row, "%d.%m.%Y")
crypto_df["Date"] = crypto_df["Date"].apply(date_changer)

# getting List for GUI Dropdown Menu
all_cryptos = crypto_df["Cryptocurrency"].drop_duplicates()
crypto_name_list = all_cryptos.to_list()

#switch Dtype to float for matplotlib
crypto_df["Price in USD"] = crypto_df["Price in USD"].astype(str)
crypto_df["Price in USD"] = crypto_df["Price in USD"].str.replace(",",".")
crypto_df["Price in USD"] = crypto_df["Price in USD"].astype(float)
crypto_df["Date"] = crypto_df["Date"].dt.strftime("%d/%m")  

coin_list = []
output = multchoicebox(text, titel,crypto_name_list)



#Plot
fig= plt.subplots(figsize=(12, 8))
plt.suptitle("BTC compared to Alts")

for i in range(len(output)): 
    
    coin_name= output[i]
    crypto_df_filter = crypto_df[crypto_df["Cryptocurrency"]==coin_name]
    index_num = crypto_df_filter.index
    row_number = len(index_num)
    coin_list.append(coin_name)
    
    if row_number > 0:
        i += 1
        max_price = crypto_df_filter["Price in USD"].max()
        min_price = crypto_df_filter["Price in USD"].min()
        upper_bound = max_price 
        lower_bound = min_price

        crypto_df_filter.sort_values(by=["Date"],inplace=True)
        plt.style.use("seaborn")
        axe = plt.subplot(3,2 ,i)
        axe.set_xlabel("Days", labelpad = 0.5)
        axe.set_ylabel("Price in USD")
        axe.set_yticks(crypto_df_filter["Price in USD"])
        axe.set_xticklabels(crypto_df_filter["Date"])
        axe.set_ylim([lower_bound, upper_bound])
        
        i -= 1
        axe.title.set_text(coin_list[i])
        plt.yticks(fontsize=8, rotation= 45)
        plt.subplots_adjust(wspace=0.3, hspace=0.8)
        plt.plot('Date','Price in USD', data=crypto_df_filter, marker="o")
    else:
        print("There is no data to plot...")
        

plt.show()
plt.close()
    
    
        












        