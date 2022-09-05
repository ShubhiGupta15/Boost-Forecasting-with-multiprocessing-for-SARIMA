# create a list of model configurations to evaluate
param_grid = {'p':[1,2], 
                'd':[1,2],
                'q':[1,2], 
                'P':[1,2], 
                'D':[1,2], 
                'Q':[1,2], 
                'm':[6,12]}

param_grid_models_dict = list(ParameterGrid(param_grid))
param_grid_models_ls = [[d['p'],
                            d['d'],
                            d['q'],
                            d['P'],
                            d['D'],
                            d['Q'],
                            d['m']] for d in param_grid_models_dict]
