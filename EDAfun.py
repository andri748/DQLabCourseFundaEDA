import pandas as pd
import matplotlib.pyplot as plt

order_df = pd.read_csv("order.csv")
"""print(order_df.head())
#print(order_df.describe(include=["all"])) error
#print(order_df.describe) quick sum
print(order_df.loc[:, "product_weight_gram"].mean())                                     #.loc digunakan untuk slicing
print(order_df.loc[:, "product_weight_gram"].median())
print(order_df.loc[:, "product_weight_gram"].std())#standar deviasi #simpangan baku
print(order_df.loc[:, "product_weight_gram"].var())#varians #ragam
print(order_df.loc[:, "price"].sum)
print(order_df.loc[:, "quantity"].sum)"""

#   OUTLIERS
"""outliers merupakan data observasi yang muncul dengan nilai-nilai ekstrim. Yang dimaksud dengan nilai-nilai ekstrim
dalam observasi adalah nilai yang jauh atau beda sama sekali dengan sebagian besar nilai lain dalam kelompoknya.
Pada umumnya, outliers dapat ditentukan dengan metric IQR (interquartile range).
Rumus dasar dari IQR: Q3 - Q1. Dan data suatu observasi dapat dikatakan outliers jika memenuhi kedua syarat dibawah ini:
data < Q1 - 1.5 * IQR
data > Q3 + 1.5 * IQR"""

""" q1 = order_df[["product_weight_gram"]].quantile(0.25)
q3 = order_df[["product_weight_gram"]].quantile(0.75)
iqr = q3 - q1
print(iqr)
# Karena saat ini memiliki skor IQR, saatnya untuk menentukan Outliers. Kode di bawah ini akan memberikan output dengan
# beberapa nilai True atau False. Titik data di mana terdapat False yang berarti nilai-nilai ini valid sedangkan True
# menunjukkan adanya Outliers.
print((order_df < (q1 - 1.5 * iqr)) | (order_df > q3 - 1.5 * iqr))"""


#   Rename dengan nama kolom
#order_df.rename(columns={"price": "harga"}, inplace=True)
#   Rename dengan indeks kolom
#order_df.columns.values[0] = "harga"

#   .groupby with pandas menghitung rata2 product_Category_name dengan metode pembayaran
"""order_df["product_weight_gram"].groupby([order_df["product_category_name"], order_df["payment_type"]]).mean()
print(order_df)"""

#   sorting with pandas
"""sortharga = order_df.sort_values(by="product_weight_gram", ascending=False) #1 kolom
#sortharga = order_df.sort_values(by=["price", "product_weight_gram"], ascending=[True, False]) # 2 kolom
print(sortharga)"""

import pandas as pd
import matplotlib.pyplot as pl
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Mean price yang dibayar customer dari masing-masing metode pembayaran.
median_price = order_df["price"].groupby(order_df["payment_type"]).median()
print(median_price)
# Ubah freight_value menjadi shipping_cost dan cari shipping_cost
# termahal dari data penjualan tersebut menggunakan sort.
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
sort_value = order_df.sort_values(by="shipping_cost", ascending=0)
print(sort_value)
# Untuk product_category_name, berapa rata-rata weight produk tersebut
# dan standar deviasi mana yang terkecil dari weight tersebut,
mean_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).mean()
print(mean_value.sort_values())
std_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).std()
print(std_value.sort_values())
# Buat histogram quantity penjualan dari dataset tersebut untuk melihat persebaran quantity
# penjualan tersebut dengan bins = 5 dan figsize= (4,5)
order_df[["quantity"]].hist(figsize=(4, 5), bins=5)
plt.show()
