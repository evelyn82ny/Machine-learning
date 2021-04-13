<h2>Overfitting</h2>

주어진 train_data에 대해서는 오차가 적지만, 실제 test_data에서는 큰 오차를 보여 성능이 나빠짐을 말한다.<br>

해당 [코드](https://github.com/evelyn82/Machine-learning/blob/main/Linear%20Regression/Overfitting.py)는 Cosine Data로
Polynomial regression의 Degree를 증가시킬 때마다 변화를 측정한다.<br>
<img width="300" alt="스크린샷 2021-04-13 오후 4 22 35" src="https://user-images.githubusercontent.com/54436228/114514698-8799a700-9c76-11eb-94a8-cae9ef8ad867.png">

아래 그래프는 `degrees = [1, 3, 5, 7, 10, 15]`일 때를 나타낸다.<br>
<img width="751" alt="스크린샷 2021-04-13 오후 4 21 50" src="https://user-images.githubusercontent.com/54436228/114515513-65545900-9c77-11eb-87dc-7bbccb6e1011.png">
