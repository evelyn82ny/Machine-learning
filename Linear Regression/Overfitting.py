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
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
# %matplotlib inline

def cosFunc(X):
    return np.cos(1.5 * np.pi * X)

np.random.seed(0)
X=np.sort(np.random.rand(30))
y=cosFunc(X)+np.random.randn(30)*0.1

plt.scatter(X, y)

# +
plt.figure(figsize=(20, 13))
degrees=[1, 3, 5, 7, 10, 15]

for i in range(len(degrees)):
    ax=plt.subplot(2, 3, i+1)
    plt.setp(ax, xticks=(), yticks=())
    
    polynomial_features=PolynomialFeatures(degree=degrees[i], include_bias=False)
    linear_regression=LinearRegression()
    pipeline=Pipeline([('polynomial_features', polynomial_features),
                      ('linear_regression',linear_regression)])
    pipeline.fit(X.reshape(-1, 1), y)
    
    scores=cross_val_score(pipeline, X.reshape(-1, 1), y, scoring="neg_mean_squared_error", cv=10)
    coefficients=pipeline.named_steps['linear_regression'].coef_
    
    print('\nDegree {0} , Regression coefficient : {1}'.format(degrees[i], np.round(coefficients),2))
    print('Degree {0} , MSE : {1:.3f}'.format(degrees[i], -1*np.mean(scores)))
   
    X_test=np.linspace(0,1,100)

    plt.plot(X_test, pipeline.predict(X_test[:, np.newaxis]), label="Model") 
    plt.plot(X_test, cosFunc(X_test), '--', label="True function")
    plt.scatter(X, y, edgecolor='b', s=20, label="Samples")
    
    plt.xlabel("x"); plt.ylabel("y"); plt.xlim((0, 1)); plt.ylim((-2, 2)); plt.legend(loc="best")
    plt.title("Degree {}\nMSE = {:.2e}(+/- {:.2e})".format(degrees[i], -scores.mean(), scores.std()))

plt.show()
# -


