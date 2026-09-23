''' pre-req 

# pip install scikit-learn

agr pip se problem aaye to 

# python -m pip install scikit-learn

check krne ke liye

# python -c "import sklearn; print(sklearn.__version__)"

 
'''



from sklearn.impute import SimpleImputer
import numpy as np
data = np.array([
 [1, 2, np.nan],
 [4, np.nan, 6],
 [np.nan, 8, 9]
])
imputer = SimpleImputer(strategy='median')
imputed_data = imputer.fit_transform(data)
print(data)
print(imputed_data)
