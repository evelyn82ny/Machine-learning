<h2>Evaluation index of regression model</h2>

회귀평가지표는 회귀 예측값과 실제값의 차이를 기반으로 한다.<br>
실제값과 예측값의 차이가 적은 것을 찾는게 목표이므로, 회귀평가지표의 값이 작을수록 성능이 좋은 것이다.<br>

<h3>MAE (Mean Absolute Error)</h3>
실제값과 예측값의 차이를 절대값으로 변환한 평균<br>
<img width="248" alt="스크린샷 2021-04-17 오후 1 56 04" src="https://user-images.githubusercontent.com/54436228/115102252-aeaced00-9f84-11eb-8c36-066c6dcbfb7f.png">

<h3>MSE (Mean Squared Error)</h3>
실제값과 예측값의 차이를 제곱한 평균<br>
<img width="242" alt="스크린샷 2021-04-17 오후 1 59 52" src="https://user-images.githubusercontent.com/54436228/115102383-722dc100-9f85-11eb-8aef-af3e081ddd29.png">


<h3>MSLE (Mean Squared Log Error)</h3>
MSE에 log를 적용한 값으로, Outlier로 인해 전체 오류값이 커지는 것을 막는다.<br>
<img width="375" alt="스크린샷 2021-04-17 오후 2 22 35" src="https://user-images.githubusercontent.com/54436228/115102808-6b547d80-9f88-11eb-909e-9f8fb144d141.png">


<h3>RMSE (Root Mean Squared Error)</h3>
MSE값은 오류의 제곱을 사용하므로 실제 오류평균보다 더 커지는 특성이 있으므로 root를 사용하여 방지한다.<br>
<img width="269" alt="스크린샷 2021-04-17 오후 2 00 03" src="https://user-images.githubusercontent.com/54436228/115102389-778b0b80-9f85-11eb-9566-1b0309a1b32e.png">


<h3>RMSLE (Root Mean Squared Log Error)</h3>
RMSE에 log를 적용한 값으로, Outlier로 인해 전체 오류값이 커지는 것을 막는다.<br>
<img width="347" alt="스크린샷 2021-04-17 오후 2 24 20" src="https://user-images.githubusercontent.com/54436228/115102894-e0c04e00-9f88-11eb-8056-46e3884404fc.png">


<h3>R² (R Sqaure)</h3>
분산 기반으로 예측성능을 평가하며, 1에 가까울수록 예측 정확도가 높다.<br>

**R² = 예측값 / 실제값**
