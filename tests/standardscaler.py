from sklearn.preprocessing import StandardScaler
import pandas as pd

# Example data
train = pd.DataFrame({"age": [18, 22, 30, 40], "income": [1000, 2000, 5000, 10000]})

test = pd.DataFrame({"age": [25, 35], "income": [3000, 7000]})


scaler = StandardScaler()

# learn the mean and standard deviation of each columns
scaler.fit(train)

# Transform both
X_train_scaled = scaler.transform(train)
X_test_scaled = scaler.transform(test)

df = pd.DataFrame(X_train_scaled, columns=train.columns)

print(df)
