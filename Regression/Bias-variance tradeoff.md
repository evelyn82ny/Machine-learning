<h2>Bias-variance tradeoff</h2>

Bias-variance tradeoff는 Supervised Learning에서 주어진 training set에 대해서 지나치게 일반화하는 것을 예방하기 위해 bias(편향), variance(분산)를 최소화하는 것을 말한다.<br>

- bias(편향) : 잘못된 가정으로 underfitting 문제를 발생시키는 오차<br>
- variance(분산) : 주어진 training set에 대한 오차가 적지만, 실제 test_data에서는 큰 오차를 보여 성능이 나빠지는 overfitting을 발생시기는 오차<br>


http://scott.fortmann-roe.com/docs/BiasVariance.html 에서 사진 사용<br>
<img width="500" src="https://user-images.githubusercontent.com/54436228/115192618-03d43480-a126-11eb-8cdd-ba5a1ec52e57.png">


<h2>구현</h2>

해당 [Overfitting.py](https://github.com/evelyn82/Machine-learning/blob/main/Linear%20Regression/Overfitting.py) 코드는 Cosine Data로
Polynomial regression의 Degree를 증가시킬 때마다 변화를 측정한다.<br>
<img width="300" alt="스크린샷 2021-04-13 오후 4 22 35" src="https://user-images.githubusercontent.com/54436228/114514698-8799a700-9c76-11eb-94a8-cae9ef8ad867.png">

아래 그래프는 `degrees = [1, 3, 5, 7, 10, 15]`일 때를 나타낸다.<br>
<img width="600" alt="스크린샷 2021-04-13 오후 4 21 50" src="https://user-images.githubusercontent.com/54436228/114515513-65545900-9c77-11eb-87dc-7bbccb6e1011.png">

<h3>MSE</h3>

> MSE(Mean Squared Error) : 실제 값과 예측값의 차이를 제곱한 평균 값<br>

<img width="228" alt="스크린샷 2021-04-13 오후 4 19 45" src="https://user-images.githubusercontent.com/54436228/114517647-80c06380-9c79-11eb-9354-17f6f2748a9a.png">

**Degree 1**일 때 모델이 간단해서 기존 데이터와의 오류가 줄지 않는 상태인 Underfitting 이다.<br>

**Degree 5**일 때 MSE의 값이 제일 작다.<br>
즉, 새로운 test data 가 입력되어도 오차가 발생할 비율이 가장 적은 최적의 경우이다.<br>

**Degree 15**일 때 커질 땐 실제 데이터와의 오차는 **Degree 5**일 때보다 적다.<br>
하지만 머신러닝이란 새로운 데이터에 대해 정확도가 높은 예측값을 찾아내는 것이 목표다.<br>
MSE값을 통해 새로운 데이터에 대한 오차가 큰 Overfitting이며, 좋은 모델이 아님을 알 수 있다.<br>

<img width="600" alt="스크린샷 2021-04-13 오후 5 06 17" src="https://user-images.githubusercontent.com/54436228/114518716-9c783980-9c7a-11eb-8fe2-322c607924b9.png">

<h3>Regression coefficient</h3>

Degree가 커질수록 coefficient의 범위도 늘어나는 문제가 발생한다.<br>
해당 문제는 Lasso, Ridge, ElasticNet Regularization으로 해결한다.<br>

<img width="550" alt="linear regression coefficient" src="https://user-images.githubusercontent.com/54436228/114531188-a2741780-9c86-11eb-91fe-73d57594a4c0.png">



