<h2>F1 Score</h2>

F1 score는 recall과 precision의 조화 평균이다.

<img width="500" alt="스크린샷 2021-04-22 오후 1 28 25" src="https://user-images.githubusercontent.com/54436228/115656771-b8619680-a370-11eb-9a70-dbf757dc9903.png">


<h4>recall = 0.01 / precision = 1 인 경우</h4>

> F1 = 2 * (0.01) / 1.01 = 0.0198

<h4>recall = 0.5 / precision = 0.5 인 경우</h4>

> F1 = 2 * 0.25 / 1 = 0.5

recall과 precision의 값이 비슷할수록 F1 score 값이 증가하여 좋아진다.<br>

 <h3>조화 평균을 사용하는 이유</h3>
  
한가지 값이 극단적으로 낮을땐 F1 score도 낮게 나오고, 두 값이 모두 높을 경우 F1 score도 높게 나와야 하기 떄문에 harmonic mean 조화 평균을 사용한다.<br>

> 산술 평균 arithmetic mean = (0.01 + 1) / 2 = 0.505<br>
> 조화 평균 harmonic mean = 2 * (1 * 0.01) / (1 + 0.01) = 0.0198<br>

***

> 아래 모든 수식은 wikipedia 에서 사용
> 아래 모든 그래프는 gaussian37.github.io 에서 사용

<h2>Arithmetic mean</h2>

Arithmetic mean 산술평균이란 주어진 모든 수의 합을 주어진 수의 개수로 나눈 값이다.<br>

<img width="300" alt="스크린샷 2021-04-22 오후 3 06 30" src="https://user-images.githubusercontent.com/54436228/115664093-5e66ce00-a37c-11eb-826c-1b34124b128f.png">

<img width="350" alt="스크린샷 2021-04-22 오후 3 06 39" src="https://user-images.githubusercontent.com/54436228/115664160-72aacb00-a37c-11eb-814c-18835cb19bae.png">

위 그래프는 1, 4, 7, 10, 13, 16, 19 인 7개의 데이터(파란점)와 7개의 평균인 10(빨간점)을 나타낸 그래프이다.<br>
위와 같이 산술 평균은 데이터가 선형이거나 등차 관계가 가까울수록 제대로 된 결과를 얻을 수 있다.<br>


<h2>Geometric mean</h2>

Geometric mean 기하 평균은 양수인 n개의 모든 데이터를 곱한 값에 n 제곱근한 결과이다.<br>

<img width="300" alt="스크린샷 2021-04-22 오후 3 15 21" src="https://user-images.githubusercontent.com/54436228/115665023-9f131700-a37d-11eb-8e73-c08ee1880544.png">

<img width="350" alt="스크린샷 2021-04-22 오후 3 22 30" src="https://user-images.githubusercontent.com/54436228/115665691-996a0100-a37e-11eb-9b57-603d083e1d79.png">

위 그래프는 1, 3, 9, 27, 81, 243, 729 인 7개의 데이터(파란점)과 7개의 기하평균 27(빨간점)을 나타낸 그래프이다.<br>

