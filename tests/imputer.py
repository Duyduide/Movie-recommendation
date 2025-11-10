from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd

train = pd.DataFrame(
    {"age": [18, np.nan, 30, 40], "income": [1000, 2000, np.nan, 10000]}
)

test = pd.DataFrame({"age": [25, np.nan], "income": [np.nan, 7000]})

imputer = SimpleImputer(strategy="mean")

imputer.fit(train)
X_train_filled = imputer.transform(train)
X_test_filled = imputer.transform(test)

df = pd.DataFrame(X_train_filled, columns=train.columns)
print(df)
