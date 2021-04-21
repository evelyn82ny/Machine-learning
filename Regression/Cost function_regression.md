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

𝐽(𝜃)=0 경우 𝐽(𝜃1)의 값이 최소가 되는 cost function은 다음과 같다.<br>

<img width="650" alt="스크린샷 2021-04-21 오후 1 28 39" src="https://user-images.githubusercontent.com/54436228/115497271-50df1480-a2a6-11eb-847b-50cc54ac1e46.png">


<h2>𝜃0, 𝜃1에 대한 cost funtcion</h2>

2개의 𝜃0, 𝜃1에 대한 cost function 𝐽(𝜃0,𝜃1)는 3가지를 표현하기 위해 3차원이 된다.<br>

<img width="650" alt="스크린샷 2021-04-21 오후 1 28 46" src="https://user-images.githubusercontent.com/54436228/115497411-913e9280-a2a6-11eb-99ca-e693de159757.png">

3차원 그래프를 오른쪽과 같이 2차원 등고선 표현하며, 등고선 중심와 가까울수록 좋은 hypothesis이다.<br>

오른쪽 빨간색 X은 중심과 많이 떨어져있으며, 왼쪽 그래프를 통해 알 수 있듯이 많은 error가 발생되는 hypothesis임을 알 수 있다.<br>
<img width="605" alt="스크린샷 2021-04-21 오후 1 45 38" src="https://user-images.githubusercontent.com/54436228/115498105-e4651500-a2a7-11eb-8ada-ac88f6a681cc.png">


오른쪽 빨간색 X은 중심과 근접하며 왼쪽 그래프를 통해 실제 데이터와 근접한 hypothesis임을 알 수 있다.<br>
<img width="586" alt="스크린샷 2021-04-21 오후 1 45 45" src="https://user-images.githubusercontent.com/54436228/115498489-9ef51780-a2a8-11eb-9881-13d29fe2451f.png">
