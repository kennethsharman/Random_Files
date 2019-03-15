import pandas as pd
import matplotlib.pyplot as plt

# import S&P 500 Data from 2014-2019
df = pd.read_csv('sp500.csv')
print(df.head(5))

dates = df['Ddate']
closes = df['Close']

fig = plt.figure(figsize=(15,8))
ax = plt.subplot()

plt.xlabel('Date', fontsize=20, labelpad=20)
plt.ylabel('Close Price (USD)', fontsize=20, labelpad=20)
plt.title('S&P 500 Index Close Pricing over 5 Year Period', fontsize=20, pad=20)

plt.grid()
ax.set_xticks([2014.201, 2015.201, 2016.201, 2017.201, 2018.201, 2019.201])
ax.set_xticklabels(['$03.14.2014$', r'$03.14.2015$', r'$03.14.2016$', r'$03.14.2017$',\
                    r'$03.14.2018$', r'$03.14.2019$'])
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)

ax.plot(dates,closes)
plt.savefig('time_series.png')
plt.show()