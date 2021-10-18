<h2>Impurity</h2>

해당 범주 안에 서로 다른 데이터가 섞여 있는지를 말한다.<br>
Decision Tree는 impurity를 최소화하면서 over fitting이 발생되지 않는 방향으로 학습을 진행한다.<br>
<img width="300" alt="스크린샷 2021-04-19 오전 11 31 40" src="https://user-images.githubusercontent.com/54436228/115174342-0de53b80-a104-11eb-9ec4-1f0b7f7841ed.png">

- 범주 내에 같은 데이터가 많은 경우 : impurity가 낮다. ( = purity가 높다.)

- 범주 내에 여러 데이터가 많은 경우 : impurity가 높다. ( = purity가 낮다.)


<h2>Entropy</h2>

entropy는 주어진 데이터 집합의 impurity를 수치적으로 나타낸다.<br>
주어진 데이터 집합에 같은 종류의 데이터가 많으면 entropy가 낮고,<br>
다른 종류의 데이터가 많으면 entropy가 높다.<br>

0과 1사이의 값을 가지며 1로 갈수록 혼합도가 높고, 0으로 갈수록 같은 데이터가 많은 혼합도가 적음을 의미한다.<br>

<img width="200" alt="스크린샷 2021-04-19 오후 10 50 06" src="https://user-images.githubusercontent.com/54436228/115247273-9d6d0780-a161-11eb-8050-04afbfde2ff3.png">

> p(x) : 한 범주 내에 존재하는 데이터 중 x가 나올 확률

아래와 같이 식을 변경한다.<br>
<img width="200" alt="스크린샷 2021-04-19 오후 11 41 02" src="https://user-images.githubusercontent.com/54436228/115255111-eb393e00-a168-11eb-9b55-7f051e4fc3d8.png">

만약 모든 요소들이 나올 확률이 동일하다면 p(x)의 총합이 1이 되므로 수식이 아래와 같이 변경된다.<br>
<img width="200" alt="스크린샷 2021-04-19 오후 11 41 05" src="https://user-images.githubusercontent.com/54436228/115255127-ed030180-a168-11eb-90ca-24c521b0da94.png">

<img width="200" src="https://user-images.githubusercontent.com/54436228/115255205-fdb37780-a168-11eb-8d26-56eab33dcbf0.JPG">

-logx의 경우 x가 작아질수록 y가 증가한다.<br>
* x가 작아질수록 = p(x)의 값이 작아질수록 = x 데이터가 나올 확률이 적어질수록
* y가 증가한다 = entropy 가 증가한다 = impurity 높아진다.


<h2>Infomation Gain 정보이득</h2>

Entropy을 기반으로 하며, Decision tree는 정보이득이 커지는 방향으로 분할 기준을 정한다.<br>
<img width="400" alt="스크린샷 2021-04-19 오후 2 14 15" src="https://user-images.githubusercontent.com/54436228/115184819-928e8480-a119-11eb-9767-a3acb1f6460e.png">
상위노드의 entropy에서 하위노도의 enttopy의 총합을 뺀다.<br>
즉, 특성 속성을 기준으로 entropy의 감소량에 대한 기대치를 의미한다.<br><br>

entropy는 0에 가까워질수록 impurity가 줄어든다.<br>
entropy가 줄어들수록 information gain이 커진다.<br>
그러므로 information gain이 더 큰 속성을 기준으로 구분한다.<br>
