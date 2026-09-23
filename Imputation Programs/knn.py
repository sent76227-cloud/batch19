from sklearn.impute import KNNImputer
import numpy as np

a = [ [2, 4, np.nan],
 [5, 1, 6],
 [np.nan, 5, 7],
 [9, 8, 9]]
data = np.array(a)
knn_imputer = KNNImputer(n_neighbors=2)
imputed_data = knn_imputer.fit_transform(data)
print(data)
print(imputed_data)
