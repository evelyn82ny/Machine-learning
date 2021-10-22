# Delta rule (Widrow & Hoff 학습법)

- 1개의 계층만 존재하는 단층 신경망에 대한 기울기 강하 학습을 델타 규칙이라고 한다.
- 손실 함수는 MSE를 사용한다.

![png](/_img/regression/delta_loss_function_expression.png)<br>

MSE는 입력 샘플과 가중치가 필요한데 입력 샘플은 사실상 상수이므로 가중치에 대한 함수라 말할 수 있다.<br>

## 입력 성분이 1개인 경우

입력 성분이 1개인 경우 위 MSE 수식이 다음과 같은 식이 된다.<br>
![png](/_img/regression/delta_loss_one_dimensional_expression.png) <br>
에러 기울기는 최종적으로 손실함수가 가중치에 의해 미분된 값이다.<br>

## 입력 성분이 2개인 경우

입력 성분이 2개인 경우 위 MSE 수식이 다음과 같은 식이 된다.<br>
![png](/_img/regression/delta_loss_two_dimensional_expression.png) <br>

## delta rule의 증분값

![png](/_img/regression/delta_learning_rate.png) <br>

## 선형 뉴런

- parabolic 2차 함수
- 글로벌 최소값은 하나 존재하고, local 최소값은 존재하지 않음

## 비선형 뉴런

![png](/_img/regression/non_linear_loss_function_expression.png)

- 다양한 함수로 표현
- 글로벌 최소값은 하나 존재하고, local 최소값도 존재할 수 있음