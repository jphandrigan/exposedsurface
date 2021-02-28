#setting tank/compartment volume (in Litres)
volume = '12124'

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
 
x = np.array([20820, 43910, 5254, 6272, 4343, 2380, 3372, 5678, 1575, 2978, 3675, 4155, 7948, 10510, 3186, 9464, 7949, 3785, 5678, 7949, 34000, 16670, 3747, 2300, 4500,11356,3785,7570,13249, 36000, 22976, 34000, 34000, 31797.46, 31000, 36000, 16655, 4921,14763, 18927.05, 31797.4]) #L
y = np.array([54, 88.17, 18, 20, 16, 13, 13,16.3, 6.6, 13, 7.9, 15, 23, 24.8, 12, 24, 17.8, 8.83, 11.9, 19.8, 83.94, 41.2, 12.4, 7.6, 8.7,26.85,7.62,15.4,30.94, 84.6, 55.57, 85.60, 85.00,75.5302, 63.7, 84.1,38.46, 9.94, 31.31, 56.11, 79.61]) #m2
 
f = interp1d(x,y,fill_value="extrapolate")
 
type(f)
 
f(volume)
print ('A tank/compartment with a volume of {} L has an estimated exposed surface area of: {} m2.'.format(volume,f(volume)))
