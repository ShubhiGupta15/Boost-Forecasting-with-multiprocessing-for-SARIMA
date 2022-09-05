import concurrent.futures
import time

import multiprocessing
from itertools import product
from multiprocessing.pool import Pool

def Sarima():
    dicti={}
        
    for i in param_grid_models_ls:
        sarima_model = i
        dicti[str(i)]=[]
        model = SARIMAX(train["#Passengers"], order=(i[0],i[1],i[2]), seasonal_order=(i[3],i[4],i[5],i[6]), enforce_stationarity=False, enforce_invertibility=False)
        model_fit = model.fit(disp=False)
        yhat = model_fit.predict(start = len(air_passeneger)-3, end = len(air_passeneger)-1)
        error= mean_absolute_percentage_error(test,yhat)
        data= {'Parameters':str(i),'Predictions':yhat, 'MAPE':error*100}
        df_new = pd.DataFrame(columns = ['Parameters', 'Predictions', 'MAPE'],dtype=object)
        df_new = df_new.append(data,ignore_index= True)
        return df_new

processes = []
t = time.time()
for i in range(len(air_passeneger)):
    p = multiprocessing.Process(target=Sarima)
    processes.append(p)
    p.start()

for j in range(len(processes)):
    processes[j].join()

print("Done in : ",time.time()-t)
