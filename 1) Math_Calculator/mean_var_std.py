import numpy as np

def calculate(list):

  if len(list) != 9:
     raise ValueError("List must contain nine numbers.")

  New_list = np.array(list).reshape(3,3)
  
  calculations = {
    'mean': [np.mean(New_list, axis=0).tolist(), np.mean(New_list,axis=1).tolist(), np.mean(New_list).tolist()], 

    'variance': [np.var(New_list, axis=0).tolist(), np.var(New_list,axis=1).tolist(), np.var(New_list).tolist()], 

    'standard deviation': [np.std(New_list, axis=0).tolist(), np.std(New_list,axis=1).tolist(), np.std(New_list).tolist()],

    'max': [np.max(New_list, axis=0).tolist(), np.max(New_list,axis=1).tolist(), np.max(New_list).tolist()],

    'min': [np.min(New_list, axis=0).tolist(), np.min(New_list,axis=1).tolist(), np.min(New_list).tolist()],

    'sum': [np.sum(New_list, axis=0).tolist(), np.sum(New_list,axis=1).tolist(), np.sum(New_list).tolist()]
}
    
  
  return calculations
