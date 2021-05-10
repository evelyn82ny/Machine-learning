# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
from sklearn.preprocessing import LabelEncoder

items=['cpp', 'java', 'java', 'python', 'ruby','swift','ruby']

encoder=LabelEncoder()
encoder.fit(items)
labels=encoder.transform(items)
print(labels)
# -

print(encoder.classes_)

# +
from sklearn.preprocessing import OneHotEncoder
import numpy as np

items=['cpp', 'java', 'java', 'python', 'ruby','swift','ruby']

encoder=LabelEncoder()
encoder.fit(items)
labels=encoder.transform(items)

labels=labels.reshape(-1,1)

oh_encoder=OneHotEncoder()
oh_encoder.fit(labels)
oh_labels=oh_encoder.transform(labels)

print(oh_labels.toarray())

# +
import pandas as pd

df=pd.DataFrame({'item':['cpp', 'java', 'java', 'python', 'ruby','swift','ruby']})
pd.get_dummies(df)
# -


