<h2>Multivariable Linear Regression</h2>

simple linear regression은 1개의 feature로 결과를 예측했다.<br>
Multivariable Linear Regression은 2개 이상의 featrue로 결과를 예측한다.<br>

n개의 feature를 갖는 다중선형회귀 식은 다음과 같다.<br>
`H(x) = Θ0 + Θ1*x1 + Θ2*x2 + ... + Θn*xn`<br>

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)
x1_train = torch.FloatTensor([[73], [93], [89], [96], [73]])
x2_train = torch.FloatTensor([[80], [88], [91], [98], [66]])
x3_train = torch.FloatTensor([[75], [93], [90], [100], [70]])
y_train = torch.FloatTensor([[152], [185], [180], [196], [142]])

w1=torch.zeros(1, requires_grad=True)
w2=torch.zeros(1, requires_grad=True)
w3=torch.zeros(1, requires_grad=True)
b=torch.zeros(1, requires_grad=True)

optimizer = optim.SGD([w1, w2, w3, b], lr=1e-5)

nb_epochs = 20000
for epoch in range(nb_epochs + 1):
    hypothesis = x1_train * w1 + x2_train * w2 + x3_train * w3 + b
    cost = torch.mean((hypothesis - y_train) ** 2)

    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 2000== 0:
        print('Epoch {:4d}/{} w1: {:.3f} w2: {:.3f} w3: {:.3f} b: {:.3f} Cost: {:.6f}'.format(
            epoch, nb_epochs, w1.item(), w2.item(), w3.item(), b.item(), cost.item()
        ))

```

<img width="520" alt="스크린샷 2021-04-13 오후 12 20 19" src="https://user-images.githubusercontent.com/54436228/114492006-a38b5180-9c52-11eb-895d-6c94685d7431.png" width="100" height="180">

3개의 feature이므로 `H(x) = Θ0 + Θ1*x1 + Θ2*x2 + Θ3*x3` 식을 갖는다.<br>
초기 Θ0(b), Θ1(w1), Θ2(w2), Θ3(w3) 을 0로 설정한 뒤, 20000번 훈련한 결과는<br>
>Θ0(b) = 0.028<br>
Θ1(w1) = 0.933<br> 
Θ2(w2) = 0.466<br>
Θ3(w3) = 0.612<br>

`H(x) = x1 + 0.5*x2 + 0.6*x3` 식으로 유도할 수 있다.<br>
또한, training 할수록 cost value가 작아지는 것을 확인할 수 있다.<br>

