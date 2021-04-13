<h2>Feature scaling</h2>

Multivariable Linear Regression 에서는 많은 feature를 이용하여 결과를 도출해낸다.<br>
각각의 feature들은 평수, 방의 개수, 지하철역까지의 거리 등 서로 다른 기준이기 때문에, 당연하게도 서로 다른 범위를 갖게 된다.<br>

**10이하의 범위를 갖는 x1**와 **400,000이상 2,000,000이하의 범위를 갖는 x2**인 2개의 feature가 있다.<br>
해당 hypothesis는 `H(x) = Θ1*x1 + Θ2*x2 , (Θ0가 0인 경우)` 으로 작성한다.<br>
이때 x2의 범위가 훨씬 크기때문에 `Θ1` 의 크기가 커지며.<br>
반대로 x1의 범위는 작기때문에 `Θ2` 의 크기가 작아진다.<br>

`Θ1, Θ2` 에 대한 그래프는 오른쪽과 같다.<br>
해당 그래프는 탐색을 많이 하게되므로 시간이 많이 걸린다는 문제를 갖는다.<br>
<img width="913" alt="스크린샷 2021-04-13 오후 1 48 34" src="https://user-images.githubusercontent.com/54436228/114498413-01259b00-9c5f-11eb-9118-d398eca6b935.png">

Feature scaling을 통해 feature간의 범위를 조절하여 Θ값을 비슷하게 만든다.<br>
Θ값을 비슷하게 만들면 오른쪽과 같은 그래프가 나오며, 왼쪽 그래프보다 빨리 결과를 찾을 수 있다.<br>
<img width="960" alt="스크린샷 2021-04-13 오후 1 48 45" src="https://user-images.githubusercontent.com/54436228/114498420-04208b80-9c5f-11eb-9565-1c2ace42982d.png">
