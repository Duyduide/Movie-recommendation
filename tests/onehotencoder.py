from sklearn.preprocessing import OneHotEncoder
import pandas as pd

train = pd.DataFrame({"color": ["red", "green", "blue", "green"]})

test = pd.DataFrame({"color": ["green", "red"]})

encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")

encoder.fit(train)

X_train_encoded = encoder.transform(train)
X_test_encoded = encoder.transform(test)

df = pd.DataFrame(X_train_encoded, columns=encoder.get_feature_names_out())

print(df)
