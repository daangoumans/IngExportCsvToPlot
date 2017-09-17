import pandas as pd
import matplotlib.pyplot as plt

dates = []
amount = []
df = pd.read_csv("ing_export.csv")


for index, row in df.iterrows():
    if "Af" in row['Af Bij']:
        row["Bedrag (EUR)"] = ("-" + row["Bedrag (EUR)"])
    bedrag = float(row["Bedrag (EUR)"].replace(",","."))
    dates.append(pd.to_datetime(str(row["Datum"])[:6], format='%Y%m'))
    amount.append(bedrag)
new_df = list(zip(dates,amount))

df = pd.DataFrame(data = new_df, columns=['Date', 'Amount'])
df = df.groupby(["Date"])[["Amount"]].sum()
plt.figure()
df.plot()
plt.savefig('plot')
