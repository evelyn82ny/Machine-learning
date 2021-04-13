<h2>Single Linear Regression</h2>

1개의 feature로 결과를 예측하며, `Univariate Linear Regression`이라고도 한다.<br>

`H(x) = Θ0 + Θ1*x1`<br>
`Θ0`는 절편, `Θ1`는 기울기라고 생각하면 된다.<br>

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
    
    if epoch%100==0:
        print('Epoch {:4d}/{} W: {:.3f}, b: {:.3f} Cost: {:.6f}'.format(epoch, nb_epochs, W.item(), b.item(), cost.item()))
```

<img width="354" alt="스크린샷 2021-04-13 오전 11 44 45" src="https://user-images.githubusercontent.com/54436228/114489196-b2bbd080-9c4d-11eb-83d9-498151f509da.png" width="120" height="300">

`H(x) = Θ0 + Θ1*x1` -> `H(x) = b + W*x`<br>
W = 0, b = 0 으로 시작하여 2000번의 training 을 통해<br>
W = 1.997 , b = 0.006 으로 `H(x) = 2*x` 식과 근접한 결과를 얻을 수 있다.<br>

