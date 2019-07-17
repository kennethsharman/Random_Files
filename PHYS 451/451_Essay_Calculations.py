import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import S&P 500 Data from 2014-2019
df = pd.read_csv('sp500.csv')
print(df.head(5))

# Isolate Imported Data
dates = df['Ddate']
closes = df['Adj Close']

# Plot timeseries
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

# Typecast pandas dataframe to numpy array
closes_list = np.array(closes.values.tolist())

# Transform the time series of returns to standard normal distribution

# time series of returns over time scale of 1 day
dS1 = (closes_list[1:] - closes_list[:-1]) / closes_list[:-1]
# Square of the previous value
dS1_sqr = [i*i for i in dS1]
# Expected value of 1 day returns
dS1_mean = np.mean(dS1)
# Stadnard Deviation of 1 day returns
dS1_std = np.std(dS1)
# Expected value of square of 1 day return
dS1_sqr_mean = np.mean(dS1_sqr)

# Standardized returns
ds1 = (dS1-dS1_mean) / dS1_std

max_time_sep = 30 # Maximum autocorrelation time separation
time_separation = [t for t in range(1,max_time_sep+1)] # list of time separations

auto_correlations = [] # initialize list for autocorrelation values
# populate list with autocorrelations over the range of time separations
for t in range(1, max_time_sep+1):
    auto_corr = np.mean([i*j for (i,j) in zip(ds1[:-t], ds1[t:]) ])
    auto_correlations.append(auto_corr)
    
# Confidence interval for sample autocorrelation
# Sourced from:
# www.mathworks.com/help/signal/ug/confidence-intervals-for-sample-autocorrelation.html
confidence_int = 1.96/np.sqrt(len(ds1))
print(confidence_int)

# Plot the autocorrelation values against time separation
# superimpose confidence interval bands
ax = plt.figure(figsize=(15,7)) # Set the plot size
plt.xlabel("Time Separation (days)", fontsize=20)
plt.ylabel("Autocorrelation", fontsize=20)
plt.title("Autocorrelations of S&P 500 Index Closing Price", fontsize=20)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)

plt.plot(time_separation, auto_correlations, 'ok-', label='Autocorrelation')
plt.axhline(y=confidence_int, color='k', ls='--', label='Confidence Interval')
plt.axhline(y=-confidence_int, color='k', ls='--')

plt.grid(linestyle='dashed') # Add grid with solid lines to graph
plt.ylim(-.1,0.12)
plt.savefig('auto_correlations.png')

# Add customized legend
legend = plt.legend(loc=0, fontsize='x-large', shadow=(True), borderaxespad=3)
frame = legend.get_frame()
frame.set_facecolor('#f9f9f9')
frame.set_alpha(0.6)

plt.show()
