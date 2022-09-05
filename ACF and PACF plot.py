fig, ax = plt.subplots(2,1, figsize =(18, 10))
fig = sm.graphics.tsa.plot_acf(train.diff().dropna(), lags=15, ax=ax[0])
fig = sm.graphics.tsa.plot_pacf(train.diff().dropna(), lags=15, ax=ax[1])
plt.show()
