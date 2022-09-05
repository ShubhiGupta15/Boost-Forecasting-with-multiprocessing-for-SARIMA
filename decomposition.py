# Decompose time series into daily trend, seasonal, and residual components.

from statsmodels.tsa.seasonal import seasonal_decompose

# additive decomposition
result_additive = seasonal_decompose(air_passeneger,model='additive', extrapolate_trend='freq')

# multiplicative
result_multiplicative = seasonal_decompose(air_passeneger,model='multiplicative', extrapolate_trend='freq')

# plot
plt.rcParams.update({'figure.figsize':(20,8)})
result_additive.plot()
plt.suptitle('Additive Seasonal Decompose', fontsize=12)
plt.show()

result_multiplicative.plot()
plt.suptitle('Multiplicative Seasonal Decompose', fontsize=12)
plt.show()
