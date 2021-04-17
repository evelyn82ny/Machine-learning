<h2>Regression</h2>

**Regression analysis란 관찰된 연속형 변수들 사이의 모델을 구현하여 적합도를 측정해 내는 분석 방법**이라고 wikipedia에 정의되어있다.<br>

<h3>Hypothesis</h3>
<img width="1045" alt="스크린샷 2021-04-17 오후 12 53 44" src="https://user-images.githubusercontent.com/54436228/115101053-1ad72300-9f7c-11eb-8950-9effd01a92d4.png">

- m : Number of training examples
- 𝑥′𝑠 : input variable or features
- 𝑦′𝑠 : output variable" or target value
- (x,y) : one training example
- (𝑥𝑖,𝑦𝑖) : i-th training example
- θ : Regression coefficient(Parameter)


**X(feature)** , **H(target)** 를 기반으로 하는 Supervised Learning 통해 최적의 **θ(coefficient)** 를 찾아낸다.<br>

<h3>Cost function</h3>

Hypothesis에 대한 값과 실제 데이터의 차이에 대한 값으로 정의된다.<br>
cost function을 **𝐽(𝜃)** 라고 하며, **𝐽(𝜃)의 값이 최소가 되도록 θ를 찾는다.**<br>
<img width="308" alt="스크린샷 2021-04-17 오후 1 14 47" src="https://user-images.githubusercontent.com/54436228/115101413-f761a780-9f7e-11eb-8f6b-061e1d118721.png">

**ℎ𝜃(𝑥)−𝑦** 를 error(오차)라고 하며, 오차의 값은 양수 / 음수의 값이 나온다.<br>
양수와 음수가 서로 상쇄되는 것을 막기위해 **ℎ𝜃(𝑥)−𝑦** 에 제곱을 한다.<br>
위 식은 모든 오차의 제곱을 더해 평균한 MSE(Mean Square Error)이며, 다양한 비용함수 중 가장 보편적으로 사용된다.<br>

 
<h2>Single Linear Regression</h2>

1개의 feature로 결과를 예측하며, `Univariate Linear Regression`이라고도 한다.<br>

`H(x) = b + w1*x1`<br>

`H(x) = 2*x`의 수식을 알고있는 상태에서 x_train, y_train 값을 입력하여<br>
`Θ1` = 2, `Θ0` = 0 의 값을 갖는지 아래 결과로 확인할 수 있다.<br>
```python

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)
x_train=torch.FloatTensor([[1], [2], [3]])
y_train=torch.FloatTensor([[2], [4], [6]])

W=torch.zeros(1, requires_grad=True)
b=torch.zeros(1, requires_grad=True)

optimizer=optim.SGD([W,b], lr=0.01) # lr : learning rate

nb_epochs=2000
for epoch in range(nb_epochs+1):
    hypothesis=x_train*W+b
    cost=torch.mean((hypothesis-y_train)**2)
    
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()
    
    if epoch%200==0:
        print('Epoch {:4d}/{} W: {:.3f}, b: {:.3f} Cost: {:.6f}'.format(epoch, nb_epochs, W.item(), b.item(), cost.item()))
```
<img width="345" alt="스크린샷 2021-04-17 오후 4 15 06" src="https://user-images.githubusercontent.com/54436228/115105202-4831ca00-9f98-11eb-8917-b62721446b6d.png">

W = 0, b = 0 으로 시작하여 2000번의 training 을 통해<br>
W = 1.997 , b = 0.006 으로 `H(x) = 2*x` 식과 근접한 결과를 얻을 수 있다.<br>


<h2>Multivariable Linear Regression</h2>

Multivariable Linear Regression은 2개 이상의 featrue로 결과를 예측한다.<br>

n개의 feature를 갖는 다중선형회귀 식은 다음과 같다.<br>
`H(x) = b + W1*x1 + W2*x2 + ... + Wn*xn`<br>

```python
x_train  =  torch.FloatTensor([[73,  80,  75], 
                               [93,  88,  93], 
                               [89,  91,  80], 
                               [96,  98,  100],   
                               [73,  66,  70]])  
y_train  =  torch.FloatTensor([[152],  [185],  [180],  [196],  [142]])

W = torch.zeros((3, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)
optimizer = optim.SGD([W, b], lr=1e-5)

nb_epochs = 20
for epoch in range(nb_epochs + 1):

    hypothesis = x_train.matmul(W) + b
    cost = torch.mean((hypothesis - y_train) ** 2)

    optimizer.zero_grad()
    cost.backward()
    optimizer.step()
    
    if epoch%5==0:
        print('\n\nEpoch {:4d}/{} hypothesis: {} Cost: {:.3f}'.format(
        epoch, nb_epochs, hypothesis.squeeze().detach(), cost.item()
    ))
        print('\nW: {} , b: {}'.format(W.squeeze().detach(), b))
```

<img width="679" alt="스크린샷 2021-04-17 오후 4 25 24" src="https://user-images.githubusercontent.com/54436228/115105387-8b406d00-9f99-11eb-90df-95eccf922d2c.png">

초기 b, w1, w2, w3을 0로 설정한 뒤, 20000번 훈련한 결과는<br>
>w1 = 0.6807<br> 
w2 = 0.6785<br>
w3 = 0.6677<br>
b = 0.0079<br>

`H(x) = 0.68*x1 + 0.678*x2 + 0.6677*x3 + 0.0079` 식으로 유도할 수 있다.<br>
또한, training 할수록 cost value가 작아지는 것을 확인할 수 있다.<br>
