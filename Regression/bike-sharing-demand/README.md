<h2>Bike Sharing Demand</h2>

https://www.kaggle.com/c/bike-sharing-demand/data

<h3>Evaluation</h3>

Submissions are evaluated one the Root Mean Squared Logarithmic Error RMSLE<br>
<img width="286" alt="스크린샷 2021-04-17 오후 4 46 24" src="https://user-images.githubusercontent.com/54436228/115105862-83ce9300-9f9c-11eb-9042-346712a5c201.png">
***
<h5>Ordinary Least Squares 추정 방식으로 구현한 결과는 다음과 같다.</h5>
<img width="288" alt="스크린샷 2021-04-15 오전 8 13 16" src="https://user-images.githubusercontent.com/54436228/114795518-afe5ea80-9dc9-11eb-9bb1-f62f80996586.png">

<h4>y_target log1p로 변환</h4>

기존 데이터보다 조금 더 정규분포된 형태로 만들기 위해 log1p로 변환<br>
<img width="560" alt="스크린샷 2021-04-15 오전 9 17 13" src="https://user-images.githubusercontent.com/54436228/114796227-65656d80-9dcb-11eb-927b-4224b7fbd87e.png">

<h5>log1p로 변환한 결과 다음과 같다.</h5>
<img width="281" alt="스크린샷 2021-04-15 오전 8 19 00" src="https://user-images.githubusercontent.com/54436228/114795735-431f2000-9dca-11eb-8577-b11193a99235.png">
RMSLE은 약간 줄었지만 RMSE는 더 증가했다.<br>

정렬된 diff를 보면 알 수 있듯이 오류가 컸던 데이터들의 오차가 더 커짐으로 인해 RMSE가 증가함을 알 수 있다.<br>

<h4>One-Hot Encoding</h4>

<img width="317" alt="스크린샷 2021-04-15 오전 8 20 23" src="https://user-images.githubusercontent.com/54436228/114796621-68ad2900-9dcc-11eb-8bf2-54601847c00b.png">

각 feature들의 회귀계수를 통해 아래와 같이 one-hot encoding을 진행한다.<br>

```python
X_features_ohe = pd.get_dummies(X_features, columns=['year', 'month','day', 'hour', 'holiday',
                                              'workingday','season','weather'])
```

<h5>one-hot encoding으로 Linear Regression 한 결과는 다음과 같다.</h5>
<img width="303" alt="스크린샷 2021-04-15 오전 8 39 26" src="https://user-images.githubusercontent.com/54436228/114796889-f1c46000-9dcc-11eb-989a-e53081cdda37.png">

<h5>one-hot encoding으로 Ridge (alpha=10) 한 결과는 다음과 같다.</h5>
<img width="290" alt="스크린샷 2021-04-15 오전 8 39 38" src="https://user-images.githubusercontent.com/54436228/114796934-09034d80-9dcd-11eb-81dc-358713bb2e7e.png">

<h5>one-hot encoding으로 Lasso (alpha=0.01) 한 결과는 다음과 같다.</h5>
<img width="293" alt="스크린샷 2021-04-15 오전 8 39 48" src="https://user-images.githubusercontent.com/54436228/114796986-21736800-9dcd-11eb-88d4-a5d497b16496.png">
