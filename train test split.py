#train-test split
train = air_passeneger[0:-3]
test = air_passeneger[-3:]
print('Train Timeseries Range => ', train.index.min(), ' - ' , train.index.max())
print('Train Timeseries Range => ', test.index.min(), ' - ' , test.index.max())
