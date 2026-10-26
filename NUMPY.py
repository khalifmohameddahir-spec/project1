#PYTHON FOR DATA ANALYSIS

#NumPy fundermentals
#creating arrays and basic operations

import numpy as np 

#create a 1D array from a list 
arr_1d = np.array([10, 20, 30, 40, 50])

#create a 2D arrray (Matrix)
arr_2D = np.array([[1, 2, 3, ],[4, 5, 6, ], [7, 8, 9]])

print ("1D Array:", arr_1d)
print("2D Array shape:", arr_2D.shape)

#Mathematical operations(vectorization)
scaled_array = arr_1d * 2
print("scaled array (multiplied by 2):", scaled_array)

#statistical functions
print("Mean:", np.mean(arr_1d))
print("median:",np.median(arr_1d))
print("standard Deviation:",np.std(arr_1d))
print("min/max:",np.min(arr_1d), "/", np.max(arr_1d))





























