<h2>Cost Function</h2>

linear regression의 cost function을 그대로 사용할 수 없다.<br>
<img width="700" alt="스크린샷 2021-04-21 오전 12 24 10" src="https://user-images.githubusercontent.com/54436228/115422841-3ff7ba00-a238-11eb-960b-26054c592029.png">

linear regression cost function에 sigmoid function을 사용할 경우 왼쪽 아래그림과 같은 non-convex 함수가 된다.<br>

<img width="700" alt="스크린샷 2021-04-21 오전 12 24 18" src="https://user-images.githubusercontent.com/54436228/115422868-46863180-a238-11eb-92d7-c861d68db18a.png">

오른쪽 convex function의 경우 Gradient Descent으로 global minimum에 수렴가능하다. (linear regression 해당)<br>
하지만 왼쪽 non-convex function의 경우 global minimum에 수렴하는 것을 보장하지 못한다.<br>
그러므로 convex function이 될 수 있게 식을 변경한다.<br>

<img width="500" alt="스크린샷 2021-04-21 오전 12 39 07" src="https://user-images.githubusercontent.com/54436228/115425029-2fe0da00-a23a-11eb-8cf2-b95d930a099c.png">

<h3>y=1인 경우</h3>

<img width="500" alt="스크린샷 2021-04-21 오전 12 40 11" src="https://user-images.githubusercontent.com/54436228/115425004-2b1c2600-a23a-11eb-9234-b86d64d7dac5.png">

- 실제 값 y가 1이고 예측 값도 1인 경우 : 일치하므로 cost = 0
- 실제 값 y가 1인데 예측을 0으로 한 경우 : cost 증가


<h3>y=0인 경우</h3>

<img width="500" alt="스크린샷 2021-04-21 오전 12 24 52" src="https://user-images.githubusercontent.com/54436228/115424661-dc6e8c00-a239-11eb-82be-8ca78b7aa752.png">

- 실제 값 y가 0이고 예측 값도 0인 경우 : 일치하므로 cost = 0
- 실제 값 y가 0인데 예측을 1로 한 경우 : cost 증가
