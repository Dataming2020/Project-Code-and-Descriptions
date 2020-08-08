import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
f = open('Prediction_1season_00325.txt', 'rb')
cl = pickle.load(f)
print(cl)
