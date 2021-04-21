<h2>Cost function</h2>

Hypothesis에 대한 값과 실제 데이터의 차이에 대한 값으로 정의된다.<br>
cost function을 **𝐽(𝜃)** 라고 하며, **𝐽(𝜃)의 값이 최소가 되도록 θ를 찾는다.**<br>
<img width="308" alt="스크린샷 2021-04-17 오후 1 14 47" src="https://user-images.githubusercontent.com/54436228/115101413-f761a780-9f7e-11eb-8f6b-061e1d118721.png">
<img width="650" alt="스크린샷 2021-04-21 오후 1 28 28" src="https://user-images.githubusercontent.com/54436228/115496906-994a0280-a2a5-11eb-8bf2-2bae9d1da190.png">

**ℎ𝜃(𝑥)−𝑦** 를 error(오차)라고 하며, 오차의 값은 양수 / 음수의 값이 나온다.<br>
양수와 음수가 서로 상쇄되는 것을 막기위해 **ℎ𝜃(𝑥)−𝑦** 에 제곱을 한다.<br>
제곱한 총합을 Data 개수로 나누는 이유는 data의 개수가 많아질수록 큰 오차 값이 나오기 때문에 평균을 적용한다. <br>
위 식은 모든 오차의 제곱을 더해 평균한 MSE(Mean Square Error)이며, 다양한 비용함수 중 가장 보편적으로 사용된다.<br>


<h2>𝜃1에 대한 cost funtcion</h2>

<img width="650" alt="스크린샷 2021-04-21 오후 1 28 39" src="https://user-images.githubusercontent.com/54436228/115497271-50df1480-a2a6-11eb-847b-50cc54ac1e46.png">


<h2>𝜃0, 𝜃1에 대한 cost funtcion</h2>

2개의 𝜃0, 𝜃1에 대한 cost function 𝐽(𝜃0,𝜃1)는 3가지를 표현하기 위해 3차원이 된다.<br>

<img width="650" alt="스크린샷 2021-04-21 오후 1 28 46" src="https://user-images.githubusercontent.com/54436228/115497411-913e9280-a2a6-11eb-99ca-e693de159757.png">

