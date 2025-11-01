import pandas as pd
import time
import swifter

df = pd.DataFrame({"a": range(10000)})


def slow_func(x):
    time.sleep(0.001)
    return x**2


# normal apply
t1 = time.time()
df["b"] = df["a"].apply(slow_func)
print("Normal apply:", time.time() - t1)

# swifter apply
t2 = time.time()
df["c"] = df["a"].swifter.apply(slow_func)
print("Swifter apply:", time.time() - t2)
