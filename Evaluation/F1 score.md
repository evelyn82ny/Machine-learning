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
