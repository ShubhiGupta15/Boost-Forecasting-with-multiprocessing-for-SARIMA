# Forecasting Airline passenger count for next year
df_new3 = pd.DataFrame(columns = ['Month'],dtype=object)
df_new2 = pd.DataFrame(columns = ['Forecast'],dtype=object)

i=df_new1['Parameters']
res = ast.literal_eval(i[0])
p=res[0]
d=res[1]
q=res[2]
P=res[3]
D=res[4]
Q=res[5]
m=res[6]
    
for i in range(0,12):
    my_date = datetime.datetime(1961,1,1)
    my_date_months = my_date + relativedelta(months = i)
    data= {'Month':my_date_months}
    df_new3 = df_new3.append(data,ignore_index= True)
    

model = SARIMAX(air_passeneger["#Passengers"], order=(p,d,q), seasonal_order=(P,D,Q,m), enforce_stationarity=False, enforce_invertibility=False)
model_fit = model.fit()
forecast = model_fit.forecast(steps=12)

for y in forecast:
    data1= {'Forecast': y}
    df_new2 = df_new2.append(data1,ignore_index= True)

frames = [df_new3, df_new2]
df_forecast = pd.concat(frames, axis=1)
