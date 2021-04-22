<h2>Santander Customer Satisfaction</h2>

https://www.kaggle.com/c/santander-customer-satisfaction

<h3>Evaluation</h3>

Submissions are evaluated on area under the ROC curve between the predicted probability and the observed target.
***

```python
print(cust_df['TARGET'].value_counts())
unsatisfied_cnt=cust_df[cust_df['TARGET']==1].TARGET.count()
total_cnt=cust_df.TARGET.count()

print('unsatisfied ratio : {:.2f}'.format(unsatisfied_cnt/total_cnt))
```

<img width="300" alt="스크린샷 2021-04-22 오후 4 15 08" src="https://user-images.githubusercontent.com/54436228/115671883-ef8e7280-a385-11eb-93ce-300436b5d5ea.png">

만족하지 못한 사람(positive, 1)은 3008명으로 전체 데이터의 0.04 이다.<br>

```python
cust_df.describe()
print(cust_df['var3'].value_counts()[:10])
cust_df['var3'].replace(-999999, 2, inplace=True)
```
<img width="650" alt="스크린샷 2021-04-22 오후 4 21 15" src="https://user-images.githubusercontent.com/54436228/115672701-c7ebda00-a386-11eb-8f1f-5e1a511b7e5a.png">

var3의 min값이 -999999로 다른 수치에 비해 이상하다는 것을 알 수 있다.<br>
-999999인 116개의 데이터를 Null 값으로 추측하여, 116개의 데이터를 가장 많은 2로 변경한다.<br>

```python

X_features=cust_df.iloc[:, :-1]
y_labels=cust_df.iloc[:, -1]
X_train, X_test, y_train, y_test=train_test_split(X_features, y_labels, test_size=0.2, random_state=0)

```
<img width="300" alt="스크린샷 2021-04-22 오후 4 26 42" src="https://user-images.githubusercontent.com/54436228/115673401-8f003500-a387-11eb-9db9-ea86b70081a6.png">

