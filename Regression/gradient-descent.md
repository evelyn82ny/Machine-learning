# 신경망 (뉴럴 네트워크, neural network)

![png](/_img/regression/neural_network.png) <br>

입력에 대한 실제 출력과 목표출력(target)을 근접한 값을 갖도록 가중치를 조정하는 작업을 신경망 학습이라고 한다.<br>
신경망 학습법은 분석적 기법과 에러 정정 기법 2가지 방식이 있다.<br>

- 분석적 기법 : 방정식을 구한 후 해를 계산하는 방식으로 대표적인 Wiener-Hoff 방정식이 있다.
- 에러 정정 기법 : 오차를 점진적으로 줄여가는 방식으로 퍼셉트론 학습법, 기울기 강하 기법이 있다.
  - 기울기 강하 기법은 단층 신경망에 적용되는 델타 규칙과 다층 신경망에 적용되는 백프로퍼게이션(역전파 학습) 알고리즘이 있다.

## 분석적 기법 : Wiener filter model

![png](/_img/regression/wiener_filter_model.png) <br>

Wiener filter란 신호 잡음 최소화를 위한 선형 필터 모델이다.<br>
입력 신호 x와 가중치 w를 곱한 모든 합이 실제 출력 결과인데, 이 실제 출력 결과와 목표 출력(target)이 근접한 값을 갖도록 가중치 w를 조정한다. 편향이 0이라고 가정할 때 가중치 w를 조정한다는 측면에서 보면 선형 뉴런 모델과 동일하다.<br>
손실 함수(loss function)는 **MSE(평균 제곱 에러)** 를 사용하고 손실 함수 최소화를 위한 분석적인 해는 다음과 같다.<br>

![png](/_img/regression/loss_function_w.png) <br>

행렬의 inverse가 존재하지 않는 singular(비가역) 이면 계산이 불가해서 Wiener 필터 모델을 신경망에 적용하기 적절하지 않다고 결론났다.<br><br>

## error correction scheme 에러 정정 기법

1. 입력 샘플 x에 대해 출력 y를 산출한다.
2. 출력 y와 목표 출력 d 간의 차이인 손실(에러)가 줄어들도록 가중치를 변경한다.

에러 정정 기법은 과정 1, 2를 모든 입력 샘플에 대해 반복하며 최적의 가중치를 찾는다.<br>
분석적 기법은 모든 입력 x와 가중치 w를 곱한 결과를 모두 더해 가중치를 조정했다면, 에러 정정 기법은 입력 샘플을 계산하면서 가중치를 바꿔나간다는 차이가 있다. 또한 분석적 기법은 수식으로 해결한다면 에러 정정 기법은 수식이 아니고 튜닝을 한다는 개념이다.<br>

- 손실 함수 정량화로 목표 출력과 실제 출력을 계산하고
- 기울기 강하 기법으로 손실이 줄어들도록 가중치를 변경한다.

## Loss function

손실함수는 목표치와 실제 출력 간의 차이(손실, 에러)를 계량화하는 함수로 오차함수, 에러함수라고도 한다.<br>
손실함수의 종류는 평균제곱에러(for regression), 교차엔트로피 에러(for classification) 등이 있다.<br>

- MSE 평균제곱에러 : 출력값과 목표치 차이에 제곱에 1/2를 곱하고, 모든 입력에 대한 해당 값의 평균

<br>

# Gradient Descent 기울기 강하 기법

각 점은 각 성분 xi에 대한 접선의 기울기를 갖는다. 접선의 기울기를 성분으로 하는 벡터(기울기를 모아둔 것)를 해당 위치의 gradient라고 한다.<br>

![png](/_img/regression/gradient1.png) <br>

기울기 강하 기법의 기본원리는 함수의 접선 기울기를 사용해 함수의 최소값을 구한다. 정확하게 말하면 최소값을 갖는 파라미터(독립변수 x값)를 구한다.<br>
기울기가 양수일 땐 최소값을 찾기 위해 왼쪽으로 이동하며 탐색하고, 기울기가 음수일 땐 오른쪽으로 이동하며 최소값을 찾는데 이런식으로 시작점부터 반복적으로 파라미터 값을 갱신해 나간다.<br>

## learning rate

갱신시점마다 얼마나 증분할 것인가 대해서도 고민해야 하는데 다음지점을 구하기 위해 갱신률(update rate, learning rate) 사용한 식은 다음과 같다.<br>

![png](/_img/regression/gradient_expression.png) <br>
![png](/_img/regression/gradient2.png) <br>

현재 기울기에 갱신률을 곱한 값을 뺀 결과가 다음 탐색 지점인데 빼는 이유는 다음과 같다.<br>
기울기가 음수인 경우 최소값을 찾기 위해 오른쪽으로 이동해야 하는데 이미 기울기가 음수값이므로 오른쪽으로 이동하기 위해 파라미터 값이 증가해야하므로 음수값을 빼 증가시킨다.<br>
반대로 기울기가 양수인 경우 최소값을 찾기 위해 왼쪽으로 이동해야 하고 이미 기울기가 양수값이므로 양수값을 빼면 파라미터 값이 감소해 왼쪽으로 이동하게 된다.<br>
그러므로 현재 기울기에 갱신률을 곱한 값을 **빼주면** 다음 파라미터를 구할 수 있다.<br>

![png](/_img/regression/learning_rate_diff.png) <br>

learning rate가 작은 값이면 왼쪽과 같이 수렴하는 과정이 길어진다.<br>
수렴과정을 단축하기 위해 learning rate를 큰 값을 사용하면 오른쪽과 같이 최소점 주위에서 계속 진동하거나 다시 발산하는 문제가 생기기도 한다.<br>

## gradient descent의 한계점

![png](/_img/regression/global_minima.png) <br>

여러 최소점이 존해하는데 이를 local minima라고 한다. 여러개의 local minima 중 제일 작은 값인 global minima(전역 최소점)를 찾아야 한다.<br>
하지만 global minima가 아닌 다른 지점에서 local minima에 도달했다면 global minima에 도달할 수 없는데 이것이 gradient descent의 한계점이다.<br>

## 신경망에서 gradient descent 기법 적용

신경망에서는 가중치 갱신에 gradient descent를 적용한다.<br>
신경망의 loss function L(x, w) 에서 입력 x는 사실상 상수이므로 가중치 w에 의해 값이 결정된다.<br>
수렴 상태에 도달하기 위해 가중치 w를 변경하기 위해 gradient descent를 적용하고 식은 다음과 같다.<br>

![png](/_img/regression/gradient_expression.png) <br>
![png](/_img/regression/neural_network.png) <br>

입력 샘플에 대한 손실함수를 통해 최적의 가중치를 계속해서 갱신한다.<br>







