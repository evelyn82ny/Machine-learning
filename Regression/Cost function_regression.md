<h2>Cost function</h2>


<img width="650" alt="스크린샷 2021-04-21 오후 1 28 28" src="https://user-images.githubusercontent.com/54436228/115496906-994a0280-a2a5-11eb-8bf2-2bae9d1da190.png">

실제 값과 예측값의 차이를 error(오류)라고 한다.<br>
error는 + / - 값을 갖기 때문에 서로 상쇄되어 오류가 없는 것처럼 보이는 문제를 발생시킨다. <br>
이를 막기 위해 error에 제곱한다.

제곱한 총합을 Data 개수로 나누는 이유는 data의 개수가 많아질수록 큰 오차 값이 나오기 때문에 평균을 적용한다. <br>

<h2>𝜃1에 대한 cost funtcion</h2>

<img width="650" alt="스크린샷 2021-04-21 오후 1 28 39" src="https://user-images.githubusercontent.com/54436228/115497271-50df1480-a2a6-11eb-847b-50cc54ac1e46.png">


<h2>𝜃0, 𝜃1에 대한 cost funtcion</h2>

2개의 𝜃0, 𝜃1에 대한 cost function 𝐽(𝜃0,𝜃1)는 3가지를 표현하기 위해 3차원이 된다.<br>

<img width="650" alt="스크린샷 2021-04-21 오후 1 28 46" src="https://user-images.githubusercontent.com/54436228/115497411-913e9280-a2a6-11eb-99ca-e693de159757.png">

