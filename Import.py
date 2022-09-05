#read the csv file
air_passeneger = pd.read_csv(r'C:/Datasets/AirPassengers.csv')
#string to date format
air_passeneger['Month'] = pd.to_datetime(air_passeneger['Month'],infer_datetime_format=True)
air_passeneger = air_passeneger.set_index(['Month'])
display(air_passeneger.shape)
air_passeneger.head(5)
