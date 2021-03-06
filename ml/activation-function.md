# 뉴런 연산

![png](/_img/ml/nn.png) <br>

- 입력과 가중치는 column vector 인데 두 벡터를 곱셈 연산하기 위해 입력 벡터를 전치 행렬(transpose matrix)로 변경해 연산한다.
  - 반대로, 가중치 벡터의 전치 행렬과 입력 행렬의 곱셈 연산 결과는 동일하다.
- 가중합 : 입력 벡터와 가중치 벡터를 곱셈 연산한 결과에 편향(bias)을 더한 값
- 활성화 함수 : 가중합을 활성화 함수에 의해 변환해 출력을 산출

### 편향을 왜 더할까

편향을 계산하지 않고 입력의 전치 행렬과 가중치 행렬의 곱셈 연산한 결과를 **순수 가중입력합**이라고 한다.<br>
순수 가중입력합에 어파인 변환(affine transformation)을 적용하는 효과를 주기 위해 bias를 더한다.<br>
> 어파인 연산에 대한 자세한 내용 : [https://namunotebook.tistory.com/29](https://namunotebook.tistory.com/29)<br>

벡터 연산 결과에 편향까지 더한 가중입력합의 수식은 다음과 같다.<br>

![png](/_img/ml/weighted_sum.png) <br>

수식을 단순화 하기 위해 편한을 w0으로 취급하면 오른쪽과 같이 변경된다.<br><br>

# 활성화 함수

가중합을 활성화 함수에 의해 변환하는데 여러 유형이 존재한다.<br>

## linear function

선형 함수를 활성화로 채택한 뉴런은 **가중합 v를 그대로 출력 y로 내보낸다.**<br>
즉, y = x 함수로 단순하지만 연산력에 제한을 받는다.<br>

## piecewise-linear function

![png](/_img/ml/piecewise_linear_function.png) <br>
piecewise-linear 함수는 선형 함수에 **Squashing을 도입**한 함수이다.<br>
Squashing을 도입했다는 의미는 어떤 기준을 넘어서면 증가/감소하지 않는 것을 말한다.<br>

## Sign function

![png](/_img/ml/sign_function.png) <br>
계단함수로 3가지 출력이 존재하지만 초기 뉴런에 적용될 땐 입력이 0인 경우도 1로 출력해 2가지 출력만 사용했다.<br>

## Rectified linear function

![png](/_img/ml/rectified_linear_function.png) <br>
Linear threshold function 이라고도 하는 해당 함수는 **가중합이 음수일 경우 0을 출력**하고, **가중합이 양수인 경우 상한값이 없다.**<br>
가중합이 양수인 경우 상한값이 없기 때문에 폭증하는 문제가 발생하는데 이를 시그모이드 함수로 해결한다.<br>

![png](/_img/ml/leaky_relu.png) <br>
축약명으로 ReLU를 사용하고 위 그래프와 같이 가중합이 음수인 경우에 음수를 출력하는 Leaky ReLU 변형이 존재한다.<br>

## Logistic sigmoid function

![png](/_img/ml/sigmoid_function2.png) <br>
[0, 1] 범위의 출력 값을 갖는 smooth 함수이다.<br>
로지스틱 시그모이드 함수는 미분이 가능하기 때문에 기울기 강하 기반 신경망 학습에 적합하다.<br>

## Hyperbolic tangent function

![png](/_img/ml/tan_sig_function.png) <br>
[-1, 1] 범위의 출력값을 갖는 smooth 함수로 tangent sigmoid(tan-sig) 함수라고도 부른다.<br>
로지스틱 시그모이드 함수처럼 미분이 가능하지만 입력 부호가 유지되는 차이점이 있다.<br>