import pandas as pd
import numpy as np

data = pd.read_excel('finds.xlsx')
print("Data:\n", data)

d = np.array(data.iloc[:, :-1])
target = np.array(data.iloc[:, -1])

print("\nFeatures:\n", d)
print("\nTarget:\n", target)

def train(c, t):
    specific_hypothesis = None
    for i, val in enumerate(t):
        if val == "yes":
            specific_hypothesis = c[i].copy()
            break
    for i, val in enumerate(c):
        if t[i] == "yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
    return specific_hypothesis

final_hypothesis = train(d, target)
print("\nThe final hypothesis is:", final_hypothesis)
