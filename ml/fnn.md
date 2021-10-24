# FNN(Feedforward Neural Network)

퍼셉트론은 선형 분리에만 적용 가능해 xor 연산을 처리할 수 없는 한계가 있는데 이를 해결한 것이 FNN 이다.<br>

![png](/_img/ml/fnn_xor.png) <br>
2개의 계층으로 구성된 **다층 퍼셉트론(MLP, multi-layer perception)** 으로 XOR 기능을 구현하며 한계를 극복했다.<br>
점점 hidden layer가 많아지면서 학습 데이터 규모가 커지고 계산량이 늘어나 학습이 어려워지는 또 다른 문제가 발생했지만 이를 오류 역전파 알고리즘(back propagation)으로 해결했다.<br>

퍼셉트론에선 계단함수를 2가지 출력으로 변경해서 사용했기 때문에 non-linear 인 경우에는 적용하지 못했다.<br>
non-linear 에는 계단함수가 아닌 **sigmoid 함수**를 활성화 함수로 사용한다.<br>

2개 이상의 계층을 갖기 때문에 초기에는 다층 퍼셉트론(MLP)라고 불렀지만, 계단함수가 아닌 sigmoid 함수를 활성화 함수로 사용하기 때문에 퍼셉트론이라고 부르는 것은 적합하지 않다. 그래서 주로 FNN(Feedforward Neural Network)라고 부른다.<br>

## Forward processing

![png](/_img/ml/fnn_processing.png) <br>

- Forward processing(순방향 처리) : 입력 샘플에 대한 추론(inference, prediction) 용도
- Backward processing(역방향 처리) : 학습을 위한 용도로 backpropagation 알고리즘을 수행하며 가중치를 갱신함

## Binary classification

FNN은 비선형 분리가 가능하기 때문에 2개 이상으로 분리 가능하다.<br>
![png](/_img/ml/fnn_binary_classification.png) <br>
2개의 클래스(C1, C2) 중에서 하나를 선택하는 이진 분류는 **출력 노드가 1개**이다.<br>
손실함수는 주로 MSE를 사용하고, 출력 뉴런은 sigmoid 함수를 사용한다.<br>


## Multiple classification

![png](/_img/ml/fnn_multiple_classification.png) <br>
q개의 클래스(C1, C2 ... Cq) 중에서 하나를 선택하는 다중 분류는 출력 뉴런이 **분류하고자 하는 클래스의 개수**만큼 필요하다.<br>
출력층은 softmax 함수를 사용하는데 이는 모든 결과의 합이 1이되는 확률로 처리한다.(아래 softmax 함수에 대한 설명)<br>

## 활성화 함수

FNN은 다음과 같은 특징이 있다.<br>

- Feed forward 방식으로 Acyclic(no cyclic) link
- 1개의 hidden layer (hidden layer가 2개 이상이면 Deep FNN)
- 다양한 활성화 함수를 사용
- 일반적으로 각 계층은 Fully-connected(FC 계층)

FNN은 응용에 따라 쓰는 활성화 함수가 다르다.<br>

- linear 계층 : linear regression(선형 회귀)에서 단순 선형 활성화 함수인 계단 함수를 사용
- sigmoid 계층 : logistic regression(로지스틱 회귀, 분류)에서 logistic sigmoid 함수 사용, 확률적 이진 분류에서 tanh(Hyperbolic tangent, 쌍곡선 함수)를 사용
- softmax 계층 : 다중 분류에서 softmax 함수를 사용 (결과 값을 확률로 계산하는 기능으로 출력층에서만 사용)

<br>

### Softmax 계층

![png](/_img/ml/softmax.png) <br>
소프트맥스 계층은 입력값을 정규화하여 출력하며, 출력층에서만 사용된다.<br>
입력값을 정규화한다는 것은 모든 출력값의 합이 1인 확률로 변환한다.<br>

### Affine 계층

행렬의 곱을 수행하는 계층으로 선형 뉴런으로 구성된 계층이다. linear 계층이라고도 한다.<br>
신경망에서 가중치합을 계산하기 위해 행렬의 곱을 사용해 y = np.dot(x, w) + b 를 계산한다. 해당 수식을 수행하기 위해선 각 벡터의 차원을 일치시켜야 한다.<br>

### non-linear 계층

![png](/_img/ml/non_linear_function.png) <br>
행렬의 곱으로 구한 가중치합을 활성화 함수로 변환해 출력한다. 응용에 따라 사용되는 활성화 함수의 종류는 다양하다.<br>
sigmoid 함수, ReLU, softmax 함수 같은 non-linear 활성화 함수를 사용하는 뉴런으로 구성된 계층을 non-linear 계층이라고 한다.<br><br>

## forward 방식(추론)에서 각 계층의 수식

신경망에서 forward 방식은 추론하는 용도로 사용된다.<br>

### 입력층 -> 은닉층

![png](/_img/ml/input_layer_expression.png) <br>
입력값 x와 가중치 W를 행렬 곱셈연산한 결과에 bias를 더한 값이 v이다.<br>
가중합 v를 다음 계층 노드에 그대로 저장하는 것이 아니라 활성화 함수로 변환한 출력값 h를 저장한다.<br>

### 은닉층 -> 은닉층

![png](/_img/ml/hidden_layer_expression.png) <br>
은닉층끼리 처리하는 방식도 입력 계층과 동일한 방식이지만 입력값이 아닌 **활성화 함수로 변환한 출력값 h**를 사용한다.<br>

### 은닉층 -> 출력층

![png](/_img/ml/output_layer_expression.png) <br>
은닉층에서 출력층으로 가는 처리 방식도 **활성화 함수로 변환한 출력값 h**를 사용<br><br>

## 단일모드, 배치 모드

![png](/_img/ml/single_mode.png) <br>
단일 모드는 한번에 한개의 입력만 처리한다. 즉, 전방처리 횟수가 데이터의 개수와 같다.<br>

![png](/_img/ml/batch_mode.png) <br>
배치 모드는 한번에 여러개의 입력(batch)을 함께 처리한다. 입력데이터가 1000개일 때 배치 크기가 100이라면 전방처리 횟수는 10이다.<br>

